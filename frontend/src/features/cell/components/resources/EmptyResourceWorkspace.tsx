import { Paperclip } from "lucide-react";
import React from "react";

interface Props {
  disabled: boolean;
  onSelectFile: () => void;
}

export const EmptyResourceWorkspace: React.FC<Props> = ({
  disabled,
  onSelectFile,
}) => {
  return (
    <div className="resource-empty">
      <Paperclip size={23} />
      <p>Keep reference material alongside your response</p>
      <span>
        Drag and drop or attach PDF, image, audio, or TXT.
        <br />
        Up to 2 MB per file.
      </span>
      <button
        className="button outlined"
        disabled={disabled}
        onClick={onSelectFile}
      >
        Select document
      </button>
    </div>
  );
};
