import { CircleAlert, Plus } from "lucide-react";
import React, { useRef, useState } from "react";
import { JupyterCell, SKILL_NAMES } from "./features/cell/index.ts";
import {
  NotebookHeader,
  NotebookToolbar,
  useNotebook,
  type SkillType,
} from "./features/notebook/index.ts";
import { UndoNotice } from "./shared/index.ts";

export const App: React.FC = () => {
  const [addType, setAddType] = useState<SkillType>("markdown");
  const fileInputRef = useRef<HTMLInputElement>(null);

  const {
    doc,
    notebooks,
    activeNotebookId,
    activeId,
    activeIndex,
    saveState,
    databaseStatus,
    dbHealth,
    snapshots,
    loadError,
    deleted,
    switchTab,
    createTab,
    closeTab,
    renameTab,
    duplicateTab,
    closeOtherTabs,
    importFiles,
    setActiveId,
    setLoadError,
    add,
    run,
    remove,
    move,
    undoDelete,
    dismissUndo,
    resetToSample,
    exportDoc,
    insertTemplate,
    restoreSnapshot,
    createSnapshotNow,
    updateSource,
    updateSkill,
    updateResource,
  } = useNotebook();

  return (
    <div className="app-shell">
      <a className="skip-link" href="#notebook">
        Skip to notebook content
      </a>

      <NotebookHeader
        notebooks={notebooks}
        activeNotebookId={activeNotebookId}
        saveState={saveState}
        databaseStatus={databaseStatus}
        onSelectTab={switchTab}
        onCloseTab={closeTab}
        onCloseOtherTabs={closeOtherTabs}
        onNewTab={() => createTab()}
        onDuplicateTab={duplicateTab}
        onRenameTab={renameTab}
        onExportTab={(nb) => exportDoc(nb)}
        onExport={exportDoc}
        onImportFiles={importFiles}
        fileInputRef={fileInputRef}
      />

      <NotebookToolbar
        addType={addType}
        databaseStatus={databaseStatus}
        dbHealth={dbHealth}
        snapshots={snapshots}
        onAddTypeChange={setAddType}
        onAddCell={() => add(activeIndex, addType)}
        onResetToSample={resetToSample}
        onCreateSnapshot={createSnapshotNow}
        onRestoreSnapshot={restoreSnapshot}
      />

      <main id="notebook" className="notebook" tabIndex={-1}>
        {(saveState === "error" || loadError) && (
          <div className="notice error" role="alert">
            <CircleAlert size={18} />
            <span>
              {loadError ||
                "Browser storage is full or restricted. Your workspace remains open; export your notebook to save your work."}
            </span>
            {loadError && (
              <button className="button quiet" onClick={() => setLoadError("")}>
                Dismiss
              </button>
            )}
          </div>
        )}

        <div className="document-heading">
          <div>
            <h1>{doc.title.replace(/\.(ipynb|json|ilnb)$/i, "") || "Practice Workspace"}</h1>
            <p>Draft your work while keeping references alongside.</p>
          </div>
          <span>
            {doc.cells.length} {doc.cells.length === 1 ? "cell" : "cells"}
            {doc.cells.length > 0 && (
              <> · {activeIndex >= 0 ? `Selected ${activeIndex + 1}` : "Select a cell"}</>
            )}
          </span>
        </div>

        {doc.cells.length === 0 ? (
          <div className="empty-workspace">
            <p>This notebook is currently empty. Add a cell below to begin your practice.</p>
          </div>
        ) : (
          doc.cells.map((cell, index) => (
            <JupyterCell
              key={cell.id}
              cell={cell}
              index={index}
              totalCells={doc.cells.length}
              isActive={cell.id === activeId}
              onSelect={() => setActiveId(cell.id)}
              onUpdateSource={updateSource}
              onUpdateSkill={updateSkill}
              onUpdateResource={updateResource}
              onRun={run}
              onDelete={remove}
              onMoveUp={(idx) => move(idx, -1)}
              onMoveDown={(idx) => move(idx, 1)}
              onAddAbove={(idx) => add(idx - 1, cell.cellType)}
              onAddBelow={(idx) => add(idx, cell.cellType)}
              onInsertTemplate={() => insertTemplate(cell.id)}
            />
          ))
        )}

        <button
          className="append-cell"
          onClick={() => add(doc.cells.length - 1, addType)}
        >
          <Plus size={17} />
          Add {SKILL_NAMES[addType].toLowerCase()}
          <span>{doc.cells.length === 0 ? "to begin notebook" : "to end of notebook"}</span>
        </button>

        <footer className="notebook-footer">
          <span>
            {databaseStatus === "connected"
              ? "Content safely backed up in Database"
              : "Content saved in this browser"}
          </span>
          <span>Shift + Enter · Next cell</span>
        </footer>
      </main>

      {deleted && <UndoNotice onUndo={undoDelete} onDismiss={dismissUndo} />}
    </div>
  );
};

export default App;
