import { BookOpen, Download, Upload } from "lucide-react";
import React, { useRef } from "react";
import type { DatabaseStatus, SaveState } from "../hooks/useNotebook.ts";
import type { JupyterNotebookDoc } from "../types/notebook.ts";
import { SaveStateIndicator } from "../../../shared/components/SaveStateIndicator.tsx";
import { NotebookTabs } from "./NotebookTabs.tsx";

interface Props {
  notebooks: JupyterNotebookDoc[];
  activeNotebookId: string;
  saveState: SaveState;
  databaseStatus?: DatabaseStatus;
  onSelectTab: (id: string) => void;
  onCloseTab: (id: string) => void;
  onCloseOtherTabs?: (id: string) => void;
  onNewTab: () => void;
  onDuplicateTab?: (id: string) => void;
  onRenameTab?: (id: string, newTitle: string) => void;
  onExportTab?: (notebook: JupyterNotebookDoc) => void;
  onExport: () => void;
  onImportFiles?: (files: File[]) => void;
  fileInputRef?: React.RefObject<HTMLInputElement | null>;
}

export const NotebookHeader: React.FC<Props> = ({
  notebooks,
  activeNotebookId,
  saveState,
  databaseStatus,
  onSelectTab,
  onCloseTab,
  onCloseOtherTabs,
  onNewTab,
  onDuplicateTab,
  onRenameTab,
  onExportTab,
  onExport,
  onImportFiles,
  fileInputRef: externalFileInputRef,
}) => {
  const internalFileInputRef = useRef<HTMLInputElement>(null);
  const inputRef = externalFileInputRef || internalFileInputRef;

  const handleFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const fileList = e.target.files;
    e.target.value = "";
    if (!fileList || fileList.length === 0) return;

    const files = Array.from(fileList);
    if (onImportFiles) {
      onImportFiles(files);
    }
  };

  return (
    <header className="app-header">
      <div className="header-inner">
        <div className="header-left">
          <BookOpen size={20} className="brand-mark" />
          <span className="brand-title">IELTS Notebook</span>
        </div>

        <div className="header-center">
          <NotebookTabs
            notebooks={notebooks}
            activeId={activeNotebookId}
            onSelectTab={onSelectTab}
            onCloseTab={onCloseTab}
            onCloseOtherTabs={onCloseOtherTabs}
            onNewTab={onNewTab}
            onDuplicateTab={onDuplicateTab}
            onRenameTab={onRenameTab}
            onExportTab={onExportTab}
          />
        </div>

        <div className="header-right">
          <SaveStateIndicator state={saveState} databaseStatus={databaseStatus} />
          <input
            ref={inputRef}
            type="file"
            accept=".ilnb,.json,.ipynb"
            multiple
            onChange={handleFileChange}
            hidden
          />
          <button
            className="button quiet"
            title="Open .ilnb or .ipynb files (multiple supported)"
            onClick={() => inputRef.current?.click()}
          >
            <Upload size={14} />
            <span>Open</span>
          </button>
          <button
            className="button outlined"
            title="Export active notebook as .ilnb / .json"
            onClick={onExport}
          >
            <Download size={14} />
            <span>Export</span>
          </button>
        </div>
      </div>
    </header>
  );
};
