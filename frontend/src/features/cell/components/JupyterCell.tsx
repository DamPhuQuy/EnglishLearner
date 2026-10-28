import React from "react";
import type {
  CellResource,
  JupyterCell as CellType,
  SkillType,
} from "../../notebook/types/notebook.ts";
import type { IeltsExerciseData } from "../types/ieltsSchema.ts";
import { SKILL_NAMES } from "../services/skillTemplates.ts";
import { CellEditorPane } from "./CellEditorPane.tsx";
import { CellGutter } from "./CellGutter.tsx";
import { CellHeader } from "./CellHeader.tsx";
import { CellResourcePane } from "./CellResourcePane.tsx";

export interface JupyterCellProps {
  cell: CellType;
  index: number;
  totalCells: number;
  isActive: boolean;
  onSelect: () => void;
  onUpdateSource: (id: string, source: string) => void;
  onUpdateSkill: (id: string, skill: SkillType) => void;
  onUpdateResource: (id: string, resource: CellResource | undefined) => void;
  onUpdateStructuredData?: (id: string, data: IeltsExerciseData | undefined) => void;
  onRun: (id: string) => void;
  onDelete: (id: string) => void;
  onMoveUp: (index: number) => void;
  onMoveDown: (index: number) => void;
  onAddAbove: (index: number) => void;
  onAddBelow: (index: number) => void;
  onInsertTemplate: () => void;
}

export const JupyterCell: React.FC<JupyterCellProps> = ({
  cell,
  index,
  totalCells,
  isActive,
  onSelect,
  onUpdateSource,
  onUpdateSkill,
  onUpdateResource,
  onUpdateStructuredData,
  onRun,
  onDelete,
  onMoveUp,
  onMoveDown,
  onAddAbove,
  onAddBelow,
  onInsertTemplate,
}) => {
  const skillLabel = SKILL_NAMES[cell.cellType] ?? cell.cellType;

  return (
    <section
      id={`cell-${cell.id}`}
      className={`notebook-cell ${isActive ? "active" : ""}`}
      aria-label={`Cell ${index + 1}: ${skillLabel}`}
      onFocusCapture={onSelect}
      onClick={onSelect}
    >
      <CellGutter executionCount={cell.executionCount} />
      <div className="cell-content">
        <CellHeader
          cellId={cell.id}
          index={index}
          totalCells={totalCells}
          cellType={cell.cellType}
          disabled={false}
          onUpdateSkill={(skill) => onUpdateSkill(cell.id, skill)}
          onRun={() => onRun(cell.id)}
          onInsertTemplate={onInsertTemplate}
          onMoveUp={() => onMoveUp(index)}
          onMoveDown={() => onMoveDown(index)}
          onAddAbove={() => onAddAbove(index)}
          onAddBelow={() => onAddBelow(index)}
          onDelete={() => onDelete(cell.id)}
        />
        <div className="cell-panes">
          <CellEditorPane
            cellId={cell.id}
            source={cell.source}
            cellType={cell.cellType}
            structuredData={cell.structuredData}
            onUpdateSource={(src) => onUpdateSource(cell.id, src)}
            onUpdateStructuredData={(data) => onUpdateStructuredData?.(cell.id, data)}
            onUpdateResource={(res) => onUpdateResource(cell.id, res)}
            onRun={() => onRun(cell.id)}
          />
          <CellResourcePane
            cellId={cell.id}
            cellType={cell.cellType}
            resource={cell.resource}
            onUpdateResource={(res) => onUpdateResource(cell.id, res)}
          />
        </div>
      </div>
    </section>
  );
};
