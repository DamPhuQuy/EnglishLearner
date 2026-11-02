import { test } from "node:test";
import assert from "node:assert";
import {
  ALL_QUESTION_BANK_ITEMS,
  READING_QUESTIONS,
  LISTENING_QUESTIONS,
  WRITING_QUESTIONS,
  SPEAKING_QUESTIONS,
} from "../src/data/question-bank/index.ts";
import {
  getQuestionCount,
  getQuestionBankStats,
  filterQuestionBank,
  convertQuestionBankItemToExerciseData,
  getRandomDrill,
} from "../src/features/question-bank/services/questionBankService.ts";

test("Question Bank has exact 500-question scale across 4 skills", () => {
  const stats = getQuestionBankStats();
  assert.strictEqual(stats.totalQuestions, 500, "Must contain exactly 500 questions");
  assert.strictEqual(stats.bySkill.reading, 165, "Reading must have 165 questions");
  assert.strictEqual(stats.bySkill.listening, 145, "Listening must have 145 questions");
  assert.strictEqual(stats.bySkill.writing, 75, "Writing must have 75 tasks");
  assert.strictEqual(stats.bySkill.speaking, 115, "Speaking must have 115 questions/prompts");
});

test("Question Bank filters properly by individual skill", () => {
  const readingOnly = filterQuestionBank({ skill: "reading" });
  assert.ok(readingOnly.length > 0);
  assert.ok(readingOnly.every((i) => i.skill === "reading"));

  const listeningOnly = filterQuestionBank({ skill: "listening" });
  assert.ok(listeningOnly.length > 0);
  assert.ok(listeningOnly.every((i) => i.skill === "listening"));

  const writingOnly = filterQuestionBank({ skill: "writing" });
  assert.ok(writingOnly.length > 0);
  assert.ok(writingOnly.every((i) => i.skill === "writing"));

  const speakingOnly = filterQuestionBank({ skill: "speaking" });
  assert.ok(speakingOnly.length > 0);
  assert.ok(speakingOnly.every((i) => i.skill === "speaking"));
});

test("Question Bank filters by specific question type (e.g. Multiple Choice)", () => {
  const mcqOnly = filterQuestionBank({ questionTypes: ["multiple_choice"] });
  assert.ok(mcqOnly.length > 0);
  assert.ok(mcqOnly.every((i) => i.questionType === "multiple_choice"));

  const tfngOnly = filterQuestionBank({ questionTypes: ["true_false_not_given"] });
  assert.ok(tfngOnly.length > 0);
  assert.ok(tfngOnly.every((i) => i.questionType === "true_false_not_given"));
});

test("Question Bank filters by difficulty ladder (Easy, Medium, Advanced)", () => {
  const easyItems = filterQuestionBank({ difficulty: "easy" });
  assert.ok(easyItems.length > 0);
  assert.ok(easyItems.every((i) => i.difficulty === "easy"));

  const medItems = filterQuestionBank({ difficulty: "medium" });
  assert.ok(medItems.length > 0);
  assert.ok(medItems.every((i) => i.difficulty === "medium"));

  const advItems = filterQuestionBank({ difficulty: "advanced" });
  assert.ok(advItems.length > 0);
  assert.ok(advItems.every((i) => i.difficulty === "advanced"));
});

test("Question Bank converts item to valid IeltsExerciseData conforming to schema", () => {
  const readingItem = READING_QUESTIONS[0];
  const exercise = convertQuestionBankItemToExerciseData(readingItem);

  assert.strictEqual(exercise.version, "1.0");
  assert.strictEqual(exercise.skill, "reading");
  assert.ok(exercise.title);
  assert.ok(exercise.material);
  assert.strictEqual(exercise.material.type, "text");
  assert.ok(exercise.material.content);
  assert.ok(exercise.questionGroups && exercise.questionGroups.length > 0);

  const group = exercise.questionGroups[0];
  assert.ok(group.questions.length > 0);
  assert.ok(group.questions[0].answer, "Every question must have an answer");
  assert.ok(group.questions[0].explanation, "Every question must have an explanation");
});

test("100% of questions contain pedagogical explanation and answer grounding", () => {
  for (const item of ALL_QUESTION_BANK_ITEMS) {
    if (item.questions) {
      for (const q of item.questions) {
        assert.ok(q.answer !== undefined && q.answer !== "", `Question ${q.questionNumber} in ${item.id} must have answer`);
        assert.ok(q.explanation && q.explanation.length > 5, `Question ${q.questionNumber} in ${item.id} must have explanation`);
      }
    } else if (item.writingTask) {
      assert.ok(item.writingTask.prompt, `Writing task ${item.id} must have prompt`);
      assert.ok(item.writingTask.sampleEssay, `Writing task ${item.id} must have sampleEssay`);
    } else if (item.speakingTask) {
      assert.ok(item.speakingTask.topic, `Speaking task ${item.id} must have topic`);
    }
  }
});

test("Random drill picker returns valid matching item", () => {
  const randomDrill = getRandomDrill({ skill: "reading", questionTypes: ["multiple_choice"] });
  assert.ok(randomDrill);
  assert.strictEqual(randomDrill.skill, "reading");
  assert.strictEqual(randomDrill.questionType, "multiple_choice");
});
