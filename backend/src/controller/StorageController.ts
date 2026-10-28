import { Hono } from "hono";
import type { AppBindings } from "../config/env.ts";
import { StorageService } from "../service/StorageService.ts";

export const StorageController = new Hono<{ Bindings: AppBindings }>();

// POST /api/v1/upload
StorageController.post("/", async (c) => {
  try {
    if (!c.env.BUCKET) {
      return c.json({ error: "R2 Bucket binding is not available" }, 503);
    }

    const storageService = new StorageService(c.env.BUCKET);
    const contentTypeHeader = c.req.header("content-type") || "";

    if (contentTypeHeader.includes("multipart/form-data")) {
      const body = await c.req.parseBody();
      const file = body["file"];

      if (!file || !(file instanceof File)) {
        return c.json({ error: "No file provided in 'file' field" }, 400);
      }

      const result = await storageService.uploadFile(file);
      return c.json(result);
    }

    // Direct binary stream upload
    const customFilename = c.req.header("x-filename") || "unnamed_asset.bin";
    const mimeType = contentTypeHeader || "application/octet-stream";
    const arrayBuffer = await c.req.arrayBuffer();

    const result = await storageService.uploadBinary(arrayBuffer, customFilename, mimeType);
    return c.json(result);
  } catch (error) {
    return c.json(
      { error: error instanceof Error ? error.message : "File upload failed" },
      500
    );
  }
});

// GET /api/v1/files/*
StorageController.get("/:key{.+}", async (c) => {
  try {
    const key = c.req.param("key");

    if (!c.env.BUCKET) {
      return c.json({ error: "R2 Bucket binding is not available" }, 503);
    }

    const storageService = new StorageService(c.env.BUCKET);
    const object = await storageService.getFile(key);

    if (!object) {
      return c.text("File not found in R2 storage", 404);
    }

    const headers = new Headers();
    object.writeHttpMetadata(headers);
    headers.set("etag", object.httpEtag);
    headers.set("Cache-Control", "public, max-age=31536000, immutable");

    return new Response(object.body, { headers });
  } catch (error) {
    return c.text(error instanceof Error ? error.message : "Error reading file", 500);
  }
});

// DELETE /api/v1/files/*
StorageController.delete("/:key{.+}", async (c) => {
  try {
    const key = c.req.param("key");

    if (!c.env.BUCKET) {
      return c.json({ error: "R2 Bucket binding is not available" }, 503);
    }

    const storageService = new StorageService(c.env.BUCKET);
    await storageService.deleteFile(key);
    return c.json({ success: true, message: `File ${key} deleted` });
  } catch (error) {
    return c.json(
      { error: error instanceof Error ? error.message : "Error deleting file" },
      500
    );
  }
});
