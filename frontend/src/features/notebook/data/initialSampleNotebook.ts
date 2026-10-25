import type { JupyterNotebookDoc } from "../types/notebook.ts";

export const sampleNotebook: JupyterNotebookDoc = {
  id: "ielts-notebook-01",
  title: "IELTS_Workbench.ipynb",
  cells: [
    {
      id: "cell-listening-1",
      executionCount: null,
      cellType: "listening",
      source: `### Listening — Sample Notes

The audio player on the right is loaded with a demo tone. Attach your own practice recording to get started.`,
      resource: {
        type: "audio",
        url: "https://actions.google.com/sounds/v1/science/sonar_ping.ogg",
        name: "Audio demo — sonar (not an IELTS test)",
      },
    },
    {
      id: "cell-writing-1",
      executionCount: null,
      cellType: "writing",
      source: `### Task 1: Report Draft`,
      resource: {
        type: "text",
        name: "Task1_Prompt_&_Data.txt",
        textContent: `[IELTS WRITING TASK 1 - PROMPT & DATA]
Topic: The chart below shows the adoption rate and yield output of autonomous agricultural technology from 2015 to 2024.

Key Figures:
- 2015: 12% adoption, conventional yields baseline.
- 2019: 38% adoption, 15% increase in crop resilience.
- 2024: 74% adoption, 42% reduction in water usage.

Requirement: Summarize the information by selecting and reporting the main features, and make comparisons where relevant. Write at least 150 words.`,
      },
    },
    {
      id: "cell-reading-1",
      executionCount: null,
      cellType: "reading",
      source: `### Reading Answers & Vocabulary Notes`,
      resource: {
        type: "text",
        name: "Passage_1_Robotic_Machinery.txt",
        textContent: `[READING PASSAGE 1]
The integration of autonomous robotic machinery into agricultural production, which was once dismissed by conventional farmers as financially unfeasible, has remarkably transformed rural yields over the past decade.

Initial attempts faced widespread skepticism due to exorbitant maintenance overheads and unpredictable software calibration under adverse weather conditions. However, subsequent iterations featuring modular hardware and automated telemetry steadily mitigated these concerns.

Furthermore, environmental scientists emphasize that automated drip irrigation significantly reduces freshwater consumption by precisely targeting root systems rather than saturating entire fields.`,
      },
    },
    {
      id: "cell-speaking-1",
      executionCount: null,
      cellType: "speaking",
      source: `### Speaking Part 2 — 1-Minute Prep Notes`,
      resource: {
        type: "voice_recorder",
        name: "Speaking_Voice_Studio",
      },
    },
  ],
};
