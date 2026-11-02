import { BookOpen, Copy, Check } from "lucide-react";
import React, { useState } from "react";

export interface ReadingPassageWorkspaceProps {
  title?: string;
  content?: string;
}

export const ReadingPassageWorkspace: React.FC<ReadingPassageWorkspaceProps> = ({
  title,
  content = "",
}) => {
  const [copied, setCopied] = useState(false);

  const wordCount = content.trim() ? content.trim().split(/\s+/).length : 0;

  // Split content by paragraphs [A], [B], [C], etc.
  const paragraphs = React.useMemo(() => {
    if (!content.trim()) return [];
    // Split by double newlines or by paragraph markers
    const rawParagraphs = content.split(/\n\s*\n/);
    return rawParagraphs.map((p, idx) => {
      const match = p.match(/^\[([A-Z0-9]+)\]\s*(.*)/s);
      if (match) {
        return { label: match[1], text: match[2], full: p };
      }
      return { label: String.fromCharCode(65 + idx), text: p, full: p };
    });
  }, [content]);

  const handleCopy = () => {
    if (!content) return;
    navigator.clipboard.writeText(content);
    setCopied(true);
    setTimeout(() => setCopied(false), 2000);
  };

  const scrollToParagraph = (label: string) => {
    const el = document.getElementById(`para-${label}`);
    if (el) {
      el.scrollIntoView({ behavior: "smooth", block: "start" });
    }
  };

  return (
    <div className="reading-passage-workspace">
      {/* Passage Top Bar */}
      <div className="reading-passage-header">
        <div className="passage-title-group">
          <BookOpen size={14} className="text-blue-400" />
          <h4 className="passage-main-title">{title || "Reading Passage"}</h4>
        </div>
        <div className="passage-meta-right">
          <span className="passage-word-pill">{wordCount} words</span>
          <button
            type="button"
            className="button quiet small copy-passage-btn"
            onClick={handleCopy}
            title="Copy passage text"
          >
            {copied ? <Check size={12} /> : <Copy size={12} />}
            <span>{copied ? "Copied" : "Copy"}</span>
          </button>
        </div>
      </div>

      {/* Paragraph Quick Navigation Anchors */}
      {paragraphs.length > 1 && (
        <div className="passage-anchors-bar">
          <span className="anchors-label">Jump to paragraph:</span>
          <div className="anchors-list">
            {paragraphs.map((p) => (
              <button
                key={p.label}
                type="button"
                className="anchor-btn"
                onClick={() => scrollToParagraph(p.label)}
                title={`Jump to Paragraph ${p.label}`}
              >
                {p.label}
              </button>
            ))}
          </div>
        </div>
      )}

      {/* Passage Body */}
      <div className="passage-content-scroll">
        {paragraphs.map((p) => (
          <div key={p.label} id={`para-${p.label}`} className="passage-paragraph-block">
            <span className="para-letter-badge">[{p.label}]</span>
            <p className="para-text">{p.text}</p>
          </div>
        ))}
      </div>
    </div>
  );
};
