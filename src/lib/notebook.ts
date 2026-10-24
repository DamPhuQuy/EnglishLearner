import type { JupyterNotebookDoc } from '../types/notebook';

const skills = new Set(['listening', 'reading', 'writing', 'speaking', 'markdown']);
const resources = new Set(['audio', 'pdf', 'image', 'text', 'voice_recorder', 'none']);

export function isNotebook(value: unknown): value is JupyterNotebookDoc {
  if (!value || typeof value !== 'object') return false;
  const doc = value as JupyterNotebookDoc;
  if (typeof doc.id !== 'string' || typeof doc.title !== 'string' || !Array.isArray(doc.cells) || !doc.cells.length) return false;
  const ids = new Set<string>();
  return doc.cells.every(cell => {
    if (!cell || typeof cell.id !== 'string' || ids.has(cell.id) || !skills.has(cell.cellType) || typeof cell.source !== 'string') return false;
    ids.add(cell.id);
    if (cell.executionCount !== null && (!Number.isInteger(cell.executionCount) || cell.executionCount < 0)) return false;
    const r = cell.resource;
    if (!r) return true;
    return resources.has(r.type) && [r.url, r.name, r.textContent].every(v => v === undefined || typeof v === 'string') &&
      (!r.url || /^(https?:\/\/|blob:|data:(audio\/|image\/|application\/pdf[;,]|text\/plain[;,]))/i.test(r.url));
  });
}

export function readFileData(file: File): Promise<string> {
  return new Promise((resolve, reject) => {
    const reader = new FileReader();
    reader.onload = () => resolve(String(reader.result));
    reader.onerror = () => reject(new Error('Không đọc được tệp. Hãy thử chọn lại.'));
    reader.readAsDataURL(file);
  });
}
