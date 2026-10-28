import type { JupyterNotebookDoc } from "../types/notebook.ts";
import { MINI_IELTS_PRESETS } from "../../cell/services/skillTemplates.ts";

export const sampleNotebook: JupyterNotebookDoc = {
  id: "ielts-notebook-01",
  title: "Mini_IELTS_Practice_Workbench.ipynb",
  cells: MINI_IELTS_PRESETS.map((preset) => ({
    id: `cell-${preset.id}`,
    executionCount: null,
    cellType: preset.skill,
    source: preset.source,
    resource: preset.resource,
    structuredData: preset.structuredData,
  })),
};
