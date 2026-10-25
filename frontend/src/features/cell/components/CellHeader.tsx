import {
  ArrowDown,
  ArrowUp,
  BookOpen,
  Check,
  FileText,
  Headphones,
  Mic,
  MoreHorizontal,
  PenLine,
  Plus,
  Trash2,
} from "lucide-react";
import React from "react";
import type { SkillType } from "../../notebook/types/notebook.ts";
import { SKILL_NAMES } from "../services/skillTemplates.ts";

export interface CellHeaderProps {
  cellId: string;
  index: number;
  totalCells: number;
  cellType: SkillType;
  disabled: boolean;
  onUpdateSkill: (skill: SkillType) => void;
  onRun: () => void;
  onInsertTemplate: () => void;
  onMoveUp: () => void;
  onMoveDown: () => void;
  onAddAbove: () => void;
  onAddBelow: () => void;
  onDelete: () => void;
}

const SKILL_ICONS: Record<
  SkillType,
  React.ComponentType<{ size?: number; className?: string }>
> = {
  listening: Headphones,
  reading: BookOpen,
  writing: PenLine,
  speaking: Mic,
  markdown: FileText,
};

export const CellHeader: React.FC<CellHeaderProps> = ({
  index,
  totalCells,
  cellType,
  disabled,
  onUpdateSkill,
  onRun,
  onInsertTemplate,
  onMoveUp,
  onMoveDown,
  onAddAbove,
  onAddBelow,
  onDelete,
}) => {
  const IconComponent = SKILL_ICONS[cellType] ?? FileText;

  const closeMenu = (e: React.MouseEvent) => {
    const details = e.currentTarget.closest("details");
    if (details) details.open = false;
  };

  return (
    <header className="cell-header">
      <div className="cell-type">
        <IconComponent size={16} />
        <select
          aria-label={`Cell ${index + 1} skill`}
          value={cellType}
          disabled={disabled}
          onChange={(e) => onUpdateSkill(e.target.value as SkillType)}
        >
          {Object.entries(SKILL_NAMES).map(([key, label]) => (
            <option key={key} value={key}>
              {label}
            </option>
          ))}
        </select>
      </div>
      <div className="cell-actions">
        <span className="cell-number">Cell {index + 1}</span>
        <button
          className="button quiet next-cell"
          title="Mark visited and advance (Shift + Enter)"
          onClick={(e) => {
            e.stopPropagation();
            onRun();
          }}
        >
          <Check size={15} />
          Next
        </button>
        <details
          className="cell-menu"
          onClick={(e) => e.stopPropagation()}
          onKeyDown={(e) => {
            if (e.key === "Escape") {
              e.currentTarget.open = false;
              e.currentTarget.querySelector("summary")?.focus();
            }
          }}
        >
          <summary
            className="icon-button"
            aria-label={`Cell ${index + 1} actions`}
          >
            <MoreHorizontal size={19} />
          </summary>
          <div className="options-panel" onClick={closeMenu}>
            <button onClick={onInsertTemplate}>
              <FileText size={15} />
              Insert outline template
            </button>
            <button disabled={index === 0} onClick={onMoveUp}>
              <ArrowUp size={15} />
              Move up
            </button>
            <button
              disabled={index === totalCells - 1}
              onClick={onMoveDown}
            >
              <ArrowDown size={15} />
              Move down
            </button>
            <button onClick={onAddAbove}>
              <Plus size={15} />
              Add cell above
            </button>
            <button onClick={onAddBelow}>
              <Plus size={15} />
              Add cell below
            </button>
            <button
              className="danger-action"
              disabled={disabled}
              onClick={onDelete}
            >
              <Trash2 size={15} />
              Delete cell
            </button>
          </div>
        </details>
      </div>
    </header>
  );
};
