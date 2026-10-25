import { Undo2 } from "lucide-react";
import React from "react";

interface Props {
  onUndo: () => void;
  onDismiss: () => void;
}

export const UndoNotice: React.FC<Props> = ({ onUndo, onDismiss }) => {
  return (
    <output className="undo-notice">
      <span>Cell deleted.</span>
      <button className="button quiet" onClick={onUndo}>
        <Undo2 size={15} />
        Undo
      </button>
      <button
        className="button quiet"
        aria-label="Dismiss notice"
        onClick={onDismiss}
      >
        Dismiss
      </button>
    </output>
  );
};
