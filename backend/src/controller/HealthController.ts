import { Hono } from "hono";
import type { AppBindings } from "../config/env.ts";
import { HealthService } from "../service/HealthService.ts";

export const HealthController = new Hono<{ Bindings: AppBindings }>();

HealthController.get("/", async (c) => {
  const service = new HealthService(c.env.DB, c.env.ENVIRONMENT);
  const health = await service.checkHealth();
  const statusCode = health.status === "ok" ? 200 : 500;
  return c.json(health, statusCode);
});
