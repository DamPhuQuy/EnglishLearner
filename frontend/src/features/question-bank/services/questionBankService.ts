import {
  ALL_QUESTION_BANK_ITEMS,
  type QuestionBankItem,
} from "../../../data/question-bank/index.ts";
import type {
  IeltsExerciseData,
  IeltsQuestionGroup,
  IeltsQuestionType,
} from "../../cell/types/ieltsSchema.ts";
import type {
  QuestionBankFilter,
  QuestionBankStats,
} from "../types/questionBank.ts";

export function getQuestionCount(item: QuestionBankItem): number {
  if (item.questions && Array.isArray(item.questions)) {
    return item.questions.length;
  }
  if (item.writingTask) {
    return 1;
  }
  if (item.speakingTask) {
    if (item.speakingTask.part1Questions) {
      return item.speakingTask.part1Questions.length;
    }
    if (item.speakingTask.cueCard) {
      return 4;
    }
    if (item.speakingTask.part3Questions) {
      return item.speakingTask.part3Questions.length;
    }
    return 1;
  }
  return 1;
}

export function getQuestionBankStats(): QuestionBankStats {
  const stats: QuestionBankStats = {
    totalQuestions: 0,
    totalModules: ALL_QUESTION_BANK_ITEMS.length,
    bySkill: {
      reading: 0,
      listening: 0,
      writing: 0,
      speaking: 0,
    },
    byDifficulty: {
      easy: 0,
      medium: 0,
      advanced: 0,
    },
    byQuestionType: {},
  };

  for (const item of ALL_QUESTION_BANK_ITEMS) {
    const count = getQuestionCount(item);
    stats.totalQuestions += count;

    if (stats.bySkill[item.skill] !== undefined) {
      stats.bySkill[item.skill] += count;
    }

    if (stats.byDifficulty[item.difficulty] !== undefined) {
      stats.byDifficulty[item.difficulty] += count;
    }

    const qType = item.questionType;
    stats.byQuestionType[qType] = (stats.byQuestionType[qType] || 0) + count;
  }

  return stats;
}

export function filterQuestionBank(
  filter: QuestionBankFilter,
  items: QuestionBankItem[] = ALL_QUESTION_BANK_ITEMS
): QuestionBankItem[] {
  return items.filter((item) => {
    // Skill filter
    if (filter.skill && filter.skill !== "all" && item.skill !== filter.skill) {
      return false;
    }

    // Question type filter
    if (
      filter.questionTypes &&
      filter.questionTypes.length > 0 &&
      !filter.questionTypes.includes(item.questionType)
    ) {
      return false;
    }

    // Difficulty filter
    if (
      filter.difficulty &&
      filter.difficulty !== "all" &&
      item.difficulty !== filter.difficulty
    ) {
      return false;
    }

    // Granularity filter
    if (
      filter.granularity &&
      filter.granularity !== "all" &&
      item.granularity !== filter.granularity
    ) {
      return false;
    }

    // Search query filter
    if (filter.search && filter.search.trim() !== "") {
      const q = filter.search.trim().toLowerCase();
      const inTitle = item.title.toLowerCase().includes(q);
      const inTopic = item.topic.toLowerCase().includes(q);
      const inMaterial =
        item.material?.content?.toLowerCase().includes(q) ||
        item.material?.audioTranscript?.toLowerCase().includes(q) ||
        false;
      const inQuestions =
        item.questions?.some(
          (qq) =>
            qq.question?.toLowerCase().includes(q) ||
            qq.statement?.toLowerCase().includes(q) ||
            qq.prefix?.toLowerCase().includes(q)
        ) || false;

      if (!inTitle && !inTopic && !inMaterial && !inQuestions) {
        return false;
      }
    }

    return true;
  });
}

export function getRandomDrill(filter: QuestionBankFilter): QuestionBankItem | null {
  const filtered = filterQuestionBank(filter);
  if (filtered.length === 0) return null;
  const randomIndex = Math.floor(Math.random() * filtered.length);
  return filtered[randomIndex];
}

export function convertQuestionBankItemToExerciseData(
  item: QuestionBankItem
): IeltsExerciseData {
  let questionGroups: IeltsQuestionGroup[] | undefined;

  if (item.questions && item.questions.length > 0) {
    const firstQ = item.questions[0];
    let instruction = "Answer the questions below based on the provided material.";
    let qType = item.questionType as IeltsQuestionType;

    if (item.questionType === "multiple_choice") {
      instruction = "Choose the correct letter, A, B, C or D.";
    } else if (item.questionType === "true_false_not_given") {
      instruction =
        "Do the following statements agree with the information in the text? Choose TRUE, FALSE, or NOT GIVEN.";
    } else if (item.questionType === "yes_no_not_given") {
      instruction =
        "Do the following statements agree with the views of the writer? Choose YES, NO, or NOT GIVEN.";
    } else if (
      item.questionType === "sentence_completion" ||
      item.questionType === "summary_completion" ||
      item.questionType === "form_completion" ||
      item.questionType === "note_completion"
    ) {
      instruction = "Complete the sentences below. Write NO MORE THAN TWO WORDS for each answer.";
    } else if (item.questionType === "matching_headings") {
      instruction = "Choose the correct heading for each paragraph from the list of headings.";
    } else if (item.questionType === "plan_map_diagram_labelling") {
      instruction = "Label the map/plan below. Write the correct letter in the boxes.";
    }

    questionGroups = [
      {
        id: `group-${item.id}`,
        type: qType,
        title: `Questions 1–${item.questions.length}`,
        instruction,
        questions: item.questions,
      },
    ];
  }

  const exercise: IeltsExerciseData = {
    version: "1.0",
    skill: item.skill,
    title: item.title,
    topic: item.topic,
    difficulty: item.band,
    timeLimitMinutes:
      item.granularity === "micro" ? 5 : item.granularity === "drill" ? 12 : 20,
    material: item.material
      ? {
          type: item.material.type,
          title: item.material.title || item.title,
          content: item.material.content,
          audioUrl: item.material.audioUrl,
          audioTranscript: item.material.audioTranscript,
        }
      : item.writingTask
      ? {
          type: "text",
          title: `Writing Task Specification: ${item.title}`,
          content: `[IELTS WRITING SPECIFICATION: ${item.title}]\n\nPrompt:\n${item.writingTask.prompt}\n\nKey Highlights / Requirements:\n${(item.writingTask.bulletPoints || item.writingTask.keyDataPoints || []).map((b: string) => `• ${b}`).join("\n")}\n\nTarget: At least ${item.writingTask.minWords || 150} words.`,
        }
      : item.speakingTask
      ? {
          type: "audio",
          title: `Speaking Studio: ${item.title}`,
        }
      : undefined,
    questionGroups,
    writingTask: item.writingTask,
    speakingTask: item.speakingTask,
  };

  return exercise;
}
