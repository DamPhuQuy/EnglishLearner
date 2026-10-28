export type SkillType =
  | "listening"
  | "reading"
  | "writing"
  | "speaking"
  | "markdown";

export type ResourceType =
  | "audio"
  | "pdf"
  | "image"
  | "text"
  | "voice_recorder"
  | "none";

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
  source: string;
  resource?: CellResource;
  structuredData?: any;
}

export interface CellRow {
  id: string;
  notebook_id: string;
  position: number;
  cell_type: string;
  execution_count: number | null;
  source: string | null;
  resource_type: string | null;
  resource_url: string | null;
  resource_name: string | null;
  resource_text_content: string | null;
  structured_data: string | null;
  created_at: string;
  updated_at: string;
}
