import {
  Check,
  ClipboardCopy,
  FileCode,
  FileJson,
  HelpCircle,
  Sparkles,
  Upload,
  X,
} from "lucide-react";
import React, { useState } from "react";
import type { IeltsExerciseData, IeltsSkill } from "../../types/ieltsSchema.ts";
import { isIeltsExerciseData } from "../../types/ieltsSchema.ts";
import { getIeltsAiPrompt } from "../../services/aiPromptTemplate.ts";

export interface AiImportModalProps {
  isOpen: boolean;
  onClose: () => void;
  onApplyExercise: (data: IeltsExerciseData) => void;
  initialSkill?: IeltsSkill;
}

export const AiImportModal: React.FC<AiImportModalProps> = ({
  isOpen,
  onClose,
  onApplyExercise,
  initialSkill = "reading",
}) => {
  const [tab, setTab] = useState<"import" | "guide">("import");
  const [guideSkill, setGuideSkill] = useState<IeltsSkill>(
    ["reading", "listening", "writing", "speaking"].includes(initialSkill)
      ? initialSkill
      : "reading"
  );
  const [jsonText, setJsonText] = useState("");
  const [parsedData, setParsedData] = useState<IeltsExerciseData | null>(null);
  const [error, setError] = useState<string>("");
  const [copied, setCopied] = useState(false);

  if (!isOpen) return null;

  const handleJsonChange = (text: string) => {
    setJsonText(text);
    setError("");
    if (!text.trim()) {
      setParsedData(null);
      return;
    }

    try {
      // Auto clean code blocks if user pasted ```json ... ```
      let cleaned = text.trim();
      if (cleaned.startsWith("```")) {
        cleaned = cleaned.replace(/^```[a-zA-Z]*\n?/, "").replace(/\n?```$/, "");
      }

      const obj = JSON.parse(cleaned);
      if (isIeltsExerciseData(obj)) {
        setParsedData(obj);
        setError("");
      } else {
        setParsedData(null);
        setError(
          "JSON parsed, but does not match IELTS Exercise Schema. Missing 'skill', 'title', or 'questionGroups'."
        );
      }
    } catch (err) {
      setParsedData(null);
      setError(err instanceof Error ? err.message : "Invalid JSON syntax");
    }
  };

  const handleFileUpload = async (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];
    if (!file) return;
    try {
      const text = await file.text();
      handleJsonChange(text);
    } catch {
      setError("Failed to read file.");
    }
    e.target.value = "";
  };

  const handleApply = () => {
    if (!parsedData) return;
    onApplyExercise(parsedData);
    onClose();
  };

  const currentPrompt = getIeltsAiPrompt(guideSkill);

  const handleCopyPrompt = async () => {
    try {
      await navigator.clipboard.writeText(currentPrompt);
      setCopied(true);
      setTimeout(() => setCopied(false), 2500);
    } catch {
      // fallback
    }
  };

  const totalQuestions =
    parsedData?.questionGroups?.reduce(
      (acc, g) => acc + (g.questions?.length || 0),
      0
    ) || 0;

  return (
    <div className="modal-backdrop" onClick={onClose}>
      <div
        className="ai-modal-card"
        onClick={(e) => e.stopPropagation()}
        role="dialog"
        aria-modal="true"
      >
        <div className="ai-modal-header">
          <div className="ai-modal-title">
            <Sparkles size={18} className="ai-modal-icon" />
            <span>AI Mini-IELTS Structured Import</span>
          </div>
          <button className="button quiet small" onClick={onClose} aria-label="Close">
            <X size={16} />
          </button>
        </div>

        <div className="ai-modal-tabs">
          <button
            type="button"
            className={`ai-tab-btn ${tab === "import" ? "active" : ""}`}
            onClick={() => setTab("import")}
          >
            <FileJson size={14} />
            Paste or Upload JSON
          </button>
          <button
            type="button"
            className={`ai-tab-btn ${tab === "guide" ? "active" : ""}`}
            onClick={() => setTab("guide")}
          >
            <HelpCircle size={14} />
            AI Prompt & Schema Guide
          </button>
        </div>

        {tab === "import" ? (
          <div className="ai-modal-body">
            <div className="ai-upload-row">
              <label className="button outlined small file-picker-label">
                <Upload size={14} />
                <span>Upload .json File</span>
                <input
                  type="file"
                  accept=".json,application/json"
                  onChange={handleFileUpload}
                  hidden
                />
              </label>
              <span className="ai-upload-hint">
                Or paste the JSON response directly below
              </span>
            </div>

            <textarea
              className="ai-json-textarea"
              placeholder={`Paste the AI generated JSON here, for example:\n{\n  "version": "1.0",\n  "skill": "${initialSkill}",\n  "title": "Passage 1...",\n  "questionGroups": [...]\n}`}
              value={jsonText}
              onChange={(e) => handleJsonChange(e.target.value)}
              spellCheck={false}
            />

            {error && (
              <div className="ai-modal-error">
                <span>{error}</span>
              </div>
            )}

            {parsedData && (
              <div className="ai-preview-card">
                <div className="preview-heading">
                  <Check size={16} className="text-green-400" />
                  <span>Valid IELTS Exercise Detected!</span>
                </div>
                <div className="preview-meta-grid">
                  <div>
                    <strong>Title:</strong> {parsedData.title}
                  </div>
                  <div>
                    <strong>Skill:</strong> {parsedData.skill.toUpperCase()}
                  </div>
                  <div>
                    <strong>Question Groups:</strong>{" "}
                    {parsedData.questionGroups?.length || 0}
                  </div>
                  <div>
                    <strong>Total Questions:</strong> {totalQuestions}
                  </div>
                  {parsedData.material?.content && (
                    <div>
                      <strong>Passage Length:</strong>{" "}
                      {parsedData.material.content.split(/\s+/).length} words
                    </div>
                  )}
                </div>
              </div>
            )}

            <div className="ai-modal-footer">
              <button
                type="button"
                className="button primary"
                disabled={!parsedData}
                onClick={handleApply}
              >
                <Sparkles size={15} />
                Apply to this Cell
              </button>
              <button type="button" className="button quiet" onClick={onClose}>
                Cancel
              </button>
            </div>
          </div>
        ) : (
          <div className="ai-modal-body">
            <div className="ai-guide-skills-selector">
              {(["reading", "listening", "writing", "speaking"] as IeltsSkill[]).map(
                (s) => (
                  <button
                    key={s}
                    type="button"
                    className={`skill-pill-btn ${guideSkill === s ? "active" : ""}`}
                    onClick={() => setGuideSkill(s)}
                  >
                    {s.toUpperCase()} PROMPT
                  </button>
                )
              )}
            </div>

            <div className="ai-guide-intro">
              <p>
                Select skill above, copy prompt, and paste to <strong>ChatGPT</strong>,{" "}
                <strong>Claude</strong>, or <strong>Gemini</strong> with any text/topic:
              </p>
              <button
                type="button"
                className="button primary small copy-prompt-btn"
                onClick={handleCopyPrompt}
              >
                {copied ? <Check size={14} /> : <ClipboardCopy size={14} />}
                <span>
                  {copied ? "Copied!" : `Copy ${guideSkill.toUpperCase()} Prompt`}
                </span>
              </button>
            </div>

            <pre className="ai-prompt-preview">
              <code>{currentPrompt}</code>
            </pre>
          </div>
        )}
      </div>
    </div>
  );
};
