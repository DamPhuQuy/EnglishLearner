-- Initial Sample Data for Mini-IELTS Cells
INSERT OR IGNORE INTO notebooks (id, title, description, created_at, updated_at)
VALUES (
  'default-ielts-notebook',
  'IELTS Mini Practice Tests',
  'Comprehensive IELTS practice notebook organized into bite-sized Mini-IELTS test cells.',
  datetime('now'),
  datetime('now')
);

INSERT OR IGNORE INTO cells (id, notebook_id, position, cell_type, execution_count, source, resource_type, resource_url, resource_name, resource_text_content, created_at, updated_at)
VALUES 
(
  'cell-listening-1',
  'default-ielts-notebook',
  0,
  'listening',
  NULL,
  '### Mini-IELTS Listening: Section 1
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
- *Weak forms*: "for a" -> /fərə/',
  'audio',
  'https://actions.google.com/sounds/v1/science/sonar_ping.ogg',
  'Listening_Section1_Registration.mp3',
  NULL,
  datetime('now'),
  datetime('now')
),
(
  'cell-reading-1',
  'default-ielts-notebook',
  1,
  'reading',
  NULL,
  '### Mini-IELTS Reading: Passage 1 Questions
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
- *Exorbitant* (adj): Unreasonably high or costly.',
  'text',
  NULL,
  'Passage_1_Robotic_Machinery.txt',
  '[READING PASSAGE 1: The Automation of Modern Agriculture]

[A] The integration of autonomous robotic machinery into agricultural production, which was once dismissed by conventional farmers as financially unfeasible, has remarkably transformed rural yields over the past decade. Where early twentieth-century agriculture depended on heavy machinery operated exclusively by manual laborers, modern farming embraces unmanned aerial scouting and autonomous soil sensors.

[B] Initial attempts faced widespread skepticism due to exorbitant maintenance overheads and unpredictable software calibration under adverse weather conditions. However, subsequent iterations featuring modular hardware and automated telemetry steadily mitigated these concerns, lowering replacement downtime from weeks to hours.

[C] Furthermore, environmental scientists emphasize that automated drip irrigation significantly reduces freshwater consumption by precisely targeting root systems rather than saturating entire fields. Sensor networks track soil humidity in real-time, delivering micro-doses of mineral nutrients alongside water.

[D] In conclusion, autonomous farming presents a vital paradigm shift toward sustainable food security, balancing high yields with eco-friendly resource conservation.',
  datetime('now'),
  datetime('now')
),
(
  'cell-writing-1',
  'default-ielts-notebook',
  2,
  'writing',
  NULL,
  '### Mini-IELTS Writing Task 1: Model Draft & Notes

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

The trend culminated in 2024, when adoption reached 74%. This widespread utilization yielded an impressive 42% decrease in agricultural water usage compared to conventional techniques, underscoring the ecological viability of smart farming.',
  'text',
  NULL,
  'Task1_Autonomous_Agriculture_Prompt.txt',
  '[IELTS WRITING TASK 1 - PROMPT & DATA SPECIFICATION]

Topic: The chart and report below summarize the adoption rate and operational yield output of autonomous agricultural machinery between 2015 and 2024.

Key Figures:
• 2015: 12% adoption rate; crop yields at conventional baseline.
• 2019: 38% adoption rate; +15% increase in crop resilience.
• 2024: 74% adoption rate; 42% reduction in freshwater usage.

Instructions: Summarize the information by selecting and reporting the main features, and make comparisons where relevant. Write at least 150 words.',
  datetime('now'),
  datetime('now')
),
(
  'cell-speaking-1',
  'default-ielts-notebook',
  3,
  'speaking',
  NULL,
  '### Mini-IELTS Speaking: Part 2 Cue Card

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
- [x] Pronunciation: Clear syllable stress on technical terms.',
  'voice_recorder',
  NULL,
  'Speaking_CueCard_Part2_Technology',
  NULL,
  datetime('now'),
  datetime('now')
);
