import type { JupyterNotebookDoc } from "../types/notebook.ts";
import { isNotebook } from "./notebookValidator.ts";
import { defaultNotebookApiClient, NotebookApiClient } from "./notebookApiClient.ts";

const DEFAULT_STORAGE_KEY = "ielts_jupyter_notebook_v2";
const MULTI_STORAGE_KEY = "ielts_multi_notebooks_v1";
const ACTIVE_TAB_KEY = "ielts_active_notebook_tab_v1";

export class LocalStorageNotebookStorage {
  protected readonly storageKey: string;

  constructor(storageKey: string = DEFAULT_STORAGE_KEY) {
    this.storageKey = storageKey;
  }

  load(): JupyterNotebookDoc | null {
    try {
      const saved = localStorage.getItem(this.storageKey);
      if (!saved) return null;
      const parsed: unknown = JSON.parse(saved);
      if (isNotebook(parsed)) {
        return parsed;
      }
      return null;
    } catch {
      return null;
    }
  }

  save(notebook: JupyterNotebookDoc): void {
    try {
      localStorage.setItem(this.storageKey, JSON.stringify(notebook));
    } catch {
      // quota handling
    }
  }

  loadAll(): { notebooks: JupyterNotebookDoc[]; activeId: string } | null {
    try {
      const saved = localStorage.getItem(MULTI_STORAGE_KEY);
      const activeId = localStorage.getItem(ACTIVE_TAB_KEY) || "";

      if (saved) {
        const parsed: unknown = JSON.parse(saved);
        if (Array.isArray(parsed)) {
          const valid = parsed.filter(isNotebook);
          if (valid.length > 0) {
            const resolvedActiveId =
              activeId && valid.some((n) => n.id === activeId)
                ? activeId
                : valid[0].id;
            return { notebooks: valid, activeId: resolvedActiveId };
          }
        }
      }

      // Fallback to legacy single notebook storage
      const single = this.load();
      if (single) {
        return { notebooks: [single], activeId: single.id };
      }

      return null;
    } catch {
      return null;
    }
  }

  saveAll(notebooks: JupyterNotebookDoc[], activeId: string): void {
    try {
      localStorage.setItem(MULTI_STORAGE_KEY, JSON.stringify(notebooks));
      localStorage.setItem(ACTIVE_TAB_KEY, activeId);

      // Keep legacy key in sync with active notebook for backward compatibility
      const active = notebooks.find((n) => n.id === activeId) || notebooks[0];
      if (active) {
        this.save(active);
      }
    } catch {
      // Storage quota or private browsing mode
    }
  }
}

export class HybridNotebookStorage extends LocalStorageNotebookStorage {
  private apiClient: NotebookApiClient;

  constructor(
    storageKey: string = DEFAULT_STORAGE_KEY,
    apiClient: NotebookApiClient = defaultNotebookApiClient,
  ) {
    super(storageKey);
    this.apiClient = apiClient;
  }

  get client(): NotebookApiClient {
    return this.apiClient;
  }

  async syncToDatabase(notebook: JupyterNotebookDoc, reason: string = "auto_sync") {
    this.save(notebook);
    return await this.apiClient.syncNotebook(notebook, reason);
  }

  async loadFromDatabase(): Promise<JupyterNotebookDoc | null> {
    const remote = await this.apiClient.fetchCurrentNotebook();
    if (remote) {
      this.save(remote);
      return remote;
    }
    return this.load();
  }
}

export const defaultNotebookStorage = new LocalStorageNotebookStorage();
export const defaultHybridStorage = new HybridNotebookStorage();
