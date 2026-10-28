import test from "node:test";
import assert from "node:assert/strict";

const BASE_URL = process.env.TEST_API_URL || "http://localhost:3000";

test("Backend API Integration Test Suite", async (t) => {
  await t.test("1. Root Endpoint - Returns architecture info", async () => {
    const res = await fetch(`${BASE_URL}/`);
    assert.equal(res.status, 200);
    const json = await res.json();
    assert.equal(json.service, "IELTS Notebook API");
    assert.ok(json.architecture.includes("Clean Layered Architecture"));
    assert.equal(json.database, "Cloudflare D1 (SQLite)");
    assert.equal(json.storage, "Cloudflare R2");
  });

  await t.test("2. Health Endpoint - D1 and R2 connected", async () => {
    const res = await fetch(`${BASE_URL}/api/v1/health`);
    assert.equal(res.status, 200);
    const json = await res.json();
    assert.equal(json.status, "ok");
    assert.equal(json.database, "connected");
    assert.equal(json.adapter, "cloudflare_d1_sqlite");
    assert.equal(json.storage, "cloudflare_r2");
    assert.equal(typeof json.notebooksCount, "number");
    assert.equal(typeof json.cellsCount, "number");
    assert.equal(typeof json.snapshotsCount, "number");
  });

  await t.test("3. Notebooks List - Returns array of summaries", async () => {
    const res = await fetch(`${BASE_URL}/api/v1/notebooks`);
    assert.equal(res.status, 200);
    const json = await res.json();
    assert.ok(Array.isArray(json.notebooks));
    assert.ok(json.notebooks.length > 0);
  });

  await t.test("4. Current Notebook - Returns default notebook with cells", async () => {
    const res = await fetch(`${BASE_URL}/api/v1/notebooks/current`);
    assert.equal(res.status, 200);
    const doc = await res.json();
    assert.ok(doc.id);
    assert.ok(doc.title);
    assert.ok(Array.isArray(doc.cells));
  });

  const testNotebookId = `test-nb-${Date.now()}`;

  await t.test("5. Create Notebook - Creates notebook with 4-skills cells", async () => {
    const payload = {
      id: testNotebookId,
      title: "Automated Test Notebook",
      cells: [
        {
          id: `${testNotebookId}-c1`,
          cellType: "reading",
          source: "### Reading Test Questions",
          structuredData: {
            version: "1.0",
            skill: "reading",
            title: "Mini-IELTS Automated Reading",
            questionGroups: [
              {
                id: "g1",
                type: "true_false_not_given",
                instruction: "Choose TRUE, FALSE, or NOT GIVEN.",
                questions: [
                  {
                    questionNumber: 1,
                    statement: "Automated test runs successfully.",
                    answer: "TRUE",
                    explanation: "Verified by integration test."
                  }
                ]
              }
            ]
          }
        },
        {
          id: `${testNotebookId}-c2`,
          cellType: "listening",
          source: "### Listening Section Notes",
          resource: {
            type: "audio",
            name: "test_audio.mp3",
            url: "https://example.com/audio.mp3"
          }
        }
      ]
    };

    const res = await fetch(`${BASE_URL}/api/v1/notebooks`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload)
    });

    assert.equal(res.status, 201);
    const created = await res.json();
    assert.equal(created.id, testNotebookId);
    assert.equal(created.title, "Automated Test Notebook");
    assert.equal(created.cells.length, 2);
    assert.equal(created.cells[0].cellType, "reading");
    assert.ok(created.cells[0].structuredData);
    assert.equal(created.cells[0].structuredData.skill, "reading");
  });

  await t.test("6. Sync Notebook - Updates title and syncs cells atomically", async () => {
    const syncPayload = {
      title: "Automated Test Notebook (Updated)",
      cells: [
        {
          id: `${testNotebookId}-c1`,
          cellType: "reading",
          source: "Updated Reading Source Content"
        },
        {
          id: `${testNotebookId}-c3`,
          cellType: "writing",
          source: "New Writing Task Cell"
        }
      ]
    };

    const res = await fetch(`${BASE_URL}/api/v1/notebooks/${testNotebookId}/sync`, {
      method: "PUT",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(syncPayload)
    });

    assert.equal(res.status, 200);
    const updated = await res.json();
    assert.equal(updated.title, "Automated Test Notebook (Updated)");
    assert.equal(updated.cells.length, 2);
    // Verified c2 was removed, c3 was added
    const cellIds = updated.cells.map((c: any) => c.id);
    assert.ok(cellIds.includes(`${testNotebookId}-c1`));
    assert.ok(cellIds.includes(`${testNotebookId}-c3`));
    assert.ok(!cellIds.includes(`${testNotebookId}-c2`));
  });

  await t.test("7. Snapshots History - Records checkpoints on sync", async () => {
    const res = await fetch(`${BASE_URL}/api/v1/notebooks/${testNotebookId}/snapshots`);
    assert.equal(res.status, 200);
    const json = await res.json();
    assert.ok(Array.isArray(json.snapshots));
    assert.ok(json.snapshots.length >= 1);
    assert.equal(json.snapshots[0].notebookId, testNotebookId);
  });

  await t.test("8. Export Notebook - Returns JSON file attachment", async () => {
    const res = await fetch(`${BASE_URL}/api/v1/notebooks/${testNotebookId}/export`);
    assert.equal(res.status, 200);
    assert.ok(res.headers.get("content-disposition")?.includes(".ilnb"));
    const exported = await res.json();
    assert.equal(exported.id, testNotebookId);
    assert.equal(exported.cells.length, 2);
  });

  let uploadedFileKey = "";

  await t.test("9. Cloudflare R2 - Upload binary asset", async () => {
    const formData = new FormData();
    const fileContent = "IELTS Audio Simulation Content - Cloudflare R2 Unit Test";
    const blob = new Blob([fileContent], { type: "text/plain" });
    formData.append("file", blob, "r2-integration-test.txt");

    const res = await fetch(`${BASE_URL}/api/v1/upload`, {
      method: "POST",
      body: formData
    });

    assert.equal(res.status, 200);
    const json = await res.json();
    assert.equal(json.success, true);
    assert.ok(json.key);
    assert.ok(json.url);
    assert.equal(json.name, "r2-integration-test.txt");
    uploadedFileKey = json.key;
  });

  await t.test("10. Cloudflare R2 - Retrieve streamed asset", async () => {
    assert.ok(uploadedFileKey);
    const res = await fetch(`${BASE_URL}/api/v1/files/${uploadedFileKey}`);
    assert.equal(res.status, 200);
    assert.ok(res.headers.get("etag"));
    const text = await res.text();
    assert.equal(text, "IELTS Audio Simulation Content - Cloudflare R2 Unit Test");
  });

  await t.test("11. Cloudflare R2 - Delete asset", async () => {
    assert.ok(uploadedFileKey);
    const res = await fetch(`${BASE_URL}/api/v1/files/${uploadedFileKey}`, {
      method: "DELETE"
    });
    assert.equal(res.status, 200);
    const json = await res.json();
    assert.equal(json.success, true);

    // Verify subsequent fetch returns 404
    const checkRes = await fetch(`${BASE_URL}/api/v1/files/${uploadedFileKey}`);
    assert.equal(checkRes.status, 404);
  });

  await t.test("12. Delete Notebook - Cascades and cleans up", async () => {
    const delRes = await fetch(`${BASE_URL}/api/v1/notebooks/${testNotebookId}`, {
      method: "DELETE"
    });
    assert.equal(delRes.status, 204);

    // Verify it is gone
    const getRes = await fetch(`${BASE_URL}/api/v1/notebooks/${testNotebookId}`);
    assert.equal(getRes.status, 404);

    const listRes = await fetch(`${BASE_URL}/api/v1/notebooks`);
    const listJson = await listRes.json();
    const ids = listJson.notebooks.map((n: any) => n.id);
    assert.ok(!ids.includes(testNotebookId));
  });
});
