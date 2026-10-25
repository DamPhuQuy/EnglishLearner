import { CircleAlert, Plus } from "lucide-react";
import React, { useState } from "react";
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

  const {
    doc,
    activeId,
    activeIndex,
    saveState,
    loadError,
    deleted,
    setActiveId,
    setLoadError,
    setTitle,
    add,
    run,
    remove,
    move,
    undoDelete,
    dismissUndo,
    resetToSample,
    exportDoc,
    importDoc,
    insertTemplate,
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
        title={doc.title}
        saveState={saveState}
        onTitleChange={setTitle}
        onExport={exportDoc}
        onImportFile={importDoc}
      />

      <NotebookToolbar
        addType={addType}
        onAddTypeChange={setAddType}
        onAddCell={() => add(activeIndex, addType)}
        onResetToSample={resetToSample}
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
            <h1>Practice Workspace</h1>
            <p>Draft your work while keeping references alongside.</p>
          </div>
          <span>
            {doc.cells.length} {doc.cells.length === 1 ? "cell" : "cells"} ·{" "}
            {activeIndex >= 0
              ? `Selected ${activeIndex + 1}`
              : "Select a cell"}
          </span>
        </div>

        {doc.cells.map((cell, index) => (
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
        ))}

        <button
          className="append-cell"
          onClick={() => add(doc.cells.length - 1, addType)}
        >
          <Plus size={17} />
          Add {SKILL_NAMES[addType].toLowerCase()}
          <span>to end of notebook</span>
        </button>

        <footer className="notebook-footer">
          <span>Content saved in this browser</span>
          <span>Shift + Enter · Next cell</span>
        </footer>
      </main>

      {deleted && <UndoNotice onUndo={undoDelete} onDismiss={dismissUndo} />}
    </div>
  );
};

export default App;
