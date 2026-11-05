import {
  BookOpen,
  ChevronDown,
  ChevronUp,
  FileText,
  PenLine,
  Target,
} from "lucide-react";
import React, { useState } from "react";
import type { IeltsExerciseMaterial, IeltsWritingTaskData } from "../../types/ieltsSchema.ts";
import { AcademicVisualStimulus } from "./AcademicVisualStimulus.tsx";

export interface WritingPromptWorkspaceProps {
  writingTask: IeltsWritingTaskData;
  title: string;
  difficulty?: string;
  material?: IeltsExerciseMaterial;
}

export const WritingPromptWorkspace: React.FC<WritingPromptWorkspaceProps> = ({
  writingTask,
  title,
  difficulty,
  material,
}) => {
  const [showSampleEssay, setShowSampleEssay] = useState(false);

  const isTask1 = String(writingTask.taskType).includes("task1");
  const taskLabel = isTask1 ? "IELTS WRITING TASK 1" : "IELTS WRITING TASK 2";
  const subTypeLabel =
    writingTask.academicVisualType?.replace(/_/g, " ") ||
    writingTask.generalLetterType?.replace(/_/g, " ") ||
    writingTask.essayCategory?.replace(/_/g, " ") ||
    "Academic Writing";

  const bullets = writingTask.bulletPoints || writingTask.keyDataPoints || [];

  return (
    <div className="writing-resource-workspace">
      {/* Header bar */}
      <div className="writing-resource-header">
        <div className="writing-resource-badge">
          <PenLine size={13} />
          <span>{taskLabel}</span>
          <span className="writing-sub-badge">{subTypeLabel}</span>
        </div>
        <div className="writing-target-badge">
          <Target size={12} />
          <span>Target: {writingTask.minWords}+ words</span>
        </div>
      </div>

      {/* Title & Topic */}
      <div className="writing-resource-title-row">
        <h3 className="writing-resource-title">{title}</h3>
        {difficulty && <span className="writing-diff-tag">{difficulty}</span>}
      </div>

      {/* Main Task Prompt */}
      <div className="writing-prompt-card">
        <div className="prompt-card-label">
          <FileText size={13} />
          <span>Official Task Prompt:</span>
        </div>
        <p className="prompt-card-text">{writingTask.prompt}</p>
      </div>

      {/* Academic Visual Stimulus (Charts / Maps / Diagrams) */}
      {isTask1 && (writingTask.academicVisualType || material?.imageUrl) && (
        <AcademicVisualStimulus
          writingTask={writingTask}
          imageUrl={material?.imageUrl}
          imageDescription={material?.imageDescription}
        />
      )}

      {/* Key Data Highlights / Bullet Points */}
      {bullets.length > 0 && (
        <div className="writing-highlights-card">
          <span className="highlights-title">
            {isTask1 ? "Key Data Features & Trends:" : "Key Argument Dimensions:"}
          </span>
          <ul className="highlights-list">
            {bullets.map((pt, i) => (
              <li key={i} className="highlight-item">
                <span className="highlight-bullet">•</span>
                <span>{pt}</span>
              </li>
            ))}
          </ul>
        </div>
      )}

      {/* Model Essay Accordion */}
      {writingTask.sampleEssay && (
        <div className="writing-model-accordion">
          <button
            type="button"
            className="model-toggle-btn"
            onClick={() => setShowSampleEssay((v) => !v)}
          >
            <span className="model-toggle-left">
              <BookOpen size={14} />
              <span>
                {showSampleEssay
                  ? "Hide Model Essay"
                  : `View ${writingTask.sampleExaminerBand || "Band 8.5"} Model Answer`}
              </span>
            </span>
            {showSampleEssay ? <ChevronUp size={15} /> : <ChevronDown size={15} />}
          </button>

          {showSampleEssay && (
            <div className="model-essay-body">
              {writingTask.sampleExaminerBand && (
                <div className="model-band-stamp">
                  Examiner Benchmark: {writingTask.sampleExaminerBand}
                </div>
              )}
              <pre className="model-essay-text">{writingTask.sampleEssay}</pre>
            </div>
          )}
        </div>
      )}
    </div>
  );
};
