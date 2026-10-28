export type IeltsSkill = "reading" | "listening" | "writing" | "speaking";

export type IeltsQuestionType =
  // Reading & Listening Shared Types
  | "true_false_not_given"
  | "yes_no_not_given"
  | "multiple_choice"
  | "sentence_completion"
  | "summary_completion"
  | "note_completion"
  | "form_completion"
  | "table_completion"
  | "flow_chart_completion"
  | "short_answer"
  // Matching Variations
  | "matching_headings"
  | "matching_information"
  | "matching_features"
  | "matching_sentence_endings"
  // Spatial & Diagram Labelling
  | "plan_map_diagram_labelling"
  // Productive Skills
  | "writing_task"
  | "speaking_task";

export interface IeltsMultipleChoiceOption {
  key: string; // "A", "B", "C", "D", "E"...
  text: string;
}

export interface IeltsBaseQuestion {
  id?: string;
  questionNumber: number;
  explanation?: string;
  paragraphRef?: string; // e.g. "Paragraph B" or "Audio timestamp 02:15"
}

export interface IeltsTfngQuestion extends IeltsBaseQuestion {
  statement: string;
  answer: "TRUE" | "FALSE" | "NOT GIVEN" | "YES" | "NO";
}

export interface IeltsMultipleChoiceQuestion extends IeltsBaseQuestion {
  question: string;
  options: IeltsMultipleChoiceOption[];
  answer: string | string[]; // Single ("B") or multiple (["A", "C"])
  isMultiSelect?: boolean;
  maxChoices?: number; // e.g. 2 for "Choose TWO letters"
}

export interface IeltsCompletionQuestion extends IeltsBaseQuestion {
  prefix?: string;
  suffix?: string;
  prompt?: string;
  answer: string;
  acceptedAnswers?: string[];
  maxWords?: number; // e.g. 1 for "ONE WORD ONLY", 2 for "NO MORE THAN TWO WORDS"
}

export interface IeltsHeadingOption {
  id: string; // "i", "ii", "iii", "iv", "v"...
  heading: string;
}

export interface IeltsMatchingHeadingQuestion extends IeltsBaseQuestion {
  paragraph: string; // "A", "B", "C"...
  answer: string; // "iii"
}

export interface IeltsMatchingFeatureOption {
  key: string; // "A", "B", "C"...
  name: string; // e.g. "Dr. Peter Watson", "The Middle Stone Age"
  description?: string;
}

export interface IeltsMatchingFeatureQuestion extends IeltsBaseQuestion {
  statement: string;
  answer: string; // "A"
}

export interface IeltsMatchingSentenceEndingQuestion extends IeltsBaseQuestion {
  beginning: string;
  answer: string; // e.g. "C"
}

export interface IeltsDiagramLabelQuestion extends IeltsBaseQuestion {
  labelLocation: string; // e.g. "Top turbine chamber (Point 14)"
  answer: string;
  acceptedAnswers?: string[];
}

export type IeltsQuestionItem =
  | IeltsTfngQuestion
  | IeltsMultipleChoiceQuestion
  | IeltsCompletionQuestion
  | IeltsMatchingHeadingQuestion
  | IeltsMatchingFeatureQuestion
  | IeltsMatchingSentenceEndingQuestion
  | IeltsDiagramLabelQuestion
  | (IeltsBaseQuestion & Record<string, any>);

export interface IeltsQuestionGroup {
  id: string;
  type: IeltsQuestionType;
  title?: string; // e.g. "Questions 1–5", "Questions 6–10"
  instruction: string; // e.g. "Choose the correct letter, A, B, C or D."
  wordLimitRule?: string; // e.g. "NO MORE THAN TWO WORDS AND/OR A NUMBER"
  headingsList?: IeltsHeadingOption[];
  featuresList?: IeltsMatchingFeatureOption[];
  endingsList?: Array<{ key: string; text: string }>;
  boxOptions?: Array<{ key: string; word: string }>; // For summary completion with a box of words
  questions: IeltsQuestionItem[];
}

export type IeltsWritingTaskType =
  | "task1_academic"
  | "task1_general"
  | "task2_opinion"
  | "task2_discussion"
  | "task2_advantages_disadvantages"
  | "task2_problem_solution"
  | "task2_two_part";

export interface IeltsWritingTaskData {
  taskType: "task1" | "task2" | IeltsWritingTaskType;
  academicVisualType?:
    | "bar_chart"
    | "line_graph"
    | "pie_chart"
    | "table"
    | "map_plan"
    | "process_diagram"
    | "multiple_charts";
  generalLetterType?: "formal" | "semi_formal" | "informal";
  essayCategory?:
    | "agree_disagree"
    | "discuss_both_views"
    | "advantages_outweigh"
    | "causes_solutions"
    | "double_question";
  prompt: string;
  bulletPoints?: string[]; // Letter bullets or task prompts
  keyDataPoints?: string[];
  minWords: number; // 150 (Task 1) or 250 (Task 2)
  timeSuggestedMinutes?: number; // 20 or 40
  sampleEssay?: string;
  sampleExaminerBand?: string; // e.g. "Band 8.5"
  bandRubricHighlights?: {
    taskAchievement?: string;
    coherenceCohesion?: string;
    lexicalResource?: string;
    grammaticalRange?: string;
  };
}

export interface IeltsSpeakingCueCard {
  title: string; // e.g. "Describe an environmental initiative you know about"
  bulletPoints: string[]; // "You should say: What it is...", "Where it happened..."
  roundingOffQuestion?: string;
}

export interface IeltsSpeakingTaskData {
  part: 1 | 2 | 3;
  topic: string;
  part1Questions?: Array<{ questionNumber: number; question: string }>;
  cueCard?: IeltsSpeakingCueCard;
  part3Questions?: Array<{ questionNumber: number; question: string; promptNote?: string }>;
  recommendedIdioms?: Array<{ phrase: string; meaning: string; example: string }>;
  discourseMarkers?: string[];
  preparationSeconds?: number; // 60 for Part 2
  speakingSeconds?: number; // 120 for Part 2
  assessmentCriteria?: {
    fluencyCoherence?: string;
    lexicalResource?: string;
    grammaticalRange?: string;
    pronunciation?: string;
  };
}

export interface IeltsExerciseMaterial {
  type: "text" | "audio" | "image" | "pdf";
  title?: string;
  content?: string; // Reading passage with [A], [B], [C] paragraph markers
  audioUrl?: string;
  audioTranscript?: string;
  imageUrl?: string;
  imageDescription?: string; // Detailed breakdown of charts/maps
}

export interface IeltsVocabularyNote {
  word: string;
  type?: string; // "noun", "verb", "adj", "collocation"
  phonetic?: string;
  definition: string;
  example?: string;
}

export interface IeltsScoreResult {
  correct: number;
  total: number;
  checkedAt?: string;
  bandEstimate?: string;
}

export interface IeltsExerciseData {
  version: "1.0";
  skill: IeltsSkill;
  title: string;
  topic?: string;
  difficulty?: string; // e.g. "Band 6.0–7.0", "Academic Cambridge 18"
  timeLimitMinutes?: number;
  material?: IeltsExerciseMaterial;
  questionGroups?: IeltsQuestionGroup[];
  writingTask?: IeltsWritingTaskData;
  speakingTask?: IeltsSpeakingTaskData;
  vocabularyNotes?: IeltsVocabularyNote[];
  userAnswers?: Record<number | string, string>;
  score?: IeltsScoreResult;
}

export function isIeltsExerciseData(data: unknown): data is IeltsExerciseData {
  if (!data || typeof data !== "object") return false;
  const obj = data as Record<string, unknown>;
  const validSkills = ["reading", "listening", "writing", "speaking"];
  return (
    typeof obj.title === "string" &&
    typeof obj.skill === "string" &&
    validSkills.includes(obj.skill) &&
    (Array.isArray(obj.questionGroups) || Boolean(obj.writingTask) || Boolean(obj.speakingTask))
  );
}

export function estimateIeltsBand(correct: number, total: number): string {
  if (total === 0) return "N/A";
  const ratio = correct / total;
  if (ratio >= 0.9) return "Band 8.5–9.0";
  if (ratio >= 0.82) return "Band 8.0";
  if (ratio >= 0.75) return "Band 7.5";
  if (ratio >= 0.67) return "Band 7.0";
  if (ratio >= 0.58) return "Band 6.5";
  if (ratio >= 0.5) return "Band 6.0";
  if (ratio >= 0.4) return "Band 5.5";
  return "Band 5.0 or below";
}
