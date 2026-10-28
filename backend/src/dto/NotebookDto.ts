import type { JupyterCell } from "../model/Cell.ts";

export interface NotebookSummaryDto {
  id: string;
  title: string;
  cellsCount: number;
  createdAt: string;
  updatedAt: string;
}

export interface SyncNotebookRequestDto {
  title?: string;
  cells?: JupyterCell[];
  reason?: string;
}

export interface CreateNotebookRequestDto {
  id?: string;
  title?: string;
  description?: string;
  cells?: JupyterCell[];
  notebook?: {
    title?: string;
    description?: string;
  };
}

export interface ImportNotebookRequestDto {
  id?: string;
  title?: string;
  cells?: JupyterCell[];
  notebook?: {
    id?: string;
    title?: string;
    cells?: JupyterCell[];
  };
}
