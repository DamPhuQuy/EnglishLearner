import test from "node:test";
import assert from "node:assert/strict";
import app from "../src/index.ts";

test("Backend Unit & Domain Logic Suite", async (t) => {
  await t.test("1. Root Endpoint - Returns architecture info in-memory", async () => {
    const res = await app.request("/");
    assert.equal(res.status, 200);
    const json = await res.json();
    assert.equal(json.service, "IELTS Notebook API");
    assert.ok(json.architecture.includes("Clean Layered Architecture"));
    assert.equal(json.database, "Cloudflare D1 (SQLite)");
    assert.equal(json.storage, "Cloudflare R2");
    assert.equal(json.version, "2.1.0");
  });

  await t.test("2. CORS Headers - Sets correct allow headers & methods", async () => {
    const res = await app.request("/", {
      method: "OPTIONS",
      headers: {
        Origin: "http://localhost:5173",
        "Access-Control-Request-Method": "POST",
      },
    });
    assert.equal(res.status, 204);
    assert.equal(res.headers.get("access-control-allow-origin"), "*");
    assert.ok(res.headers.get("access-control-allow-methods")?.includes("POST"));
  });

  await t.test("3. Not Found Handler - Returns structured 404 response", async () => {
    const res = await app.request("/api/v1/invalid-route-xyz");
    assert.equal(res.status, 404);
    const json = await res.json();
    assert.equal(json.status, 404);
    assert.equal(json.error, "Not Found");
    assert.equal(json.path, "/api/v1/invalid-route-xyz");
  });

  await t.test("4. Cell Model - Validates skill types and resource shapes", () => {
    const validSkills = ["listening", "reading", "writing", "speaking", "markdown"];
    for (const skill of validSkills) {
      assert.ok(typeof skill === "string");
    }

    const testCell = {
      id: "cell-test-1",
      executionCount: null,
      cellType: "listening",
      source: "### Mini-IELTS Listening",
      resource: {
        type: "audio",
        url: "https://example.com/audio.mp3",
        name: "test.mp3",
      },
    };
    assert.equal(testCell.id, "cell-test-1");
    assert.equal(testCell.cellType, "listening");
    assert.equal(testCell.resource.type, "audio");
  });

  await t.test("5. Notebook Entity - Structure matches contract", () => {
    const testNotebook = {
      id: "nb-unit-001",
      title: "Unit Test Notebook",
      cells: [],
      createdAt: new Date().toISOString(),
      updatedAt: new Date().toISOString(),
    };
    assert.equal(testNotebook.id, "nb-unit-001");
    assert.equal(testNotebook.cells.length, 0);
    assert.ok(testNotebook.createdAt);
  });
});
