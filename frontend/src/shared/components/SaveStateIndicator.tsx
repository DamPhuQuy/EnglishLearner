import { Check, CircleAlert, Database, CloudOff } from "lucide-react";
import React from "react";
import type { DatabaseStatus, SaveState } from "../../features/notebook/hooks/useNotebook.ts";

interface Props {
  state: SaveState;
  databaseStatus?: DatabaseStatus;
}

export const SaveStateIndicator: React.FC<Props> = ({ state, databaseStatus }) => {
  const isDbConnected = databaseStatus === "connected";
  const isDbSyncing = databaseStatus === "syncing";
  const isDbOffline = databaseStatus === "disconnected";

  return (
    <output
      className={`save-state ${state} ${isDbConnected ? "db-connected" : isDbOffline ? "db-offline" : ""}`}
      title={
        isDbConnected
          ? "Data is safely persisted to backend database and backed up"
          : isDbOffline
            ? "Backend database unreachable — data is saved in local browser storage"
            : "Saving changes"
      }
    >
      {state === "saving" || isDbSyncing ? (
        <span className="spinner-indicator">…</span>
      ) : state === "error" ? (
        <CircleAlert size={14} />
      ) : isDbConnected ? (
        <Database size={13} />
      ) : isDbOffline ? (
        <CloudOff size={13} />
      ) : (
        <Check size={14} />
      )}

      {state === "error"
        ? "Save failed"
        : isDbSyncing || state === "saving"
          ? "Syncing to DB…"
          : isDbConnected
            ? "Saved to DB"
            : isDbOffline
              ? "Saved locally (Offline)"
              : "Saved locally"}
    </output>
  );
};
