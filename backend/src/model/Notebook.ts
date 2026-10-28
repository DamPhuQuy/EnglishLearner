import type { JupyterCell } from "./Cell.ts";

export interface NotebookRow {
  id: string;
  title: string;
  description: string | null;
  created_at: string;
  updated_at: string;
}

export interface NotebookEntity {
  id: string;
  title: string;
  description?: string | null;
  cells: JupyterCell[];
  createdAt: string;
  updatedAt: string;
}
