import type { IeltsSkill } from "../types/ieltsSchema.ts";

export const IELTS_AI_PROMPT_READING = `You are an expert Cambridge IELTS Reading test creator.
Generate an authentic IELTS Reading exercise according to the STRICT JSON schema below.

### REQUIREMENTS:
1. Return ONLY valid, raw JSON (no surrounding markdown code blocks, no intro/outro).
2. "material.content" must provide a rich academic passage (500–800 words) with paragraph markers [A], [B], [C], [D], [E]...
3. Include 2–3 questionGroups chosen from:
   - "true_false_not_given" or "yes_no_not_given"
   - "multiple_choice"
   - "sentence_completion" / "summary_completion" (with "prefix", "suffix", "answer", "acceptedAnswers")
   - "matching_headings" (with "headingsList": [{"id": "i", "heading": "..."}], and questions mapping paragraph "A" -> answer "iii")
   - "matching_information" (Which paragraph contains: statement -> answer "B")
   - "matching_features" (with "featuresList": [{"key": "A", "name": "..."}], statement -> answer "A")
4. Every question must have:
   - "questionNumber" (consecutive 1, 2, 3...)
   - "answer" (exact answer string)
   - "explanation" (clear rationale quoting the passage)
   - "paragraphRef" (e.g. "Paragraph B")

### JSON FORMAT:
{
  "version": "1.0",
  "skill": "reading",
  "title": "Passage 1: The Secrets of Animal Navigation",
  "topic": "Biology & Animal Behavior",
  "difficulty": "Band 6.5–7.5",
  "timeLimitMinutes": 20,
  "material": {
    "type": "text",
    "title": "The Secrets of Animal Navigation",
    "content": "[A] For centuries, scientists have marveled at how migratory birds travel thousands of miles...\\n\\n[B] Recent investigations reveal that magnetite crystals in birds' beaks act as biological compasses..."
  },
  "questionGroups": [
    {
      "id": "g1",
      "type": "true_false_not_given",
      "title": "Questions 1–3: True / False / Not Given",
      "instruction": "Do the following statements agree with the information in the reading passage? Write TRUE, FALSE, or NOT GIVEN.",
      "questions": [
        {
          "questionNumber": 1,
          "statement": "Scientists initially believed birds navigated solely by celestial cues.",
          "answer": "FALSE",
          "explanation": "Paragraph A states scientists were puzzled rather than committed to a single belief.",
          "paragraphRef": "Paragraph A"
        }
      ]
    },
    {
      "id": "g2",
      "type": "sentence_completion",
      "title": "Questions 4–6: Summary Completion",
      "instruction": "Complete the sentences below. Choose NO MORE THAN TWO WORDS from the passage for each answer.",
      "wordLimitRule": "NO MORE THAN TWO WORDS",
      "questions": [
        {
          "questionNumber": 4,
          "prefix": "Microscopic",
          "suffix": "found within beaks serve as natural navigational tools.",
          "answer": "magnetite crystals",
          "acceptedAnswers": ["magnetite crystals", "crystals"],
          "explanation": "Paragraph B specifically notes 'magnetite crystals in birds beaks'.",
          "paragraphRef": "Paragraph B"
        }
      ]
    }
  ],
  "vocabularyNotes": [
    { "word": "celestial", "type": "adj", "definition": "Relating to the sky or outer space.", "example": "celestial cues" }
  ]
}`;

export const IELTS_AI_PROMPT_LISTENING = `You are an expert Cambridge IELTS Listening test creator.
Generate an authentic IELTS Listening exercise according to the STRICT JSON schema below.

### REQUIREMENTS:
1. Return ONLY valid, raw JSON.
2. In "material":
   - "type": "audio"
   - "title": Section title (e.g. "Section 1: Community Sports Club Enquiry")
   - "audioTranscript": Full script dialogue between speakers with clear speaker tags.
3. Include question groups such as:
   - "note_completion" / "form_completion" / "table_completion"
   - "multiple_choice"
   - "plan_map_diagram_labelling"
4. Questions must follow the audio sequence sequentially.

### JSON FORMAT:
{
  "version": "1.0",
  "skill": "listening",
  "title": "Listening Section 1: Hotel Conference Booking",
  "difficulty": "Band 6.0–7.0",
  "timeLimitMinutes": 10,
  "material": {
    "type": "audio",
    "title": "Section 1 Dialogue",
    "audioTranscript": "Agent: Good morning, Grand Plaza Hotel. How can I assist you?\\nCaller: Hello, I would like to book a conference room for the 22nd of November..."
  },
  "questionGroups": [
    {
      "id": "g1",
      "type": "note_completion",
      "title": "Questions 1–5: Complete the booking form below",
      "instruction": "Write NO MORE THAN TWO WORDS AND/OR A NUMBER for each answer.",
      "wordLimitRule": "NO MORE THAN TWO WORDS AND/OR A NUMBER",
      "questions": [
        {
          "questionNumber": 1,
          "prefix": "Event date: 22nd",
          "suffix": "",
          "answer": "November",
          "acceptedAnswers": ["November"],
          "explanation": "Caller asks to book a room for the 22nd of November."
        }
      ]
    }
  ]
}`;

export const IELTS_AI_PROMPT_WRITING = `You are an expert Cambridge IELTS Writing test creator.
Generate an authentic IELTS Writing Task 1 or Task 2 exercise according to the STRICT JSON schema below.

### REQUIREMENTS:
1. Return ONLY valid, raw JSON.
2. Choose "taskType": "task1_academic" | "task1_general" | "task2".
3. For Task 1 Academic: Provide "academicVisualType" (bar_chart, line_graph, pie_chart, table, map_plan, process_diagram) and specify data in "keyDataPoints" and "material.imageDescription".
4. For Task 2: Provide "essayCategory" (agree_disagree, discuss_both_views, advantages_outweigh, causes_solutions) with instructions.
5. Provide a high-scoring "sampleEssay" (Band 8.0+) with band rubric highlights.

### JSON FORMAT:
{
  "version": "1.0",
  "skill": "writing",
  "title": "Writing Task 1: Autonomous Agriculture Trends",
  "difficulty": "Academic Band 7.0+",
  "writingTask": {
    "taskType": "task1_academic",
    "academicVisualType": "line_graph",
    "prompt": "The graph below shows the adoption rate and water conservation metrics of precision agriculture between 2015 and 2024. Summarise the information by selecting and reporting the main features, and make comparisons where relevant.",
    "minWords": 150,
    "timeSuggestedMinutes": 20,
    "keyDataPoints": [
      "2015: 12% adoption baseline",
      "2019: 38% adoption (+15% crop resilience)",
      "2024: 74% adoption (42% water conservation)"
    ],
    "sampleEssay": "The line graph delineates the progressive uptake of precision agricultural machinery...",
    "sampleExaminerBand": "Band 8.5"
  }
}`;

export const IELTS_AI_PROMPT_SPEAKING = `You are an expert Cambridge IELTS Speaking test creator.
Generate an authentic IELTS Speaking Part 1, Part 2, or Part 3 exercise according to the STRICT JSON schema below.

### REQUIREMENTS:
1. Return ONLY valid, raw JSON.
2. Choose "part": 1 | 2 | 3.
3. For Part 2: Include "cueCard" with "title" (Describe a...), 3–4 "bulletPoints" (You should say: What, When, Where, Why), and a "roundingOffQuestion".
4. Include "recommendedIdioms" with phrases, meanings, and practical example usages.

### JSON FORMAT:
{
  "version": "1.0",
  "skill": "speaking",
  "title": "Speaking Part 2: A Time You Solved a Difficult Problem",
  "difficulty": "Band 7.0+",
  "speakingTask": {
    "part": 2,
    "topic": "Problem Solving & Innovation",
    "cueCard": {
      "title": "Describe a challenging problem you successfully resolved",
      "bulletPoints": [
        "What the problem was and when it occurred",
        "Who was involved in the situation",
        "What steps you took to overcome it",
        "And explain why you felt proud of the resolution"
      ],
      "roundingOffQuestion": "Do you often encounter similar issues?"
    },
    "part3Questions": [
      { "questionNumber": 1, "question": "What qualities make an effective problem solver in the workplace?" },
      { "questionNumber": 2, "question": "Should schools place greater emphasis on teaching critical thinking?" }
    ],
    "recommendedIdioms": [
      { "phrase": "think on one's feet", "meaning": "To make quick, wise decisions without preparation", "example": "I had to think on my feet when the projector failed." }
    ]
  }
}`;

export function getIeltsAiPrompt(skill: IeltsSkill = "reading"): string {
  switch (skill) {
    case "listening":
      return IELTS_AI_PROMPT_LISTENING;
    case "writing":
      return IELTS_AI_PROMPT_WRITING;
    case "speaking":
      return IELTS_AI_PROMPT_SPEAKING;
    case "reading":
    default:
      return IELTS_AI_PROMPT_READING;
  }
}

export const IELTS_AI_PROMPT_TEMPLATE = IELTS_AI_PROMPT_READING;
