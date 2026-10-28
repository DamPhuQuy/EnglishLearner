import type { DatabaseHealthResponseDto } from "../dto/HealthDto.ts";
import { CellRepository } from "../repository/CellRepository.ts";
import { NotebookRepository } from "../repository/NotebookRepository.ts";
import { SnapshotRepository } from "../repository/SnapshotRepository.ts";

export class HealthService {
  private readonly notebookRepo: NotebookRepository;
  private readonly cellRepo: CellRepository;
  private readonly snapshotRepo: SnapshotRepository;

  constructor(private readonly db: D1Database, private readonly environment = "development") {
    this.notebookRepo = new NotebookRepository(db);
    this.cellRepo = new CellRepository(db);
    this.snapshotRepo = new SnapshotRepository(db);
  }

  async checkHealth(): Promise<DatabaseHealthResponseDto> {
    try {
      const [notebooksCount, cellsCount, snapshotsCount] = await Promise.all([
        this.notebookRepo.count(),
        this.cellRepo.count(),
        this.snapshotRepo.count(),
      ]);

      return {
        status: "ok",
        database: "connected",
        adapter: "cloudflare_d1_sqlite",
        storage: "cloudflare_r2",
        environment: this.environment,
        notebooksCount,
        cellsCount,
        snapshotsCount,
        timestamp: new Date().toISOString(),
      };
    } catch (error) {
      return {
        status: "error",
        database: "disconnected",
        adapter: "cloudflare_d1_sqlite",
        storage: "cloudflare_r2",
        environment: this.environment,
        notebooksCount: 0,
        cellsCount: 0,
        snapshotsCount: 0,
        message: error instanceof Error ? error.message : "Database check failed",
        timestamp: new Date().toISOString(),
      };
    }
  }
}
