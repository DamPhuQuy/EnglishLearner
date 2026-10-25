import { BookOpen, Download, Upload } from "lucide-react";
import React, { useRef } from "react";
import type { SaveState } from "../hooks/useNotebook.ts";
import { SaveStateIndicator } from "../../../shared/components/SaveStateIndicator.tsx";

interface Props {
  title: string;
  saveState: SaveState;
  onTitleChange: (title: string) => void;
  onExport: () => void;
  onImportFile: (file: File) => void;
}

export const NotebookHeader: React.FC<Props> = ({
  title,
  saveState,
  onTitleChange,
  onExport,
  onImportFile,
}) => {
  const fileInputRef = useRef<HTMLInputElement>(null);

  const handleFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];
    e.target.value = "";
    if (file) {
      onImportFile(file);
    }
  };

  return (
    <header className="app-header">
      <div className="header-inner">
        <div className="notebook-identity">
          <BookOpen size={21} className="brand-mark" />
          <span>IELTS Notebook</span>
          <span className="identity-divider" />
          <input
            aria-label="Notebook title"
            className="notebook-title"
            value={title}
            onChange={(e) => onTitleChange(e.target.value)}
          />
        </div>
        <div className="file-actions">
          <SaveStateIndicator state={saveState} />
          <input
            ref={fileInputRef}
            type="file"
            accept=".ilnb,.json,.ipynb"
            onChange={handleFileChange}
            hidden
          />
          <button
            className="button quiet"
            onClick={() => fileInputRef.current?.click()}
          >
            <Upload size={15} />
            Open file
          </button>
          <button className="button outlined" onClick={onExport}>
            <Download size={15} />
            Export notebook
          </button>
        </div>
      </div>
    </header>
  );
};
