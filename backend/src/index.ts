import { Hono } from "hono";
import { cors } from "hono/cors";
import { logger } from "hono/logger";
import type { AppBindings } from "./config/env.ts";
import { HealthController } from "./controller/HealthController.ts";
import { NotebookController } from "./controller/NotebookController.ts";
import { SnapshotController } from "./controller/SnapshotController.ts";
import { StorageController } from "./controller/StorageController.ts";

const app = new Hono<{ Bindings: AppBindings }>();

// Global Middlewares
app.use("*", logger());
app.use(
  "*",
  cors({
    origin: "*",
    allowMethods: ["GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS"],
    allowHeaders: ["Content-Type", "Authorization", "Accept", "X-Filename"],
    exposeHeaders: ["Content-Length", "Content-Disposition", "ETag"],
    maxAge: 86400,
  })
);

// Root Index Info
app.get("/", (c) => {
  return c.json({
    service: "IELTS Notebook API",
    architecture: "Java Clean Layered Architecture (Controller -> Service -> Repository -> Model/DTO)",
    framework: "Hono on Cloudflare Workers",
    database: "Cloudflare D1 (SQLite)",
    storage: "Cloudflare R2",
    version: "2.1.0",
    healthCheck: "/api/v1/health",
  });
});

// Presentation Layer (REST Controllers)
app.route("/api/v1/health", HealthController);
app.route("/api/v1/notebooks", NotebookController);
app.route("/api/v1/notebooks", SnapshotController);
app.route("/api/v1/upload", StorageController);
app.route("/api/v1/files", StorageController);

// 404 Not Found Handler
app.notFound((c) => {
  return c.json(
    {
      status: 404,
      error: "Not Found",
      path: c.req.path,
    },
    404
  );
});

// Global Exception Handler
app.onError((err, c) => {
  console.error("Unhandled Worker Exception:", err);
  return c.json(
    {
      status: 500,
      error: err.message || "Internal Server Error",
    },
    500
  );
});

export default app;
