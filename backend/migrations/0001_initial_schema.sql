-- D1 SQLite Schema for IELTS Notebook
CREATE TABLE IF NOT EXISTS notebooks (
  id TEXT PRIMARY KEY,
  title TEXT NOT NULL DEFAULT 'IELTS Practice Notebook',
  description TEXT,
  created_at TEXT NOT NULL,
  updated_at TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS cells (
  id TEXT PRIMARY KEY,
  notebook_id TEXT NOT NULL REFERENCES notebooks(id) ON DELETE CASCADE,
  position INTEGER NOT NULL DEFAULT 0,
  cell_type TEXT NOT NULL DEFAULT 'markdown',
  execution_count INTEGER,
  source TEXT DEFAULT '',
  resource_type TEXT DEFAULT 'none',
  resource_url TEXT,
  resource_name TEXT,
  resource_text_content TEXT,
  structured_data TEXT,
  created_at TEXT NOT NULL,
  updated_at TEXT NOT NULL
);

CREATE INDEX IF NOT EXISTS idx_cells_notebook_position ON cells(notebook_id, position);
CREATE INDEX IF NOT EXISTS idx_cells_type ON cells(cell_type);

CREATE TABLE IF NOT EXISTS notebook_snapshots (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  notebook_id TEXT NOT NULL REFERENCES notebooks(id) ON DELETE CASCADE,
  title TEXT NOT NULL,
  snapshot_data TEXT NOT NULL,
  cells_count INTEGER NOT NULL DEFAULT 0,
  reason TEXT DEFAULT 'auto_sync',
  created_at TEXT NOT NULL,
  updated_at TEXT NOT NULL
);

CREATE INDEX IF NOT EXISTS idx_snapshots_notebook_created ON notebook_snapshots(notebook_id, created_at);
