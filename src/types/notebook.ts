export type SkillType = 'listening' | 'reading' | 'writing' | 'speaking' | 'markdown';

export type ResourceType = 'audio' | 'pdf' | 'image' | 'text' | 'voice_recorder' | 'none';

export interface CellResource {
  type: ResourceType;
  url?: string;
  name?: string;
  textContent?: string;
}

export interface JupyterCell {
  id: string;
  executionCount: number | null;
  cellType: SkillType;
  source: string; // Left Grid: User's Markdown workspace / answer sheet
  resource?: CellResource; // Right Grid: Media, PDF, Audio, Document viewer
}

export interface JupyterNotebookDoc {
  id: string;
  title: string;
  cells: JupyterCell[];
}
