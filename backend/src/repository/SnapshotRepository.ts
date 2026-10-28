import type { SnapshotRow } from "../model/Snapshot.ts";
import type { SnapshotSummaryDto } from "../dto/SnapshotDto.ts";

export class SnapshotRepository {
  constructor(private readonly db: D1Database) {}

  static toSummary(row: SnapshotRow): SnapshotSummaryDto {
    return {
      id: row.id,
      notebookId: row.notebook_id,
      title: row.title,
      cellsCount: Number(row.cells_count || 0),
      reason: row.reason,
      createdAt: row.created_at,
    };
  }

  async findByNotebookId(notebookId: string): Promise<SnapshotSummaryDto[]> {
    const result = await this.db
      .prepare(
        `SELECT id, notebook_id, title, cells_count, reason, created_at 
         FROM notebook_snapshots 
         WHERE notebook_id = ? 
         ORDER BY id DESC`
      )
      .bind(notebookId)
      .all<SnapshotRow>();

    return (result.results || []).map(SnapshotRepository.toSummary);
  }

  async findByIdAndNotebookId(id: number, notebookId: string): Promise<SnapshotRow | null> {
    const row = await this.db
      .prepare("SELECT * FROM notebook_snapshots WHERE id = ? AND notebook_id = ?")
      .bind(id, notebookId)
      .first<SnapshotRow>();
    return row || null;
  }

  async findLatestByNotebookId(notebookId: string): Promise<SnapshotRow | null> {
    const row = await this.db
      .prepare(
        "SELECT * FROM notebook_snapshots WHERE notebook_id = ? ORDER BY id DESC LIMIT 1"
      )
      .bind(notebookId)
      .first<SnapshotRow>();
    return row || null;
  }

  async insert(
    notebookId: string,
    title: string,
    snapshotData: string,
    cellsCount: number,
    reason: string
  ): Promise<void> {
    const now = new Date().toISOString();
    await this.db
      .prepare(
        `INSERT INTO notebook_snapshots 
          (notebook_id, title, snapshot_data, cells_count, reason, created_at, updated_at) 
         VALUES (?, ?, ?, ?, ?, ?, ?)`
      )
      .bind(notebookId, title, snapshotData, cellsCount, reason, now, now)
      .run();
  }

  async prune(notebookId: string, keepCount: number): Promise<void> {
    await this.db
      .prepare(
        `DELETE FROM notebook_snapshots 
         WHERE notebook_id = ? 
         AND id NOT IN (
           SELECT id FROM notebook_snapshots 
           WHERE notebook_id = ? 
           ORDER BY id DESC 
           LIMIT ?
         )`
      )
      .bind(notebookId, notebookId, keepCount)
      .run();
  }

  async deleteAllByNotebookId(notebookId: string): Promise<void> {
    await this.db
      .prepare("DELETE FROM notebook_snapshots WHERE notebook_id = ?")
      .bind(notebookId)
      .run();
  }

  async count(): Promise<number> {
    const res = await this.db
      .prepare("SELECT COUNT(*) as count FROM notebook_snapshots")
      .first<{ count: number }>();
    return Number(res?.count || 0);
  }
}
