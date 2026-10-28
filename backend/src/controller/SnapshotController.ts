import { Hono } from "hono";
import type { AppBindings } from "../config/env.ts";
import { NotebookService } from "../service/NotebookService.ts";
import { SnapshotService } from "../service/SnapshotService.ts";

export const SnapshotController = new Hono<{ Bindings: AppBindings }>();

// GET /api/v1/notebooks/:notebook_id/snapshots
SnapshotController.get("/:notebook_id/snapshots", async (c) => {
  const notebookId = c.req.param("notebook_id");
  const service = new SnapshotService(c.env.DB);
  const snapshots = await service.listSnapshots(notebookId);
  return c.json({ snapshots });
});

// GET /api/v1/notebooks/:notebook_id/snapshots/:id
SnapshotController.get("/:notebook_id/snapshots/:id", async (c) => {
  const notebookId = c.req.param("notebook_id");
  const snapshotId = Number(c.req.param("id"));

  const service = new SnapshotService(c.env.DB);
  const detail = await service.getSnapshot(notebookId, snapshotId);

  if (!detail) {
    return c.json({ error: "Snapshot not found" }, 404);
  }

  return c.json(detail);
});

// POST /api/v1/notebooks/:notebook_id/snapshots/:id/restore
SnapshotController.post("/:notebook_id/snapshots/:id/restore", async (c) => {
  const notebookId = c.req.param("notebook_id");
  const snapshotId = Number(c.req.param("id"));

  const notebookService = new NotebookService(c.env.DB);
  const restored = await notebookService.restoreFromSnapshot(notebookId, snapshotId);

  if (!restored) {
    return c.json({ error: "Snapshot not found or restore failed" }, 404);
  }

  return c.json({
    message: `Notebook successfully restored from snapshot ${snapshotId}`,
    notebook: restored,
  });
});
