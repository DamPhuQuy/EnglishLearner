import { Hono } from "hono";
import type { AppBindings } from "../config/env.ts";
import { NotebookService } from "../service/NotebookService.ts";

export const NotebookController = new Hono<{ Bindings: AppBindings }>();

// GET /api/v1/notebooks
NotebookController.get("/", async (c) => {
  const service = new NotebookService(c.env.DB);
  const notebooks = await service.listAllSummaries();
  return c.json({ notebooks });
});

// GET /api/v1/notebooks/current
NotebookController.get("/current", async (c) => {
  const service = new NotebookService(c.env.DB);
  let doc = await service.getLatestNotebook();
  if (!doc) {
    doc = await service.ensureDefaultNotebook();
  }
  return c.json(doc);
});

// POST /api/v1/notebooks/import
NotebookController.post("/import", async (c) => {
  try {
    const body = await c.req.json();
    const service = new NotebookService(c.env.DB);
    const notebook = await service.importNotebook(body);
    return c.json(notebook, 201);
  } catch (error) {
    return c.json(
      { error: error instanceof Error ? error.message : "Failed to import notebook" },
      422
    );
  }
});

// GET /api/v1/notebooks/:id
NotebookController.get("/:id", async (c) => {
  const id = c.req.param("id");
  const service = new NotebookService(c.env.DB);

  if (id === "current" || id === "default") {
    let doc = await service.getLatestNotebook();
    if (!doc) doc = await service.ensureDefaultNotebook();
    return c.json(doc);
  }

  const doc = await service.getNotebookById(id);
  if (!doc) {
    return c.json({ error: "Notebook not found" }, 404);
  }

  return c.json(doc);
});

// POST /api/v1/notebooks
NotebookController.post("/", async (c) => {
  try {
    const body = await c.req.json();
    const service = new NotebookService(c.env.DB);
    const notebook = await service.createNotebook(body);
    return c.json(notebook, 201);
  } catch (error) {
    return c.json(
      { errors: [error instanceof Error ? error.message : "Failed to create notebook"] },
      422
    );
  }
});

// PUT /api/v1/notebooks/:id
NotebookController.put("/:id", async (c) => {
  try {
    const id = c.req.param("id");
    const body = await c.req.json();
    const title = body.title || body.notebook?.title;

    const service = new NotebookService(c.env.DB);
    if (title) {
      const doc = await service.updateNotebookTitle(id, title);
      if (!doc) return c.json({ error: "Notebook not found" }, 404);
      return c.json(doc);
    }

    const doc = await service.getNotebookById(id);
    if (!doc) return c.json({ error: "Notebook not found" }, 404);
    return c.json(doc);
  } catch (error) {
    return c.json(
      { errors: [error instanceof Error ? error.message : "Failed to update notebook"] },
      422
    );
  }
});

// PUT /api/v1/notebooks/:id/sync
NotebookController.put("/:id/sync", async (c) => {
  try {
    const id = c.req.param("id");
    const body = await c.req.json();
    const service = new NotebookService(c.env.DB);
    const notebook = await service.syncNotebook(id, body);
    return c.json(notebook);
  } catch (error) {
    return c.json(
      { error: error instanceof Error ? error.message : "Sync failed" },
      422
    );
  }
});

// DELETE /api/v1/notebooks/:id
NotebookController.delete("/:id", async (c) => {
  const id = c.req.param("id");
  const service = new NotebookService(c.env.DB);
  await service.deleteNotebook(id);
  return c.body(null, 204);
});

// GET /api/v1/notebooks/:id/export
NotebookController.get("/:id/export", async (c) => {
  const id = c.req.param("id");
  const service = new NotebookService(c.env.DB);
  const doc = await service.getNotebookById(id);
  if (!doc) return c.json({ error: "Notebook not found" }, 404);

  const filename = `${doc.title.toLowerCase().replace(/[^a-z0-9_-]/g, "_") || "notebook"}.ilnb`;
  return new Response(JSON.stringify(doc, null, 2), {
    headers: {
      "Content-Type": "application/json; charset=utf-8",
      "Content-Disposition": `attachment; filename="${filename}"`,
    },
  });
});
