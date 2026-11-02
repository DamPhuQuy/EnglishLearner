import { test } from "node:test";
import assert from "node:assert";
import {
  TOTAL_PROCEDURAL_CAPACITY,
  getProceduralQuestionByIndex,
  generateProceduralBatch,
} from "../src/features/question-bank/services/infiniteQuestionEngine.ts";
import {
  convertQuestionBankItemToExerciseData,
  getQuestionCount,
} from "../src/features/question-bank/services/questionBankService.ts";

test("Infinite Question Engine provides at least 500,000 deterministic questions", () => {
  assert.ok(
    TOTAL_PROCEDURAL_CAPACITY >= 500000,
    `Capacity must be >= 500,000 (actual: ${TOTAL_PROCEDURAL_CAPACITY})`
  );
});

test("Deterministic stability: Same index yields identical content and answers", () => {
  const index = 428192;
  const q1 = getProceduralQuestionByIndex(index);
  const q2 = getProceduralQuestionByIndex(index);

  assert.strictEqual(q1.id, q2.id);
  assert.strictEqual(q1.title, q2.title);
  assert.strictEqual(q1.skill, q2.skill);
  assert.strictEqual(q1.questionType, q2.questionType);
  assert.strictEqual(q1.difficulty, q2.difficulty);
  assert.deepStrictEqual(q1.questions, q2.questions);
  assert.deepStrictEqual(q1.material, q2.material);
});

test("Generates valid IELTS items across boundary indices (0, 1000, 428192, 499999)", () => {
  const testIndices = [0, 1000, 250000, 428192, 499999];
  for (const idx of testIndices) {
    const item = getProceduralQuestionByIndex(idx);
    assert.ok(item, `Item at index ${idx} must be defined`);
    assert.ok(item.id.startsWith("proc-"), `ID must start with proc-`);
    assert.ok(item.id.endsWith(`-${idx}`), `ID must end with index ${idx}`);
    assert.ok(["reading", "listening", "writing", "speaking"].includes(item.skill));
    assert.ok(["easy", "medium", "advanced"].includes(item.difficulty));
    assert.ok(item.band.length > 0);
    assert.ok(item.title.length > 0);

    const count = getQuestionCount(item);
    assert.ok(count >= 1, `Must have at least 1 question (has ${count})`);

    // Verify Exercise conversion
    const exercise = convertQuestionBankItemToExerciseData(item);
    assert.strictEqual(exercise.skill, item.skill);
    assert.ok(exercise.title.length > 0);
  }
});

test("Listening questions have authentic multi-speaker transcripts", () => {
  // Synthesize a batch of listening questions
  const listeningBatch = generateProceduralBatch({ skill: "listening" }, 20);
  assert.strictEqual(listeningBatch.length, 20);

  for (const item of listeningBatch) {
    assert.strictEqual(item.skill, "listening");
    assert.ok(item.material?.audioTranscript, "Must have an audio transcript");
    // Verify speaker turns formatted
    assert.ok(
      item.material.audioTranscript.includes("[Speaker"),
      "Transcript must feature structured dialogue turns [Speaker 1/2]"
    );
  }
});

test("Reading questions contain academic text and answer citations", () => {
  const readingBatch = generateProceduralBatch({ skill: "reading" }, 20);
  assert.strictEqual(readingBatch.length, 20);

  for (const item of readingBatch) {
    assert.strictEqual(item.skill, "reading");
    assert.ok(item.material?.content, "Reading must have passage content");
    assert.ok(item.material.content.length > 100, "Reading passage must be substantive");

    for (const q of item.questions || []) {
      assert.ok(q.explanation, "Reading question must have explanation");
      assert.ok(q.textCitation, "Reading question must have exact text citation");
    }
  }
});

test("Batch generation respects filter constraints", () => {
  const filtered = generateProceduralBatch(
    {
      skill: "reading",
      difficulty: "advanced",
      questionType: "multiple_choice",
    },
    15
  );

  assert.strictEqual(filtered.length, 15);
  for (const item of filtered) {
    assert.strictEqual(item.skill, "reading");
    assert.strictEqual(item.difficulty, "advanced");
    assert.strictEqual(item.questionType, "multiple_choice");
  }
});

test("Ultra-fast sub-millisecond execution: 1,000 procedural questions synthesized in < 200ms", () => {
  const start = performance.now();
  const count = 1000;
  for (let i = 0; i < count; i++) {
    getProceduralQuestionByIndex(i * 499);
  }
  const duration = performance.now() - start;
  const avgMsPerQuestion = duration / count;

  assert.ok(
    duration < 200,
    `1,000 questions synthesized in ${duration.toFixed(2)}ms (expected < 200ms, avg ${avgMsPerQuestion.toFixed(3)}ms/Q)`
  );
});
