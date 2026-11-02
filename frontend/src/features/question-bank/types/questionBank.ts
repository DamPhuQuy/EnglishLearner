import type {
  QuestionBankItem,
  QuestionBankMaterial,
} from "../../../data/question-bank/index.ts";
import type { IeltsSkill } from "../../cell/types/ieltsSchema.ts";

export type { QuestionBankItem, QuestionBankMaterial };

export type QuestionDifficulty = "all" | "easy" | "medium" | "advanced";
export type QuestionGranularity = "all" | "micro" | "drill" | "section";

export interface QuestionBankFilter {
  skill?: IeltsSkill | "all";
  questionTypes?: string[];
  difficulty?: QuestionDifficulty;
  granularity?: QuestionGranularity;
  search?: string;
}

export interface QuestionBankStats {
  totalQuestions: number;
  totalModules: number;
  bySkill: Record<string, number>;
  byDifficulty: Record<string, number>;
  byQuestionType: Record<string, number>;
}
