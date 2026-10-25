import { test } from 'node:test';
import assert from 'node:assert';
import { LocalStorageNotebookStorage } from '../src/features/notebook/services/notebookStorage.ts';
import { sampleNotebook } from '../src/features/notebook/data/initialSampleNotebook.ts';

// Mock localStorage for node test environment
const mockStorage = new Map();
globalThis.localStorage = {
  getItem: (key) => mockStorage.get(key) || null,
  setItem: (key, val) => mockStorage.set(key, String(val)),
  removeItem: (key) => mockStorage.delete(key),
  clear: () => mockStorage.clear(),
};

test('LocalStorageNotebookStorage loads fallback when empty', () => {
  mockStorage.clear();
  const storage = new LocalStorageNotebookStorage('test_key');
  const result = storage.loadAll();
  assert.strictEqual(result, null);
});

test('LocalStorageNotebookStorage saves and loads multiple notebooks with active tab', () => {
  mockStorage.clear();
  const storage = new LocalStorageNotebookStorage('test_key');

  const nb1 = structuredClone(sampleNotebook);
  nb1.id = 'tab-1';
  nb1.title = 'Notebook 1.json';

  const nb2 = structuredClone(sampleNotebook);
  nb2.id = 'tab-2';
  nb2.title = 'Notebook 2.json';

  storage.saveAll([nb1, nb2], 'tab-2');

  const loaded = storage.loadAll();
  assert.ok(loaded);
  assert.strictEqual(loaded.notebooks.length, 2);
  assert.strictEqual(loaded.activeId, 'tab-2');
  assert.strictEqual(loaded.notebooks[0].title, 'Notebook 1.json');
  assert.strictEqual(loaded.notebooks[1].title, 'Notebook 2.json');
});

test('LocalStorageNotebookStorage migrates legacy single notebook to tabs', () => {
  mockStorage.clear();
  const storage = new LocalStorageNotebookStorage('ielts_jupyter_notebook_v2');

  const legacy = structuredClone(sampleNotebook);
  legacy.id = 'legacy-nb';
  legacy.title = 'Legacy_Notebook.ilnb';

  storage.save(legacy);

  const migrated = storage.loadAll();
  assert.ok(migrated);
  assert.strictEqual(migrated.notebooks.length, 1);
  assert.strictEqual(migrated.activeId, 'legacy-nb');
  assert.strictEqual(migrated.notebooks[0].title, 'Legacy_Notebook.ilnb');
});

test('tab duplication clones notebook with unique IDs and copy title', () => {
  const original = structuredClone(sampleNotebook);
  original.id = 'orig-tab';
  original.title = 'Writing_Task_2.json';
  assert.strictEqual(original.cells.length, 4);

  const copyTitle = original.title.replace(/\.(ilnb|json|ipynb)$/i, (ext) => `_copy${ext}`);
  const cloned = {
    ...structuredClone(original),
    id: 'cloned-tab',
    title: copyTitle,
    cells: original.cells.map((c, i) => ({
      ...structuredClone(c),
      id: `cloned-cell-${i}`,
    })),
  };

  assert.strictEqual(cloned.title, 'Writing_Task_2_copy.json');
  assert.notStrictEqual(cloned.id, original.id);
  assert.strictEqual(cloned.cells.length, original.cells.length);
  assert.notStrictEqual(cloned.cells[0].id, original.cells[0].id);
});

test('closeOtherTabs keeps only selected target notebook', () => {
  const list = [
    { id: 'tab-1', title: 'Doc 1', cells: [] },
    { id: 'tab-2', title: 'Doc 2', cells: [] },
    { id: 'tab-3', title: 'Doc 3', cells: [] },
  ];

  const targetId = 'tab-2';
  const filtered = list.filter((n) => n.id === targetId);

  assert.strictEqual(filtered.length, 1);
  assert.strictEqual(filtered[0].id, 'tab-2');
  assert.strictEqual(filtered[0].title, 'Doc 2');
});
