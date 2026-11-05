import listeningData from "./listeningQuestions.json" with { type: "json" };
import readingData from "./readingQuestions.json" with { type: "json" };
import speakingData from "./speakingQuestions.json" with { type: "json" };
import writingData from "./writingQuestions.json" with { type: "json" };

export interface QuestionBankMaterial {
  type: "text" | "audio" | "image";
  title?: string;
  content?: string;
  audioUrl?: string;
  audioTranscript?: string;
  imageUrl?: string;
  imageDescription?: string;
}

export interface QuestionBankItem {
  id: string;
  skill: "reading" | "listening" | "writing" | "speaking";
  questionType: string;
  difficulty: "easy" | "medium" | "advanced";
  band: string;
  granularity: "micro" | "drill" | "section";
  title: string;
  topic: string;
  instruction?: string;
  wordLimitRule?: string;
  headingsList?: Array<{ id: string; heading: string }>;
  featuresList?: Array<{ key: string; name: string; description?: string }>;
  endingsList?: Array<{ key: string; text: string }>;
  boxOptions?: Array<{ key: string; word: string }>;
  material?: QuestionBankMaterial;
  questions?: any[];
  questionGroups?: any[];
  writingTask?: any;
  speakingTask?: any;
}

export const READING_QUESTIONS: QuestionBankItem[] = readingData as unknown as QuestionBankItem[];
export const LISTENING_QUESTIONS: QuestionBankItem[] = listeningData as unknown as QuestionBankItem[];
export const WRITING_QUESTIONS: QuestionBankItem[] = writingData as unknown as QuestionBankItem[];
export const SPEAKING_QUESTIONS: QuestionBankItem[] = speakingData as unknown as QuestionBankItem[];

export const ALL_QUESTION_BANK_ITEMS: QuestionBankItem[] = [
  ...READING_QUESTIONS,
  ...LISTENING_QUESTIONS,
  ...WRITING_QUESTIONS,
  ...SPEAKING_QUESTIONS,
];
