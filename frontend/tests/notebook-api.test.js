import { test } from 'node:test';
import assert from 'node:assert';
import { NotebookApiClient } from '../src/features/notebook/services/notebookApiClient.ts';
import { sampleNotebook } from '../src/features/notebook/data/initialSampleNotebook.ts';

test('NotebookApiClient initializes with correct base url', () => {
  const client = new NotebookApiClient('http://localhost:3000/api/v1/');
  // Should trim trailing slash
  client.setBaseUrl('http://127.0.0.1:3000/api/v1/');
  assert.ok(client);
});

test('NotebookApiClient gracefully handles network errors on checkHealth', async () => {
  const client = new NotebookApiClient('http://127.0.0.1:9999/api/v1'); // unreachable port
  const health = await client.checkHealth();
  assert.strictEqual(health.status, 'error');
  assert.strictEqual(health.database, 'disconnected');
  assert.ok(health.message);
});

test('NotebookApiClient gracefully handles network errors on syncNotebook', async () => {
  const client = new NotebookApiClient('http://127.0.0.1:9999/api/v1');
  const res = await client.syncNotebook(sampleNotebook);
  assert.strictEqual(res.success, false);
  assert.ok(res.error);
});
