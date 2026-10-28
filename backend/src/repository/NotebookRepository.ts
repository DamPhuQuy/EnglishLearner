import type { NotebookRow } from "../model/Notebook.ts";
import type { NotebookSummaryDto } from "../dto/NotebookDto.ts";

export class NotebookRepository {
  constructor(private readonly db: D1Database) {}

  async findById(id: string): Promise<NotebookRow | null> {
    const row = await this.db
      .prepare("SELECT * FROM notebooks WHERE id = ?")
      .bind(id)
      .first<NotebookRow>();
    return row || null;
  }

  async findLatest(): Promise<NotebookRow | null> {
    const row = await this.db
      .prepare("SELECT * FROM notebooks ORDER BY updated_at DESC LIMIT 1")
      .first<NotebookRow>();
    return row || null;
  }

  async findAllSummaries(): Promise<NotebookSummaryDto[]> {
    const result = await this.db
      .prepare(`
        SELECT 
          n.id, 
          n.title, 
          n.created_at, 
          n.updated_at, 
          COUNT(c.id) as cells_count 
        FROM notebooks n 
        LEFT JOIN cells c ON n.id = c.notebook_id 
        GROUP BY n.id 
        ORDER BY n.updated_at DESC
      `)
      .all<{
        id: string;
        title: string;
        created_at: string;
        updated_at: string;
        cells_count: number;
      }>();

    return (result.results || []).map((r) => ({
      id: r.id,
      title: r.title,
      cellsCount: Number(r.cells_count || 0),
      createdAt: r.created_at,
      updatedAt: r.updated_at,
    }));
  }

  async insert(id: string, title: string, description: string | null = null): Promise<void> {
    const now = new Date().toISOString();
    await this.db
      .prepare(
        "INSERT INTO notebooks (id, title, description, created_at, updated_at) VALUES (?, ?, ?, ?, ?)"
      )
      .bind(id, title, description, now, now)
      .run();
  }

  async updateTitle(id: string, title: string): Promise<void> {
    const now = new Date().toISOString();
    await this.db
      .prepare("UPDATE notebooks SET title = ?, updated_at = ? WHERE id = ?")
      .bind(title, now, id)
      .run();
  }

  async touch(id: string): Promise<void> {
    const now = new Date().toISOString();
    await this.db
      .prepare("UPDATE notebooks SET updated_at = ? WHERE id = ?")
      .bind(now, id)
      .run();
  }

  async delete(id: string): Promise<void> {
    await this.db.prepare("DELETE FROM notebooks WHERE id = ?").bind(id).run();
  }

  async count(): Promise<number> {
    const res = await this.db
      .prepare("SELECT COUNT(*) as count FROM notebooks")
      .first<{ count: number }>();
    return Number(res?.count || 0);
  }
}
