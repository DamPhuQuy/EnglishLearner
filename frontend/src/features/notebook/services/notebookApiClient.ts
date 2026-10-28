import type { JupyterNotebookDoc } from "../types/notebook.ts";
import { isNotebook } from "./notebookValidator.ts";

export interface DatabaseHealth {
  status: "ok" | "error";
  database: "connected" | "disconnected" | "error";
  adapter?: string;
  storage?: string;
  environment?: string;
  notebooksCount?: number;
  cellsCount?: number;
  snapshotsCount?: number;
  timestamp?: string;
  message?: string;
}

export interface SnapshotSummary {
  id: number;
  notebookId: string;
  title: string;
  cellsCount: number;
  reason: string;
  createdAt: string;
}

export interface NotebookSummary {
  id: string;
  title: string;
  cellsCount: number;
  createdAt: string;
  updatedAt: string;
}

const getApiBaseUrl = (): string => {
  if (typeof window !== "undefined") {
    // If running in browser with Vite proxy or configured ENV
    const envUrl = (import.meta as { env?: Record<string, string> }).env?.VITE_API_URL;
    if (envUrl) return envUrl.replace(/\/$/, "");

    // Default to relative /api/v1 (routed via Vite proxy or reverse proxy)
    // Or fallback to direct port 3000 if needed
    return "/api/v1";
  }
  return "http://localhost:3000/api/v1";
};

export class NotebookApiClient {
  private baseUrl: string;

  constructor(baseUrl: string = getApiBaseUrl()) {
    this.baseUrl = baseUrl;
  }

  setBaseUrl(url: string) {
    this.baseUrl = url.replace(/\/$/, "");
  }

  async checkHealth(): Promise<DatabaseHealth> {
    try {
      const response = await fetch(`${this.baseUrl}/health`, {
        method: "GET",
        headers: { Accept: "application/json" },
      });
      if (!response.ok) {
        return { status: "error", database: "disconnected", message: `HTTP ${response.status}` };
      }
      return (await response.json()) as DatabaseHealth;
    } catch (err) {
      return {
        status: "error",
        database: "disconnected",
        message: err instanceof Error ? err.message : "Network error",
      };
    }
  }

  async fetchCurrentNotebook(): Promise<JupyterNotebookDoc | null> {
    try {
      const response = await fetch(`${this.baseUrl}/notebooks/current`, {
        method: "GET",
        headers: { Accept: "application/json" },
      });
      if (!response.ok) return null;
      const data = await response.json();
      if (isNotebook(data)) {
        return data;
      }
      return null;
    } catch {
      return null;
    }
  }

  async fetchNotebook(id: string): Promise<JupyterNotebookDoc | null> {
    try {
      const response = await fetch(`${this.baseUrl}/notebooks/${encodeURIComponent(id)}`, {
        method: "GET",
        headers: { Accept: "application/json" },
      });
      if (!response.ok) return null;
      const data = await response.json();
      if (isNotebook(data)) {
        return data;
      }
      return null;
    } catch {
      return null;
    }
  }

  async syncNotebook(
    doc: JupyterNotebookDoc,
    reason: string = "auto_sync",
  ): Promise<{ success: boolean; data?: JupyterNotebookDoc; error?: string }> {
    try {
      const response = await fetch(`${this.baseUrl}/notebooks/${encodeURIComponent(doc.id)}/sync`, {
        method: "PUT",
        headers: {
          "Content-Type": "application/json",
          Accept: "application/json",
        },
        body: JSON.stringify({
          title: doc.title,
          cells: doc.cells,
          reason,
        }),
      });

      if (!response.ok) {
        const errorJson = await response.json().catch(() => ({}));
        return {
          success: false,
          error: errorJson.error || `HTTP ${response.status}: Failed to sync with database`,
        };
      }

      const updated = await response.json();
      return { success: true, data: updated };
    } catch (err) {
      return {
        success: false,
        error: err instanceof Error ? err.message : "Sync network error",
      };
    }
  }

  async listNotebooks(): Promise<NotebookSummary[]> {
    try {
      const response = await fetch(`${this.baseUrl}/notebooks`, {
        headers: { Accept: "application/json" },
      });
      if (!response.ok) return [];
      const json = await response.json();
      return json.notebooks || [];
    } catch {
      return [];
    }
  }

  async listSnapshots(notebookId: string): Promise<SnapshotSummary[]> {
    try {
      const response = await fetch(`${this.baseUrl}/notebooks/${encodeURIComponent(notebookId)}/snapshots`, {
        headers: { Accept: "application/json" },
      });
      if (!response.ok) return [];
      const json = await response.json();
      return json.snapshots || [];
    } catch {
      return [];
    }
  }

  async restoreSnapshot(
    notebookId: string,
    snapshotId: number,
  ): Promise<{ success: boolean; notebook?: JupyterNotebookDoc; error?: string }> {
    try {
      const response = await fetch(
        `${this.baseUrl}/notebooks/${encodeURIComponent(notebookId)}/snapshots/${snapshotId}/restore`,
        {
          method: "POST",
          headers: { Accept: "application/json" },
        },
      );
      if (!response.ok) {
        return { success: false, error: `Restore failed: HTTP ${response.status}` };
      }
      const json = await response.json();
      if (isNotebook(json.notebook)) {
        return { success: true, notebook: json.notebook };
      }
      return { success: false, error: "Invalid notebook structure returned" };
    } catch (err) {
      return {
        success: false,
        error: err instanceof Error ? err.message : "Restore network error",
      };
    }
  }

  async uploadFile(
    file: File | Blob,
    customFilename?: string
  ): Promise<{
    url: string;
    key: string;
    name: string;
    type: string;
    size: number;
  }> {
    const formData = new FormData();
    if (file instanceof File) {
      formData.append("file", file, file.name);
    } else {
      formData.append("file", file, customFilename || "recording.webm");
    }

    const response = await fetch(`${this.baseUrl}/upload`, {
      method: "POST",
      body: formData,
    });

    if (!response.ok) {
      const errJson = await response.json().catch(() => null);
      throw new Error(errJson?.error || `Upload failed: HTTP ${response.status}`);
    }

    return await response.json();
  }
}

export const defaultNotebookApiClient = new NotebookApiClient();
