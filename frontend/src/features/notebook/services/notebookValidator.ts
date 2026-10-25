import type {
  JupyterNotebookDoc,
  ResourceType,
  SkillType,
} from "../types/notebook.ts";

export const VALID_SKILL_TYPES = new Set<SkillType>([
  "listening",
  "reading",
  "writing",
  "speaking",
  "markdown",
]);

export const VALID_RESOURCE_TYPES = new Set<ResourceType>([
  "audio",
  "pdf",
  "image",
  "text",
  "voice_recorder",
  "none",
]);

const SAFE_RESOURCE_URL_PATTERN =
  /^(https?:\/\/|blob:|data:(audio\/|image\/|application\/pdf[;,]|text\/plain[;,]))/i;

export function isNotebook(value: unknown): value is JupyterNotebookDoc {
  if (!value || typeof value !== "object") return false;
  const doc = value as JupyterNotebookDoc;
  if (
    typeof doc.id !== "string" ||
    typeof doc.title !== "string" ||
    !Array.isArray(doc.cells)
  ) {
    return false;
  }
  const seenIds = new Set<string>();
  return doc.cells.every((cell) => {
    if (
      !cell ||
      typeof cell.id !== "string" ||
      seenIds.has(cell.id) ||
      !VALID_SKILL_TYPES.has(cell.cellType) ||
      typeof cell.source !== "string"
    ) {
      return false;
    }
    seenIds.add(cell.id);
    if (
      cell.executionCount !== null &&
      (!Number.isInteger(cell.executionCount) || cell.executionCount < 0)
    ) {
      return false;
    }
    const r = cell.resource;
    if (!r) return true;
    return (
      VALID_RESOURCE_TYPES.has(r.type) &&
      [r.url, r.name, r.textContent].every(
        (v) => v === undefined || typeof v === "string",
      ) &&
      (!r.url || SAFE_RESOURCE_URL_PATTERN.test(r.url))
    );
  });
}
