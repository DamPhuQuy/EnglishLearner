import { AppConfig } from "../config/env.ts";
import type { SnapshotDetailDto, SnapshotSummaryDto } from "../dto/SnapshotDto.ts";
import type { NotebookEntity } from "../model/Notebook.ts";
import { SnapshotRepository } from "../repository/SnapshotRepository.ts";

export class SnapshotService {
  private readonly snapshotRepo: SnapshotRepository;

  constructor(db: D1Database) {
    this.snapshotRepo = new SnapshotRepository(db);
  }

  async recordSnapshot(
    notebookId: string,
    title: string,
    docJson: string,
    cellsCount: number,
    reason = "auto_sync"
  ): Promise<void> {
    // Throttle auto_sync snapshots within 20s
    if (reason === "auto_sync") {
      const recent = await this.snapshotRepo.findLatestByNotebookId(notebookId);
      if (recent && recent.created_at) {
        const diffMs = Date.now() - new Date(recent.created_at).getTime();
        if (diffMs < AppConfig.AUTO_SYNC_SNAPSHOT_THROTTLE_MS) {
          return;
        }
      }
    }

    await this.snapshotRepo.insert(notebookId, title, docJson, cellsCount, reason);
    await this.snapshotRepo.prune(notebookId, AppConfig.MAX_SNAPSHOTS_KEPT);
  }

  async listSnapshots(notebookId: string): Promise<SnapshotSummaryDto[]> {
    return this.snapshotRepo.findByNotebookId(notebookId);
  }

  async getSnapshot(notebookId: string, snapshotId: number): Promise<SnapshotDetailDto | null> {
    const row = await this.snapshotRepo.findByIdAndNotebookId(snapshotId, notebookId);
    if (!row) return null;

    let doc: NotebookEntity;
    try {
      doc = JSON.parse(row.snapshot_data);
    } catch {
      doc = {
        id: notebookId,
        title: row.title,
        cells: [],
        createdAt: row.created_at,
        updatedAt: row.updated_at,
      };
    }

    return {
      snapshot: SnapshotRepository.toSummary(row),
      doc,
    };
  }

  async deleteAllForNotebook(notebookId: string): Promise<void> {
    await this.snapshotRepo.deleteAllByNotebookId(notebookId);
  }
}
