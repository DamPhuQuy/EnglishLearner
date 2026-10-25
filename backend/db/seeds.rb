# db/seeds.rb
# Seeds the database with the default sample notebook

sample_cells = [
  {
    id: "cell-listening-1",
    executionCount: nil,
    cellType: "listening",
    source: "### Listening — Sample Notes\n\nThe audio player on the right is loaded with a demo tone. Attach your own practice recording to get started.",
    resource: {
      type: "audio",
      url: "https://actions.google.com/sounds/v1/science/sonar_ping.ogg",
      name: "Audio demo — sonar (not an IELTS test)"
    }
  },
  {
    id: "cell-writing-1",
    executionCount: nil,
    cellType: "writing",
    source: "### Task 1: Report Draft",
    resource: {
      type: "text",
      name: "Task1_Prompt_&_Data.txt",
      textContent: "[IELTS WRITING TASK 1 - PROMPT & DATA]\nTopic: The chart below shows the adoption rate and yield output of autonomous agricultural technology from 2015 to 2024.\n\nKey Figures:\n- 2015: 12% adoption, conventional yields baseline.\n- 2019: 38% adoption, 15% increase in crop resilience.\n- 2024: 74% adoption, 42% reduction in water usage.\n\nRequirement: Summarize the information by selecting and reporting the main features, and make comparisons where relevant. Write at least 150 words."
    }
  },
  {
    id: "cell-reading-1",
    executionCount: nil,
    cellType: "reading",
    source: "### Reading Answers & Vocabulary Notes",
    resource: {
      type: "text",
      name: "Passage_1_Robotic_Machinery.txt",
      textContent: "[READING PASSAGE 1]\nThe integration of autonomous robotic machinery into agricultural production, which was once dismissed by conventional farmers as financially unfeasible, has remarkably transformed rural yields over the past decade.\n\nInitial attempts faced widespread skepticism due to exorbitant maintenance overheads and unpredictable software calibration under adverse weather conditions. However, subsequent iterations featuring modular hardware and automated telemetry steadily mitigated these concerns.\n\nFurthermore, environmental scientists emphasize that automated drip irrigation significantly reduces freshwater consumption by precisely targeting root systems rather than saturating entire fields."
    }
  },
  {
    id: "cell-speaking-1",
    executionCount: nil,
    cellType: "speaking",
    source: "### Speaking Part 2 — 1-Minute Prep Notes",
    resource: {
      type: "voice_recorder",
      name: "Speaking_Voice_Studio"
    }
  }
]

notebook = Notebook.find_or_initialize_by(id: "ielts-notebook-01")
notebook.title = "IELTS_Workbench.ipynb"
notebook.save!
notebook.sync_cells!(sample_cells, reason: "initial_seed")

puts "Seeded notebook #{notebook.id} with #{notebook.cells.count} cells."
