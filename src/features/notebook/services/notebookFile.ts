import type {
  CellResource,
  JupyterNotebookDoc,
} from "../types/notebook.ts";
import { isNotebook } from "./notebookValidator.ts";

const MAX_NOTEBOOK_FILE_SIZE = 20 * 1024 * 1024; // 20 MB
export const MAX_ATTACHMENT_FILE_SIZE = 2 * 1024 * 1024; // 2 MB

export class BrowserNotebookFileAdapter {
  exportNotebook(notebook: JupyterNotebookDoc): void {
    const json = JSON.stringify(notebook, null, 2);
    const blob = new Blob([json], { type: "application/json" });
    const url = URL.createObjectURL(blob);
    const a = document.createElement("a");
    const rawName = notebook.title.replace(/\.(ipynb|json|ilnb)$/i, "");
    a.href = url;
    a.download = `${rawName || "IELTS Notebook"}.ilnb`;
    a.click();
    window.setTimeout(() => URL.revokeObjectURL(url), 1000);
  }

  async parseNotebookFile(file: File): Promise<JupyterNotebookDoc> {
    if (file.size > MAX_NOTEBOOK_FILE_SIZE) {
      throw new Error("File exceeds 20 MB. Please select a smaller notebook file.");
    }
    const text = await file.text();
    let parsed: unknown;
    try {
      parsed = JSON.parse(text);
    } catch {
      throw new Error(
        "File could not be parsed as JSON. Please select a notebook exported from this application.",
      );
    }
    if (!isNotebook(parsed)) {
      throw new Error(
        "File is not a valid IELTS Notebook format. Please select an .ilnb file exported from this application.",
      );
    }
    return parsed;
  }

  readFileData(file: File): Promise<string> {
    return new Promise((resolve, reject) => {
      const reader = new FileReader();
      reader.onload = () => resolve(String(reader.result));
      reader.onerror = () =>
        reject(new Error("Could not read file. Please try selecting it again."));
      reader.readAsDataURL(file);
    });
  }

  async readFileAsResource(file: File): Promise<CellResource> {
    if (file.size > MAX_ATTACHMENT_FILE_SIZE) {
      throw new Error(
        "File exceeds 2 MB. Please use smaller files to save in browser storage; for long audio, use a direct URL.",
      );
    }
    const name = file.name;
    const lower = name.toLowerCase();
    let type: CellResource["type"];

    if (
      file.type.startsWith("audio/") ||
      /\.(mp3|wav|ogg|m4a|webm)$/.test(lower)
    ) {
      type = "audio";
    } else if (file.type === "application/pdf" || lower.endsWith(".pdf")) {
      type = "pdf";
    } else if (
      /^image\/(png|jpeg|webp|gif)$/.test(file.type) ||
      /\.(png|jpe?g|webp|gif)$/.test(lower)
    ) {
      type = "image";
    } else if (/\.(txt|md)$/.test(lower)) {
      type = "text";
    } else {
      throw new Error(
        "Please select a PDF, image, audio, TXT, or Markdown file. For DOCX, convert to PDF before attaching.",
      );
    }

    if (type === "text") {
      const textContent = await file.text();
      return { type, name, textContent };
    }

    const url = await this.readFileData(file);
    return { type, name, url };
  }
}

export const defaultNotebookFileAdapter = new BrowserNotebookFileAdapter();
