import React from "react";

export interface CellEditorPaneProps {
  cellId: string;
  source: string;
  onUpdateSource: (source: string) => void;
  onRun: () => void;
}

export const CellEditorPane: React.FC<CellEditorPaneProps> = ({
  cellId,
  source,
  onUpdateSource,
  onRun,
}) => {
  const wordCount = source.trim() ? source.trim().split(/\s+/).length : 0;

  return (
    <div className="answer-pane">
      <div className="pane-heading">
        <label htmlFor={`editor-${cellId}`}>Response & Notes</label>
        <span>Markdown</span>
      </div>
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
        placeholder="Write your response, answers, or notes here…"
        spellCheck={false}
      />
      <div className="editor-footer">
        {wordCount} {wordCount === 1 ? "word" : "words"}
      </div>
    </div>
  );
};
