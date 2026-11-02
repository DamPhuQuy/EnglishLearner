import {
  CheckCircle2,
  Code,
  FileEdit,
  FileJson,
  FileText,
  ListChecks,
  PenLine,
  Sparkles,
} from "lucide-react";
import React, { useEffect, useState } from "react";
import type { CellResource, SkillType } from "../../notebook/types/notebook.ts";
import type { IeltsExerciseData } from "../types/ieltsSchema.ts";
import { isIeltsExerciseData } from "../types/ieltsSchema.ts";
import { AiImportModal } from "./interactive/AiImportModal.tsx";
import { InteractiveQuestionSheet } from "./interactive/InteractiveQuestionSheet.tsx";

export interface CellEditorPaneProps {
  cellId: string;
  source: string;
  cellType?: SkillType;
  structuredData?: IeltsExerciseData;
  onUpdateSource: (source: string) => void;
  onUpdateStructuredData?: (data: IeltsExerciseData | undefined) => void;
  onUpdateResource?: (resource: CellResource | undefined) => void;
  onRun: () => void;
}

export const CellEditorPane: React.FC<CellEditorPaneProps> = ({
  cellId,
  source,
  cellType = "markdown",
  structuredData,
  onUpdateSource,
  onUpdateStructuredData,
  onUpdateResource,
  onRun,
}) => {
  const getInitialMode = () => {
    if (!structuredData) return "markdown";
    if (structuredData.writingTask || structuredData.speakingTask) return "markdown";
    if (structuredData.questionGroups?.length) return "interactive";
    return "markdown";
  };

  const [viewMode, setViewMode] = useState<"interactive" | "markdown" | "json">(getInitialMode());
  const [isAiModalOpen, setIsAiModalOpen] = useState(false);

  useEffect(() => {
    if (structuredData) {
      if (structuredData.writingTask || structuredData.speakingTask) {
        setViewMode("markdown");
      } else if (structuredData.questionGroups?.length) {
        setViewMode("interactive");
      }
    }
  }, [structuredData]);

  const wordCount = source.trim() ? source.trim().split(/\s+/).length : 0;

  // Auto-detect if user pasted JSON into the markdown textarea
  const isPastedJson = React.useMemo(() => {
    if (structuredData || !source.trim().startsWith("{")) return false;
    try {
      const parsed = JSON.parse(source.trim());
      return isIeltsExerciseData(parsed) ? parsed : false;
    } catch {
      return false;
    }
  }, [source, structuredData]);

  const handleApplyAiData = (exercise: IeltsExerciseData) => {
    if (onUpdateStructuredData) {
      onUpdateStructuredData(exercise);
    }

    // If exercise includes material (e.g. passage or audio), populate cell resource
    if (exercise.material && onUpdateResource) {
      if (exercise.material.type === "text" && exercise.material.content) {
        onUpdateResource({
          type: "text",
          name: exercise.material.title || `${exercise.title}.txt`,
          textContent: exercise.material.content,
        });
      } else if (exercise.material.type === "audio") {
        onUpdateResource({
          type: "audio",
          name: exercise.material.title || `${exercise.title}.mp3`,
          url: exercise.material.audioUrl || "",
          textContent: exercise.material.audioTranscript || "",
        });
      }
    }

    if (exercise.writingTask || exercise.speakingTask) {
      setViewMode("markdown");
    } else {
      setViewMode("interactive");
    }
  };

  const handleConvertPastedJson = () => {
    if (isPastedJson && typeof isPastedJson === "object") {
      handleApplyAiData(isPastedJson as IeltsExerciseData);
    }
  };

  const isWritingTask = Boolean(structuredData?.writingTask);
  const isSpeakingTask = Boolean(structuredData?.speakingTask);
  const hasQuestionGroups = Boolean(structuredData?.questionGroups?.length);

  return (
    <div className="answer-pane">
      <div className="pane-heading">
        <div className="pane-heading-left">
          <label htmlFor={`editor-${cellId}`}>
            {isWritingTask
              ? "Essay Draft & Response"
              : isSpeakingTask
              ? "Speaking Preparation & Notes"
              : structuredData
              ? "Questions & Responses"
              : "Response & Notes"}
          </label>

          {structuredData && (
            <div className="view-mode-tabs">
              {hasQuestionGroups && (
                <button
                  type="button"
                  className={`view-tab-btn ${viewMode === "interactive" ? "active" : ""}`}
                  onClick={() => setViewMode("interactive")}
                  title="Interactive Question Sheet"
                >
                  <ListChecks size={13} />
                  <span>Questions</span>
                </button>
              )}
              {isWritingTask && (
                <button
                  type="button"
                  className={`view-tab-btn ${viewMode === "markdown" ? "active" : ""}`}
                  onClick={() => setViewMode("markdown")}
                  title="Essay Draft"
                >
                  <PenLine size={13} />
                  <span>Essay Draft</span>
                </button>
              )}
              {isSpeakingTask && (
                <button
                  type="button"
                  className={`view-tab-btn ${viewMode === "markdown" ? "active" : ""}`}
                  onClick={() => setViewMode("markdown")}
                  title="Speaking Preparation Notes"
                >
                  <FileEdit size={13} />
                  <span>Prep Notes</span>
                </button>
              )}
              {!isWritingTask && !isSpeakingTask && (
                <button
                  type="button"
                  className={`view-tab-btn ${viewMode === "markdown" ? "active" : ""}`}
                  onClick={() => setViewMode("markdown")}
                  title="Notes / Markdown"
                >
                  <FileEdit size={13} />
                  <span>Notes</span>
                </button>
              )}
              <button
                type="button"
                className={`view-tab-btn ${viewMode === "json" ? "active" : ""}`}
                onClick={() => setViewMode("json")}
                title="Raw Structured JSON"
              >
                <Code size={13} />
                <span>JSON</span>
              </button>
            </div>
          )}
        </div>

        <div className="pane-heading-right">
          <button
            type="button"
            className="ai-import-btn"
            onClick={() => setIsAiModalOpen(true)}
            title="Import or paste JSON test generated by AI"
          >
            <Sparkles size={13} />
            <span>AI JSON</span>
          </button>
          {!structuredData && <span>Markdown</span>}
        </div>
      </div>

      {/* Suggestion banner if valid JSON is pasted in textarea */}
      {isPastedJson && !structuredData && (
        <div className="json-detected-banner">
          <Sparkles size={14} className="banner-icon" />
          <span>Valid AI IELTS JSON detected!</span>
          <button
            type="button"
            className="button primary small"
            onClick={handleConvertPastedJson}
          >
            Render Interactive Test
          </button>
        </div>
      )}

      {/* Content based on viewMode and structuredData */}
      {structuredData && hasQuestionGroups && viewMode === "interactive" ? (
        <InteractiveQuestionSheet
          data={structuredData}
          onUpdateData={(next) => onUpdateStructuredData?.(next)}
          onOpenImportModal={() => setIsAiModalOpen(true)}
        />
      ) : structuredData && viewMode === "json" ? (
        <div className="json-editor-container">
          <textarea
            id={`json-editor-${cellId}`}
            value={JSON.stringify(structuredData, null, 2)}
            onChange={(e) => {
              try {
                const parsed = JSON.parse(e.target.value);
                if (isIeltsExerciseData(parsed)) {
                  onUpdateStructuredData?.(parsed);
                }
              } catch {
                // allow typing invalid json temporarily
              }
            }}
            spellCheck={false}
          />
        </div>
      ) : (
        <>
          <textarea
            id={`editor-${cellId}`}
            value={source}
            onChange={(e) => onUpdateSource(e.target.value)}
            onKeyDown={(e) => {
              if (e.key === "Enter" && e.shiftKey) {
                e.preventDefault();
                onRun();
              }
            }}
            placeholder={
              isWritingTask
                ? "Draft your essay response here. Refer to the task prompt and data features on the right pane..."
                : isSpeakingTask
                ? "Note down your 1-minute prep bullet points, vocabulary ideas, and discourse structure..."
                : "Write your response, answers, or notes here… (or paste AI JSON to parse)"
            }
            spellCheck={false}
          />
          <div className="editor-footer">
            <div className="editor-footer-left">
              {isWritingTask && structuredData?.writingTask ? (
                wordCount >= (structuredData.writingTask.minWords || 150) ? (
                  <span className="word-count-success">
                    <CheckCircle2 size={13} /> {wordCount} words (Target of {structuredData.writingTask.minWords || 150}+ met!)
                  </span>
                ) : (
                  <span className="word-count-pending">
                    {wordCount} / {structuredData.writingTask.minWords || 150} words ({Math.max(0, (structuredData.writingTask.minWords || 150) - wordCount)} words remaining)
                  </span>
                )
              ) : isSpeakingTask ? (
                <span className="speaking-prep-indicator">
                  Preparation & Strategy Notes
                </span>
              ) : (
                <span>{wordCount} {wordCount === 1 ? "word" : "words"}</span>
              )}
            </div>

            {isWritingTask && (
              <div className="editor-criteria-badges">
                <span title="Task Achievement / Response">Task Achievement</span>
                <span title="Coherence & Cohesion">Coherence & Cohesion</span>
                <span title="Lexical Resource">Lexicon</span>
                <span title="Grammatical Range & Accuracy">Grammar</span>
              </div>
            )}
          </div>
        </>
      )}

      {/* AI Import / Guide Modal */}
      <AiImportModal
        isOpen={isAiModalOpen}
        onClose={() => setIsAiModalOpen(false)}
        onApplyExercise={handleApplyAiData}
        initialSkill={cellType as any}
      />
    </div>
  );
};
