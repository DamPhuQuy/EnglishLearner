export interface SnapshotRow {
  id: number;
  notebook_id: string;
  title: string;
  snapshot_data: string;
  cells_count: number;
  reason: string;
  created_at: string;
  updated_at: string;
}

export interface SnapshotEntity {
  id: number;
  notebookId: string;
  title: string;
  snapshotData: string;
  cellsCount: number;
  reason: string;
  createdAt: string;
  updatedAt: string;
}
