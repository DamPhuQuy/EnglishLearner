export interface DatabaseHealthResponseDto {
  status: "ok" | "error";
  database: "connected" | "disconnected" | "error";
  adapter: string;
  storage: string;
  environment: string;
  notebooksCount: number;
  cellsCount: number;
  snapshotsCount: number;
  timestamp: string;
  message?: string;
}
