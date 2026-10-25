import { test } from "node:test";
import assert from "node:assert";
import {
  createCell,
  addCellAt,
  removeCellById,
  moveCell,
  patchCell,
  executeCellInList,
} from "../src/features/notebook/types/notebook.ts";
import {
  getSkillTemplate,
  appendTemplateToSource,
} from "../src/features/cell/services/skillTemplates.ts";

test("notebook feature createCell initializes empty cell with null execution count", () => {
  const cell = createCell("speaking");
  assert.strictEqual(cell.cellType, "speaking");
  assert.strictEqual(cell.executionCount, null);
  assert.strictEqual(cell.source, "");
  assert.ok(cell.id);
});

test("notebook feature addCellAt inserts new cell at target index", () => {
  const c1 = createCell("listening");
  const c2 = createCell("reading");
  const c3 = createCell("writing");
  const list = [c1, c2];
  const next = addCellAt(list, 0, c3);
  assert.strictEqual(next.length, 3);
  assert.strictEqual(next[0].id, c1.id);
  assert.strictEqual(next[1].id, c3.id);
  assert.strictEqual(next[2].id, c2.id);
});

test("notebook feature removeCellById preserves at least 1 cell", () => {
  const c1 = createCell("listening");
  const result = removeCellById([c1], c1.id);
  assert.strictEqual(result.cells.length, 1);
  assert.strictEqual(result.removed, null);
});

test("notebook feature removeCellById deletes target cell when more than 1 exists", () => {
  const c1 = createCell("listening");
  const c2 = createCell("reading");
  const result = removeCellById([c1, c2], c1.id);
  assert.strictEqual(result.cells.length, 1);
  assert.strictEqual(result.removed?.id, c1.id);
  assert.strictEqual(result.cells[0].id, c2.id);
});

test("notebook feature moveCell reorders cells within boundaries", () => {
  const c1 = createCell("listening");
  const c2 = createCell("reading");
  const list = [c1, c2];
  const moved = moveCell(list, 0, 1);
  assert.strictEqual(moved[0].id, c2.id);
  assert.strictEqual(moved[1].id, c1.id);

  // Out of bounds
  const unchanged = moveCell(list, 0, -1);
  assert.strictEqual(unchanged[0].id, c1.id);
});

test("notebook feature patchCell updates specified fields", () => {
  const c1 = createCell("listening");
  const patched = patchCell([c1], c1.id, { source: "Hello world" });
  assert.strictEqual(patched[0].source, "Hello world");
});

test("notebook feature executeCellInList increments max execution count and advances focus", () => {
  const c1 = createCell("listening");
  const c2 = createCell("reading");
  const list = [c1, c2];
  const { cells, nextActiveId } = executeCellInList(list, c1.id);
  assert.strictEqual(cells[0].executionCount, 1);
  assert.strictEqual(nextActiveId, c2.id);
});

test("cell feature appendTemplateToSource appends template without overwriting", () => {
  const initial = "My existing notes";
  const updated = appendTemplateToSource(initial, "writing");
  assert.ok(updated.startsWith("My existing notes\n\n### Writing"));
});
