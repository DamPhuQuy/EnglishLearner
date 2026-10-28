import { AppConfig } from "../config/env.ts";
import type {
  CreateNotebookRequestDto,
  ImportNotebookRequestDto,
  NotebookSummaryDto,
  SyncNotebookRequestDto,
} from "../dto/NotebookDto.ts";
import type { JupyterCell } from "../model/Cell.ts";
import type { NotebookEntity } from "../model/Notebook.ts";
import { CellRepository } from "../repository/CellRepository.ts";
import { NotebookRepository } from "../repository/NotebookRepository.ts";
import { SnapshotService } from "./SnapshotService.ts";

export class NotebookService {
  private readonly notebookRepo: NotebookRepository;
  private readonly cellRepo: CellRepository;
  private readonly snapshotService: SnapshotService;

  constructor(private readonly db: D1Database) {
    this.notebookRepo = new NotebookRepository(db);
    this.cellRepo = new CellRepository(db);
    this.snapshotService = new SnapshotService(db);
  }

  async getNotebookById(id: string): Promise<NotebookEntity | null> {
    const row = await this.notebookRepo.findById(id);
    if (!row) return null;

    const cells = await this.cellRepo.findByNotebookId(id);
    return {
      id: row.id,
      title: row.title,
      description: row.description,
      cells,
      createdAt: row.created_at,
      updatedAt: row.updated_at,
    };
  }

  async getLatestNotebook(): Promise<NotebookEntity | null> {
    const row = await this.notebookRepo.findLatest();
    if (!row) return null;

    const cells = await this.cellRepo.findByNotebookId(row.id);
    return {
      id: row.id,
      title: row.title,
      description: row.description,
      cells,
      createdAt: row.created_at,
      updatedAt: row.updated_at,
    };
  }

  async ensureDefaultNotebook(): Promise<NotebookEntity> {
    const existing = await this.getNotebookById(AppConfig.DEFAULT_NOTEBOOK_ID);
    if (existing) return existing;

    await this.notebookRepo.insert(
      AppConfig.DEFAULT_NOTEBOOK_ID,
      AppConfig.DEFAULT_NOTEBOOK_TITLE,
      AppConfig.DEFAULT_NOTEBOOK_DESCRIPTION
    );

    return (await this.getNotebookById(AppConfig.DEFAULT_NOTEBOOK_ID))!;
  }

  async listAllSummaries(): Promise<NotebookSummaryDto[]> {
    return this.notebookRepo.findAllSummaries();
  }

  async createNotebook(params: CreateNotebookRequestDto): Promise<NotebookEntity> {
    const id = params.id || crypto.randomUUID();
    const title = params.title || params.notebook?.title || AppConfig.DEFAULT_NOTEBOOK_TITLE;
    const cells = params.cells || [];

    return this.syncNotebook(id, {
      title,
      cells,
      reason: "create",
    });
  }

  async updateNotebookTitle(id: string, title: string): Promise<NotebookEntity | null> {
    const existing = await this.notebookRepo.findById(id);
    if (!existing) return null;

    await this.notebookRepo.updateTitle(id, title);
    return this.getNotebookById(id);
  }

  async syncNotebook(notebookId: string, params: SyncNotebookRequestDto): Promise<NotebookEntity> {
    const now = new Date().toISOString();
    const existing = await this.notebookRepo.findById(notebookId);

    if (!existing) {
      const title = params.title || AppConfig.DEFAULT_NOTEBOOK_TITLE;
      await this.notebookRepo.insert(notebookId, title, null);
    } else if (params.title && params.title !== existing.title) {
      await this.notebookRepo.updateTitle(notebookId, params.title);
    } else {
      await this.notebookRepo.touch(notebookId);
    }

    const incomingCells = Array.isArray(params.cells) ? params.cells : null;

    if (incomingCells !== null) {
      const incomingIds = incomingCells
        .map((c) => c.id || (c as any)["id"])
        .filter(Boolean)
        .map(String);

      const statements: D1PreparedStatement[] = [];

      // 1. Delete removed cells
      statements.push(this.cellRepo.buildDeleteNotMatchingStatement(notebookId, incomingIds));

      // 2. Upsert each cell in position order
      for (let index = 0; index < incomingCells.length; index++) {
        const c = incomingCells[index];
        statements.push(this.cellRepo.buildUpsertStatement(notebookId, c, index, now));
      }

      await this.cellRepo.executeBatch(statements);
    }

    const updatedDoc = (await this.getNotebookById(notebookId))!;

    // Snapshot checkpoint
    const reason = params.reason || "auto_sync";
    await this.snapshotService.recordSnapshot(
      notebookId,
      updatedDoc.title,
      JSON.stringify(updatedDoc),
      updatedDoc.cells.length,
      reason
    );

    return updatedDoc;
  }

  async restoreFromSnapshot(notebookId: string, snapshotId: number): Promise<NotebookEntity | null> {
    const snap = await this.snapshotService.getSnapshot(notebookId, snapshotId);
    if (!snap) return null;

    return this.syncNotebook(notebookId, {
      title: snap.doc.title,
      cells: snap.doc.cells,
      reason: `restore_from_snapshot_${snapshotId}`,
    });
  }

  async deleteNotebook(id: string): Promise<void> {
    await this.cellRepo.deleteAllByNotebookId(id);
    await this.snapshotService.deleteAllForNotebook(id);
    await this.notebookRepo.delete(id);
  }

  async importNotebook(params: ImportNotebookRequestDto): Promise<NotebookEntity> {
    const doc = params.notebook || params;
    const id = doc.id || crypto.randomUUID();
    const title = doc.title || "Imported Notebook";
    const cells = Array.isArray(doc.cells) ? doc.cells : [];

    return this.syncNotebook(id, {
      title,
      cells,
      reason: "import",
    });
  }
}
