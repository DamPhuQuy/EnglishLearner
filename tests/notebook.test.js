import { test } from 'node:test';
import assert from 'node:assert';
import { sampleNotebook } from '../src/data/initialSample.ts';

test('sample notebook contains 4 skill cells', () => {
  assert.strictEqual(sampleNotebook.cells.length, 4);
  const types = sampleNotebook.cells.map(c => c.cellType);
  assert.ok(types.includes('listening'));
  assert.ok(types.includes('reading'));
  assert.ok(types.includes('writing'));
  assert.ok(types.includes('speaking'));
});

test('listening cell contains audio player resource in Right Grid', () => {
  const listening = sampleNotebook.cells.find(c => c.cellType === 'listening');
  assert.ok(listening);
  assert.strictEqual(listening.resource?.type, 'audio');
  assert.ok(listening.resource?.url);
});

test('writing cell contains prompt document resource in Right Grid', () => {
  const writing = sampleNotebook.cells.find(c => c.cellType === 'writing');
  assert.ok(writing);
  assert.strictEqual(writing.resource?.type, 'text');
  assert.ok(writing.resource?.textContent);
});

test('speaking cell contains voice recorder resource in Right Grid', () => {
  const speaking = sampleNotebook.cells.find(c => c.cellType === 'speaking');
  assert.ok(speaking);
  assert.strictEqual(speaking.resource?.type, 'voice_recorder');
});

const { isNotebook } = await import('../src/lib/notebook.ts');

test('notebook import accepts an exported notebook with persistent attachment data', () => {
  const doc = structuredClone(sampleNotebook);
  doc.cells[0].resource = { type: 'audio', name: 'voice.webm', url: 'data:audio/webm;base64,AAAA' };
  assert.ok(isNotebook(JSON.parse(JSON.stringify(doc))));
});

test('notebook import rejects missing fields, empty cells, duplicates and unsafe resources', () => {
  for (const value of [null, {}, { cells: [] }, { ...sampleNotebook, cells: [] }]) assert.ok(!isNotebook(value));
  const duplicate = structuredClone(sampleNotebook);
  duplicate.cells[1].id = duplicate.cells[0].id;
  assert.ok(!isNotebook(duplicate));
  const invalid = structuredClone(sampleNotebook);
  invalid.cells[0].source = undefined;
  assert.ok(!isNotebook(invalid));
  const unsafe = structuredClone(sampleNotebook);
  unsafe.cells[0].resource.url = 'javascript:alert(1)';
  assert.ok(!isNotebook(unsafe));
  unsafe.cells[0].resource.url = 'data:text/html,<script>alert(1)</script>';
  assert.ok(!isNotebook(unsafe));
});

test('sample audio is clearly labeled as a demo rather than a Cambridge recording', () => {
  assert.match(sampleNotebook.cells[0].resource.name, /demo/);
  assert.doesNotMatch(sampleNotebook.cells[0].resource.name, /Cambridge/);
});
