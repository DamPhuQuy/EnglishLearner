import type { IeltsExerciseData } from "../../cell/types/ieltsSchema.ts";

export type SkillType =
  | "listening"
  | "reading"
  | "writing"
  | "speaking"
  | "markdown";

export type ResourceType =
  | "audio"
  | "pdf"
  | "image"
  | "text"
  | "voice_recorder"
  | "none";

export interface CellResource {
  type: ResourceType;
  url?: string;
  name?: string;
  textContent?: string;
}

export interface JupyterCell {
  id: string;
  executionCount: number | null;
  cellType: SkillType;
  source: string;
  resource?: CellResource;
  structuredData?: IeltsExerciseData;
}

export interface JupyterNotebookDoc {
  id: string;
  title: string;
  cells: JupyterCell[];
}

export function createCell(
  cellType: SkillType = "markdown",
  source = "",
  resource?: CellResource,
  structuredData?: IeltsExerciseData,
): JupyterCell {
  return {
    id: crypto.randomUUID(),
    executionCount: null,
    cellType,
    source,
    resource,
    structuredData,
  };
}

export function addCellAt(
  cells: readonly JupyterCell[],
  index: number,
  newCell: JupyterCell,
): JupyterCell[] {
  const result = [...cells];
  result.splice(index + 1, 0, newCell);
  return result;
}

export function removeCellById(
  cells: readonly JupyterCell[],
  id: string,
): { cells: JupyterCell[]; removed: JupyterCell | null; index: number } {
  const index = cells.findIndex((c) => c.id === id);
  if (index === -1) {
    return { cells: [...cells], removed: null, index: -1 };
  }
  const removed = cells[index];
  const nextCells = cells.filter((c) => c.id !== id);
  return { cells: nextCells, removed, index };
}

export function moveCell(
  cells: readonly JupyterCell[],
  index: number,
  delta: number,
): JupyterCell[] {
  const targetIndex = index + delta;
  if (index < 0 || targetIndex < 0 || targetIndex >= cells.length) {
    return [...cells];
  }
  const next = [...cells];
  const [moved] = next.splice(index, 1);
  next.splice(targetIndex, 0, moved);
  return next;
}

export function patchCell(
  cells: readonly JupyterCell[],
  id: string,
  change: Partial<JupyterCell>,
): JupyterCell[] {
  return cells.map((c) => (c.id === id ? { ...c, ...change } : c));
}

export function executeCellInList(
  cells: readonly JupyterCell[],
  id: string,
): { cells: JupyterCell[]; nextActiveId: string } {
  const index = cells.findIndex((c) => c.id === id);
  if (index === -1) {
    return { cells: [...cells], nextActiveId: id };
  }
  const maxExec = Math.max(0, ...cells.map((c) => c.executionCount ?? 0));
  const updatedCells = patchCell(cells, id, {
    executionCount: maxExec + 1,
  });
  const nextActiveId = cells[index + 1]?.id ?? id;
  return { cells: updatedCells, nextActiveId };
}
