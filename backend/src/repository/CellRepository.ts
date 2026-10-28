import type { CellResource, CellRow, JupyterCell } from "../model/Cell.ts";

export class CellRepository {
  constructor(private readonly db: D1Database) {}

  static toDomain(row: CellRow): JupyterCell {
    let resource: CellResource | undefined = undefined;

    if (row.resource_type && row.resource_type !== "none") {
      resource = {
        type: row.resource_type as any,
      };
      if (row.resource_url) resource.url = row.resource_url;
      if (row.resource_name) resource.name = row.resource_name;
      if (row.resource_text_content) resource.textContent = row.resource_text_content;
    }

    let structuredData: any = undefined;
    if (row.structured_data) {
      try {
        structuredData = JSON.parse(row.structured_data);
      } catch {
        // ignore
      }
    }

    return {
      id: row.id,
      executionCount: row.execution_count,
      cellType: (row.cell_type as any) || "markdown",
      source: row.source || "",
      ...(resource ? { resource } : {}),
      ...(structuredData ? { structuredData } : {}),
    };
  }

  async findByNotebookId(notebookId: string): Promise<JupyterCell[]> {
    const result = await this.db
      .prepare("SELECT * FROM cells WHERE notebook_id = ? ORDER BY position ASC")
      .bind(notebookId)
      .all<CellRow>();

    return (result.results || []).map(CellRepository.toDomain);
  }

  buildDeleteNotMatchingStatement(notebookId: string, keepIds: string[]): D1PreparedStatement {
    if (keepIds.length === 0) {
      return this.db.prepare("DELETE FROM cells WHERE notebook_id = ?").bind(notebookId);
    }
    const placeholders = keepIds.map(() => "?").join(",");
    return this.db
      .prepare(`DELETE FROM cells WHERE notebook_id = ? AND id NOT IN (${placeholders})`)
      .bind(notebookId, ...keepIds);
  }

  buildUpsertStatement(
    notebookId: string,
    cell: Partial<JupyterCell>,
    position: number,
    now: string
  ): D1PreparedStatement {
    const cellId = String(cell.id || crypto.randomUUID());
    const cellType = cell.cellType || (cell as any).cell_type || "markdown";
    const execCount = cell.executionCount ?? (cell as any).execution_count ?? null;
    const source = cell.source || "";

    let resourceType = "none";
    let resourceUrl: string | null = null;
    let resourceName: string | null = null;
    let resourceTextContent: string | null = null;

    if (cell.resource && typeof cell.resource === "object") {
      resourceType = cell.resource.type || "none";
      resourceUrl = cell.resource.url || null;
      resourceName = cell.resource.name || null;
      resourceTextContent = cell.resource.textContent || null;
    }

    const structuredDataStr = cell.structuredData ? JSON.stringify(cell.structuredData) : null;

    return this.db
      .prepare(
        `INSERT INTO cells (
          id, notebook_id, position, cell_type, execution_count, 
          source, resource_type, resource_url, resource_name, resource_text_content, 
          structured_data, created_at, updated_at
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ON CONFLICT(id) DO UPDATE SET
          position = excluded.position,
          cell_type = excluded.cell_type,
          execution_count = excluded.execution_count,
          source = excluded.source,
          resource_type = excluded.resource_type,
          resource_url = excluded.resource_url,
          resource_name = excluded.resource_name,
          resource_text_content = excluded.resource_text_content,
          structured_data = excluded.structured_data,
          updated_at = excluded.updated_at`
      )
      .bind(
        cellId,
        notebookId,
        position,
        cellType,
        execCount,
        source,
        resourceType,
        resourceUrl,
        resourceName,
        resourceTextContent,
        structuredDataStr,
        now,
        now
      );
  }

  async executeBatch(statements: D1PreparedStatement[]): Promise<void> {
    if (statements.length > 0) {
      await this.db.batch(statements);
    }
  }

  async deleteAllByNotebookId(notebookId: string): Promise<void> {
    await this.db.prepare("DELETE FROM cells WHERE notebook_id = ?").bind(notebookId).run();
  }

  async count(): Promise<number> {
    const res = await this.db
      .prepare("SELECT COUNT(*) as count FROM cells")
      .first<{ count: number }>();
    return Number(res?.count || 0);
  }
}
