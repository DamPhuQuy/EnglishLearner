import type { CellResource, SkillType } from "../../notebook/types/notebook.ts";
import type { IeltsExerciseData } from "../types/ieltsSchema.ts";

export const SKILL_NAMES: Record<SkillType, string> = {
  listening: "Listening (Mini-IELTS)",
  reading: "Reading (Mini-IELTS)",
  writing: "Writing (Mini-IELTS)",
  speaking: "Speaking (Mini-IELTS)",
  markdown: "Notes / Vocab",
};

export const SKILL_RESOURCE_LABELS: Record<SkillType, string> = {
  listening: "Audio Track & Script",
  reading: "Reading Passage",
  writing: "Prompt & Data Chart",
  speaking: "Voice Studio & Cue Card",
  markdown: "Attached Document",
};

export const SKILL_TEMPLATES: Record<SkillType, string> = {
  listening: `### Mini-IELTS Listening: Section Practice
**Questions 1–6: Complete the notes below.**
*Write NO MORE THAN TWO WORDS AND/OR A NUMBER for each answer.*

1. Guest Surname: [Q1] ________
2. Room preference: [Q2] ________ with sea view
3. Check-in Date: [Q3] 14th ________
4. Contact Number: [Q4] 07946 ________
5. Breakfast choice: [Q5] ________ option
6. Special request: Late check-out at [Q6] ________ AM

---
### Questions 7–10: Multiple Choice
7. The conference starts at: [Q7] (A / B / C)
8. Transport from the airport is: [Q8] (A / B / C)

---
### Vocabulary & Connected Speech Notes
- *Connected speech*:
- *Distractor note*:`,

  reading: `### Mini-IELTS Reading: Passage Practice
**Questions 1–4: True / False / Not Given**
*Do the following statements agree with the information in the text?*

1. Statement 1 -> [Q1] ________
2. Statement 2 -> [Q2] ________
3. Statement 3 -> [Q3] ________
4. Statement 4 -> [Q4] ________

---
### Questions 5–8: Summary Completion
*Choose ONE WORD ONLY from the passage for each answer.*

The researchers noted that (5) [Q5] ________ was the principal factor influencing outcomes. Additionally, the team utilized (6) [Q6] ________ to monitor fluctuations over time.

---
### Text Evidence & Vocabulary Bank
> Quote: "..."
- *Academic term*: `,

  writing: `### Mini-IELTS Writing Practice

### Overview & Structure Plan
- **Introduction**: Paraphrase the prompt & state the main subject.
- **Overview**: Highlight 2 major trends / contrasting features.
- **Body 1**: Key group / timeframe 1 with specific data.
- **Body 2**: Key group / timeframe 2 with comparisons.

---
### Essay Draft
[Write your essay here. Aim for 150+ words (Task 1) or 250+ words (Task 2)]

---
### Band Criteria Checklist
- [ ] Task Achievement / Response
- [ ] Coherence & Cohesion (logical flow & linking)
- [ ] Lexical Resource (collocations & precision)
- [ ] Grammatical Range & Accuracy`,

  speaking: `### Mini-IELTS Speaking: Part 2 Cue Card

### 1-Minute Preparation Notes
- **What**: 
- **When & Where**: 
- **Who with**: 
- **Why it is memorable / significant**: 

---
### Idioms & Collocations
- 
- 

---
### Self-Reflection Rubric
- [ ] Fluency & Coherence: Continuous flow, minimal hesitation
- [ ] Lexical Resource: Natural idioms and range
- [ ] Grammatical Accuracy: Variety of tenses and conditionals
- [ ] Pronunciation: Intonation and word stress`,

  markdown: `### Vocabulary & Grammar Notes

| Word / Collocation | Meaning & Context | Example Sentence |
| :--- | :--- | :--- |
| | | |

### Grammar Focus
- 
`,
};

export interface MiniIeltsPreset {
  id: string;
  skill: SkillType;
  title: string;
  source: string;
  resource: CellResource;
  structuredData?: IeltsExerciseData;
}

export const MINI_IELTS_PRESETS: MiniIeltsPreset[] = [
  {
    id: "listening-section1",
    skill: "listening",
    title: "Mini-IELTS Listening: Hotel Booking (Section 1)",
    source: `### Mini-IELTS Listening: Section 1
**Questions 1–6: Complete the notes below.**
*Write NO MORE THAN TWO WORDS AND/OR A NUMBER for each answer.*

1. Guest Surname: [Q1] ________
2. Room preference: [Q2] ________ with sea view
3. Check-in Date: [Q3] 14th ________
4. Contact Number: [Q4] 07946 ________
5. Breakfast choice: [Q5] ________ option
6. Special request: Late check-out at [Q6] ________ AM

---
### Vocabulary & Connected Speech Notes
- *En-suite* (/ɒn ˈswiːt/): bathroom directly connected to the bedroom.
- *Weak forms*: "for a" -> /fərə/`,
    resource: {
      type: "audio",
      url: "/audio/listening/section1_homestay_booking.mp3",
      name: "Listening_Section1_Registration_demo.mp3",
      textContent: `[Audio Transcript - Section 1: Hotel Room Booking]
[Receptionist]: Good morning, Seaside Grand Hotel reservations. How can I help you today?
[Guest]: Hello, I would like to make a room reservation for next month please.
[Receptionist]: Certainly, madam. May I take your surname first?
[Guest]: Yes, it is Thornton. That is spelled T-H-O-R-N-T-O-N.
[Receptionist]: Thank you, Mrs. Thornton. And what type of room would you prefer?
[Guest]: We would love a double room, preferably on an upper floor with a sea view.
[Receptionist]: A double room with sea view, perfect. What is your intended check-in date?
[Guest]: We plan to arrive on the 14th of August.
[Receptionist]: 14th of August, excellent. And could I take a daytime contact number?
[Guest]: Yes, it's 07946 882910.
[Receptionist]: 07946 882910. And regarding your breakfast arrangements?
[Guest]: We would like the continental breakfast option included, please.
[Receptionist]: Wonderful. Do you have any special requirements for your stay?
[Guest]: Yes, our return flight isn't until the evening, so could we arrange a late check-out at 11:30 AM?
[Receptionist]: Certainly, I have added late check-out at 11:30 AM to your booking notes.`,
    },
    structuredData: {
      version: "1.0",
      skill: "listening",
      title: "Mini-IELTS Listening: Hotel Room Booking (Section 1)",
      topic: "Accommodation & Hospitality",
      difficulty: "Band 5.0–5.5",
      timeLimitMinutes: 10,
      material: {
        type: "audio",
        title: "Listening Audio Track: Hotel Booking",
        audioUrl: "/audio/listening/section1_homestay_booking.mp3",
        audioTranscript: `[Audio Transcript - Section 1: Hotel Room Booking]
[Receptionist]: Good morning, Seaside Grand Hotel reservations. How can I help you today?
[Guest]: Hello, I would like to make a room reservation for next month please.
[Receptionist]: Certainly, madam. May I take your surname first?
[Guest]: Yes, it is Thornton. That is spelled T-H-O-R-N-T-O-N.
[Receptionist]: Thank you, Mrs. Thornton. And what type of room would you prefer?
[Guest]: We would love a double room, preferably on an upper floor with a sea view.
[Receptionist]: A double room with sea view, perfect. What is your intended check-in date?
[Guest]: We plan to arrive on the 14th of August.
[Receptionist]: 14th of August, excellent. And could I take a daytime contact number?
[Guest]: Yes, it's 07946 882910.
[Receptionist]: 07946 882910. And regarding your breakfast arrangements?
[Guest]: We would like the continental breakfast option included, please.
[Receptionist]: Wonderful. Do you have any special requirements for your stay?
[Guest]: Yes, our return flight isn't until the evening, so could we arrange a late check-out at 11:30 AM?
[Receptionist]: Certainly, I have added late check-out at 11:30 AM to your booking notes.`,
      },
      questionGroups: [
        {
          id: "qg-hotel-notes",
          type: "note_completion",
          title: "Section 1: Hotel Booking Notes",
          instruction: "Complete the notes below. Write NO MORE THAN TWO WORDS AND/OR A NUMBER for each answer.",
          wordLimitRule: "NO MORE THAN TWO WORDS AND/OR A NUMBER",
          questions: [
            {
              questionNumber: 1,
              statement: "1. Guest Surname: [Q1]",
              answer: "Thornton",
              explanation: "Receptionist asks for surname, guest confirms: 'Thornton. That is spelled T-H-O-R-N-T-O-N.'",
            },
            {
              questionNumber: 2,
              statement: "2. Room preference: [Q2] with sea view",
              answer: "double room",
              acceptedAnswers: ["double", "double room"],
              explanation: "Guest states: 'We would love a double room, preferably on an upper floor with a sea view.'",
            },
            {
              questionNumber: 3,
              statement: "3. Check-in Date: 14th [Q3]",
              answer: "August",
              explanation: "Guest says: 'We plan to arrive on the 14th of August.'",
            },
            {
              questionNumber: 4,
              statement: "4. Contact Number: 07946 [Q4]",
              answer: "882910",
              explanation: "Guest says: 'Yes, it is 07946 882910.'",
            },
            {
              questionNumber: 5,
              statement: "5. Breakfast choice: [Q5] option",
              answer: "continental",
              explanation: "Guest states: 'We would like the continental breakfast option included.'",
            },
            {
              questionNumber: 6,
              statement: "6. Special request: Late check-out at [Q6] AM",
              answer: "11:30",
              acceptedAnswers: ["11:30", "11.30"],
              explanation: "Guest asks for: 'late check-out at 11:30 AM.'",
            },
          ],
        },
      ],
    },
  },
  {
    id: "reading-passage1",
    skill: "reading",
    title: "Mini-IELTS Reading: Automation of Agriculture (Passage 1)",
    source: `### Mini-IELTS Reading: Passage 1 Questions
**Questions 1–4: Do the following statements agree with the information in the text?**
*Write TRUE, FALSE, or NOT GIVEN.*

1. Traditional agriculturalists immediately welcomed automated tractors. -> [Q1] FALSE
2. High maintenance costs were an early obstacle to adopting robotic tools. -> [Q2] TRUE
3. Automated drip irrigation requires more water than overhead sprayers. -> [Q3] FALSE
4. European governments funded the majority of early telemetry research. -> [Q4] NOT GIVEN

---
### Questions 5–7: Complete the summary below
*Choose ONE WORD ONLY from the passage for each answer.*

Subsequent machinery models reduced operational hurdles by implementing (5) [Q5] ________ hardware components and automated telemetry systems. Furthermore, precision drip systems conserve water by concentrating on root systems rather than irrigating whole (6) [Q6] ________.

---
### Key Lexical Resource
- *Mitigate* (v): To make something less severe or harmful.
- *Exorbitant* (adj): Unreasonably high or costly.`,
    resource: {
      type: "text",
      name: "Passage_1_Robotic_Machinery.txt",
      textContent: `[READING PASSAGE 1: The Automation of Modern Agriculture]

[A] The integration of autonomous robotic machinery into agricultural production, which was once dismissed by conventional farmers as financially unfeasible, has remarkably transformed rural yields over the past decade. Where early twentieth-century agriculture depended on heavy machinery operated exclusively by manual laborers, modern farming embraces unmanned aerial scouting and autonomous soil sensors.

[B] Initial attempts faced widespread skepticism due to exorbitant maintenance overheads and unpredictable software calibration under adverse weather conditions. However, subsequent iterations featuring modular hardware and automated telemetry steadily mitigated these concerns, lowering replacement downtime from weeks to hours.

[C] Furthermore, environmental scientists emphasize that automated drip irrigation significantly reduces freshwater consumption by precisely targeting root systems rather than saturating entire fields. Sensor networks track soil humidity in real-time, delivering micro-doses of mineral nutrients alongside water.

[D] In conclusion, autonomous farming presents a vital paradigm shift toward sustainable food security, balancing high yields with eco-friendly resource conservation.`,
    },
    structuredData: {
      version: "1.0",
      skill: "reading",
      title: "Mini-IELTS Reading: Automation of Agriculture",
      topic: "Agriculture & Technology",
      difficulty: "Band 6.5–7.5",
      timeLimitMinutes: 20,
      material: {
        type: "text",
        title: "Passage 1: The Automation of Modern Agriculture",
        content: `[READING PASSAGE 1: The Automation of Modern Agriculture]

[A] The integration of autonomous robotic machinery into agricultural production, which was once dismissed by conventional farmers as financially unfeasible, has remarkably transformed rural yields over the past decade.

[B] Initial attempts faced widespread skepticism due to exorbitant maintenance overheads and unpredictable software calibration under adverse weather conditions. However, subsequent iterations featuring modular hardware and automated telemetry steadily mitigated these concerns, lowering replacement downtime from weeks to hours.

[C] Furthermore, environmental scientists emphasize that automated drip irrigation significantly reduces freshwater consumption by precisely targeting root systems rather than saturating entire fields.

[D] In conclusion, autonomous farming presents a vital paradigm shift toward sustainable food security, balancing high yields with eco-friendly resource conservation.`,
      },
      questionGroups: [
        {
          id: "g1",
          type: "true_false_not_given",
          title: "Questions 1–4: True / False / Not Given",
          instruction:
            "Do the following statements agree with the information in the text? Choose TRUE, FALSE, or NOT GIVEN.",
          questions: [
            {
              questionNumber: 1,
              statement:
                "Traditional agriculturalists immediately welcomed automated tractors.",
              answer: "FALSE",
              explanation:
                "Paragraph A states it was 'dismissed by conventional farmers as financially unfeasible'.",
            },
            {
              questionNumber: 2,
              statement:
                "High maintenance costs were an early obstacle to adopting robotic tools.",
              answer: "TRUE",
              explanation:
                "Paragraph B states initial attempts faced skepticism due to 'exorbitant maintenance overheads'.",
            },
            {
              questionNumber: 3,
              statement:
                "Automated drip irrigation requires more water than overhead sprayers.",
              answer: "FALSE",
              explanation:
                "Paragraph C states automated drip irrigation significantly reduces freshwater consumption.",
            },
            {
              questionNumber: 4,
              statement:
                "European governments funded the majority of early telemetry research.",
              answer: "NOT GIVEN",
              explanation:
                "The text mentions telemetry research, but never mentions European government funding.",
            },
          ],
        },
        {
          id: "g2",
          type: "sentence_completion",
          title: "Questions 5–6: Summary Completion",
          instruction:
            "Complete the summary below. Choose ONE WORD ONLY from the passage for each answer.",
          questions: [
            {
              questionNumber: 5,
              prefix:
                "Subsequent machinery models reduced operational hurdles by implementing",
              suffix: "hardware components and automated telemetry systems.",
              answer: "modular",
              acceptedAnswers: ["modular"],
              explanation:
                "Paragraph B specifies: 'subsequent iterations featuring modular hardware'.",
            },
            {
              questionNumber: 6,
              prefix:
                "Furthermore, precision drip systems conserve water by concentrating on root systems rather than irrigating whole",
              suffix: ".",
              answer: "fields",
              acceptedAnswers: ["fields"],
              explanation:
                "Paragraph C specifies: 'targeting root systems rather than saturating entire fields'.",
            },
          ],
        },
      ],
      vocabularyNotes: [
        {
          word: "mitigate",
          type: "v",
          definition: "To make something less severe or harmful.",
          example: "steadily mitigated these concerns.",
        },
        {
          word: "exorbitant",
          type: "adj",
          definition: "Unreasonably high or costly.",
          example: "exorbitant maintenance overheads.",
        },
      ],
    },
  },
  {
    id: "writing-task1",
    skill: "writing",
    title: "Mini-IELTS Writing: Task 1 Report Draft",
    source: `### Mini-IELTS Writing Task 1: Model Draft & Notes

### Overview Plan
- **Introduction**: Paraphrase the prompt regarding autonomous agricultural adoption and crop resilience.
- **Overview**: Highlight significant upward trajectory in technology adoption alongside substantial reductions in water usage.
- **Body Paragraph 1**: 2015 baseline (12%) vs 2019 expansion (38%).
- **Body Paragraph 2**: 2024 peak (74%) and 42% water conservation achievement.

---
### Essay Draft
The provided data delineates the adoption rate and agricultural yield improvements associated with autonomous farming technology over a nine-year period from 2015 to 2024.

Overall, it is evident that autonomous equipment experienced significant uptake over the decade. Concurrently, environmental efficiency improved markedly, most notably through substantial reductions in water consumption.

In 2015, autonomous technology stood at a modest 12% adoption rate, with crop yields remaining at standard baseline levels. By 2019, adoption had more than tripled to 38%, accompanied by a notable 15% increase in crop resilience against extreme climatic conditions.

The trend culminated in 2024, when adoption reached 74%. This widespread utilization yielded an impressive 42% decrease in agricultural water usage compared to conventional techniques, underscoring the ecological viability of smart farming.`,
    resource: {
      type: "text",
      name: "Task1_Autonomous_Agriculture_Prompt.txt",
      textContent: `[IELTS WRITING TASK 1 - PROMPT & DATA SPECIFICATION]

Topic: The chart and report below summarize the adoption rate and operational yield output of autonomous agricultural machinery between 2015 and 2024.

Key Figures:
• 2015: 12% adoption rate; crop yields at conventional baseline.
• 2019: 38% adoption rate; +15% increase in crop resilience.
• 2024: 74% adoption rate; 42% reduction in freshwater usage.

Instructions: Summarize the information by selecting and reporting the main features, and make comparisons where relevant. Write at least 150 words.`,
    },
  },
  {
    id: "speaking-part2",
    skill: "speaking",
    title: "Mini-IELTS Speaking: Part 2 Cue Card",
    source: `### Mini-IELTS Speaking: Part 2 Cue Card

### 1-Minute Preparation Notes
- **What**: Autonomous soil moisture tester & smartphone plant diagnosis app.
- **When & Where**: Discovered during summer holiday at an agricultural research garden in 2023.
- **Why it matters**: Replaced guesswork with instant, accurate telemetry on soil nitrogen and hydration levels.
- **Key Idioms & Collocations**: "game changer", "cutting-edge innovation", "hands-on experience", "streamline efficiency".

---
### Self-Reflection & Examiner Rubric Checklist
- [x] Fluency & Coherence: Maintained continuous discourse for 2 minutes without protracted hesitation.
- [x] Lexical Resource: Deployed topic-specific vocabulary (telemetry, precision gardening, intuitive interface).
- [x] Grammatical Range: Utilized past continuous and conditional structures ("Had I not discovered it...").
- [x] Pronunciation: Clear syllable stress on technical terms.`,
    resource: {
      type: "voice_recorder",
      name: "Speaking_CueCard_Part2_Technology",
    },
  },
];

export function getSkillTemplate(skill: SkillType): string {
  return SKILL_TEMPLATES[skill] ?? "";
}

export function appendTemplateToSource(
  existingSource: string,
  skill: SkillType,
): string {
  const template = getSkillTemplate(skill);
  if (!existingSource.trim()) {
    return template;
  }
  return `${existingSource}\n\n${template}`;
}
