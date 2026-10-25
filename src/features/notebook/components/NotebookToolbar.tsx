import { Plus, RotateCcw } from "lucide-react";
import React from "react";
import type { SkillType } from "../types/notebook.ts";
import { SKILL_NAMES } from "../../cell/services/skillTemplates.ts";

interface Props {
  addType: SkillType;
  onAddTypeChange: (skill: SkillType) => void;
  onAddCell: () => void;
  onResetToSample: () => void;
}

export const NotebookToolbar: React.FC<Props> = ({
  addType,
  onAddTypeChange,
  onAddCell,
  onResetToSample,
}) => {
  const handleReset = () => {
    if (
      confirm(
        "Reset current notebook to the default sample? Make sure you have exported your work first.",
      )
    ) {
      onResetToSample();
    }
  };

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
        <span className="toolbar-hint">
          Write on the left. Reference on the right.
        </span>
        <details className="notebook-options">
          <summary className="button quiet">Options</summary>
          <div className="options-panel">
            <p>Shift + Enter: mark visited and advance to the next cell.</p>
            <p>
              Notebook auto-saves in this browser. Export to save a standalone
              file.
            </p>
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
