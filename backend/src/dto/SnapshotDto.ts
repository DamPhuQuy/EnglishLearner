import type { NotebookEntity } from "../model/Notebook.ts";

export interface SnapshotSummaryDto {
  id: number;
  notebookId: string;
  title: string;
  cellsCount: number;
  reason: string;
  createdAt: string;
}

export interface SnapshotDetailDto {
  snapshot: SnapshotSummaryDto;
  doc: NotebookEntity;
}
