import { History, Plus, RotateCcw, ShieldCheck } from "lucide-react";
import React, { useState } from "react";
import type { DatabaseHealth, DatabaseStatus, SnapshotSummary } from "../index.ts";
import type { SkillType } from "../types/notebook.ts";
import { SKILL_NAMES } from "../../cell/services/skillTemplates.ts";

interface Props {
  addType: SkillType;
  databaseStatus?: DatabaseStatus;
  dbHealth?: DatabaseHealth | null;
  snapshots?: SnapshotSummary[];
  onAddTypeChange: (skill: SkillType) => void;
  onAddCell: () => void;
  onResetToSample: () => void;
  onCreateSnapshot?: () => Promise<boolean>;
  onRestoreSnapshot?: (snapshotId: number) => Promise<boolean>;
}

export const NotebookToolbar: React.FC<Props> = ({
  addType,
  databaseStatus,
  dbHealth,
  snapshots = [],
  onAddTypeChange,
  onAddCell,
  onResetToSample,
  onCreateSnapshot,
  onRestoreSnapshot,
}) => {
  const [snapshotMessage, setSnapshotMessage] = useState("");

  const handleReset = () => {
    if (
      confirm(
        "Reset current notebook to the default sample? Make sure you have exported your work first.",
      )
    ) {
      onResetToSample();
    }
  };

  const handleCreateSnapshot = async () => {
    if (!onCreateSnapshot) return;
    setSnapshotMessage("Saving checkpoint…");
    const ok = await onCreateSnapshot();
    setSnapshotMessage(ok ? "Checkpoint created!" : "Failed to create checkpoint");
    setTimeout(() => setSnapshotMessage(""), 3000);
  };

  const handleRestore = async (id: number, reason: string) => {
    if (!onRestoreSnapshot) return;
    if (
      confirm(
        `Restore notebook to checkpoint #${id} (${reason})? Any uncommitted changes will be replaced.`,
      )
    ) {
      setSnapshotMessage(`Restoring #${id}…`);
      const ok = await onRestoreSnapshot(id);
      setSnapshotMessage(ok ? `Restored #${id}` : "Restore failed");
      setTimeout(() => setSnapshotMessage(""), 3000);
    }
  };

  const isDbConnected = databaseStatus === "connected";

  return (
    <div className="notebook-toolbar">
      <div className="toolbar-inner">
        <div className="add-control">
          <select
            aria-label="New cell skill"
            value={addType}
            onChange={(e) => onAddTypeChange(e.target.value as SkillType)}
          >
            {Object.entries(SKILL_NAMES).map(([key, label]) => (
              <option key={key} value={key}>
                {label}
              </option>
            ))}
          </select>
          <button className="button primary" onClick={onAddCell}>
            <Plus size={16} />
            Add cell
          </button>
        </div>
        <details className="notebook-options">
          <summary className="button quiet">
            {isDbConnected ? (
              <span className="options-db-badge">
                <span className="options-db-dot" />
                Database Active
              </span>
            ) : (
              "Options"
            )}
          </summary>
          <div className="options-panel">
            <p>Shift + Enter: mark visited and advance to the next cell.</p>

            <div className="options-db-section">
              <div
                className={`options-db-header ${isDbConnected ? "connected" : "offline"}`}
              >
                <ShieldCheck size={14} />
                <span>
                  {isDbConnected
                    ? "Database Connected"
                    : "Local Storage (Offline)"}
                </span>
              </div>

              {dbHealth && isDbConnected && (
                <div className="options-db-meta">
                  Engine: {dbHealth.adapter === "cloudflare_d1_sqlite" ? "Cloudflare D1 (SQLite)" : dbHealth.adapter}
                  {dbHealth.storage ? ` · Storage: ${dbHealth.storage === "cloudflare_r2" ? "Cloudflare R2" : dbHealth.storage}` : ""}
                  {" "}· Notebooks: {dbHealth.notebooksCount} · Checkpoints: {snapshots.length}
                </div>
              )}

              {isDbConnected && onCreateSnapshot && (
                <div className="options-checkpoint-bar">
                  <button
                    className="options-checkpoint-btn"
                    onClick={handleCreateSnapshot}
                  >
                    <History size={13} />
                    Create checkpoint
                  </button>
                  {snapshotMessage && (
                    <span className="options-checkpoint-msg">
                      {snapshotMessage}
                    </span>
                  )}
                </div>
              )}

              {snapshots.length > 0 && (
                <div className="options-snapshots-card">
                  <span className="options-snapshots-title">
                    Recent Checkpoints ({snapshots.length})
                  </span>
                  {snapshots.slice(0, 5).map((s) => (
                    <div key={s.id} className="options-snapshot-row">
                      <span className="options-snapshot-info">
                        #{s.id} · {s.reason}
                        <span className="options-snapshot-tag">
                          ({s.cellsCount} {s.cellsCount === 1 ? "cell" : "cells"})
                        </span>
                      </span>
                      <button
                        className="options-snapshot-restore-btn"
                        onClick={() => handleRestore(s.id, s.reason)}
                      >
                        Restore
                      </button>
                    </div>
                  ))}
                </div>
              )}
            </div>

            <button className="button quiet" onClick={handleReset}>
              <RotateCcw size={15} />
              Reset to sample notebook
            </button>
          </div>
        </details>
      </div>
    </div>
  );
};
