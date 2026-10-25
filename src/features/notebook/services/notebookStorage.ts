import type { JupyterNotebookDoc } from "../types/notebook.ts";
import { isNotebook } from "./notebookValidator.ts";

const DEFAULT_STORAGE_KEY = "ielts_jupyter_notebook_v2";

export class LocalStorageNotebookStorage {
  private readonly storageKey: string;

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
    localStorage.setItem(this.storageKey, JSON.stringify(notebook));
  }
}

export const defaultNotebookStorage = new LocalStorageNotebookStorage();
