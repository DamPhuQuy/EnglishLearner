import type { JupyterNotebookDoc } from '../types/notebook.ts';

export const sampleNotebook: JupyterNotebookDoc = {
  id: 'ielts-notebook-01',
  title: 'IELTS_Workbench.ipynb',
  cells: [
    {
      id: 'cell-listening-1',
      executionCount: 1,
      cellType: 'listening',
      source: `### Listening — Ghi chú mẫu

Âm thanh bên cạnh chỉ dùng thử player. Đính kèm bài nghe của bạn để luyện tập.

1. [Điền từ 1]: unprecedented
2. [Điền từ 2]: mitigate

> Ghi chú âm nuốt/nối âm:
- "placed an" ➔ phát âm lướt thành /pleɪst-ən/
- "turning to" ➔ /tɜːrnɪŋ-tə/`,
      resource: {
        type: 'audio',
        url: 'https://actions.google.com/sounds/v1/science/sonar_ping.ogg',
        name: 'Âm thanh demo — sonar (không phải bài IELTS)'
      }
    },
    {
      id: 'cell-writing-1',
      executionCount: 2,
      cellType: 'writing',
      source: `### Task 1: Report Draft

The provided visual data illustrates the trajectory of agricultural yields following the introduction of autonomous irrigation machinery.

Overall, it is evident that initial skepticism in 2015 was steadily replaced by substantial productivity gains across all surveyed regions.

Specifically, automated drip irrigation drastically curtailed freshwater consumption...`,
      resource: {
        type: 'text',
        name: 'Task1_Prompt_&_Data.txt',
        textContent: `[IELTS WRITING TASK 1 - PROMPT & DATA]
Topic: The chart below shows the adoption rate and yield output of autonomous agricultural technology from 2015 to 2024.

Key Figures:
- 2015: 12% adoption, conventional yields baseline.
- 2019: 38% adoption, 15% increase in crop resilience.
- 2024: 74% adoption, 42% reduction in water usage.

Requirement: Summarize the information by selecting and reporting the main features, and make comparisons where relevant. Write at least 150 words.`
      }
    },
    {
      id: 'cell-reading-1',
      executionCount: 3,
      cellType: 'reading',
      source: `### Reading Answers & Vocabulary Notes

1. Question 1: FALSE (Đoạn 1 khẳng định ban đầu nông dân hoài nghi và coi là bất khả thi)
2. Question 2: TRUE (Đoạn 2 nhấn mạnh giảm tiêu thụ nước ngọt)
3. Question 3: NOT GIVEN

*Vocabulary cần nhớ:*
- financially unfeasible = về mặt tài chính là không khả thi
- precisely targeting = nhắm mục tiêu chính xác`,
      resource: {
        type: 'text',
        name: 'Passage_1_Robotic_Machinery.txt',
        textContent: `[READING PASSAGE 1]
The integration of autonomous robotic machinery into agricultural production, which was once dismissed by conventional farmers as financially unfeasible, has remarkably transformed rural yields over the past decade. 

Initial attempts faced widespread skepticism due to exorbitant maintenance overheads and unpredictable software calibration under adverse weather conditions. However, subsequent iterations featuring modular hardware and automated telemetry steadily mitigated these concerns.

Furthermore, environmental scientists emphasize that automated drip irrigation significantly reduces freshwater consumption by precisely targeting root systems rather than saturating entire fields.`
      }
    },
    {
      id: 'cell-speaking-1',
      executionCount: 4,
      cellType: 'speaking',
      source: `### Speaking Part 2 — Dàn ý 1 phút (Prep Notes)

- Device: My daily code editor & terminal environment
- Usage frequency: 8–10 hours per day across various software tasks
- Core advantages:
  * Eliminates mental friction with instant syntax validation
  * Minimizes cognitive overhead through keyboard shortcuts
- Conclusion: Without it, work would be painfully slow and error-prone.`,
      resource: {
        type: 'voice_recorder',
        name: 'Speaking_Voice_Studio'
      }
    }
  ]
};
