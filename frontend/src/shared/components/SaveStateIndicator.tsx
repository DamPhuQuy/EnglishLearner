import { Check, CircleAlert } from "lucide-react";
import React from "react";
import type { SaveState } from "../../features/notebook/hooks/useNotebook.ts";

interface Props {
  state: SaveState;
}

export const SaveStateIndicator: React.FC<Props> = ({ state }) => {
  return (
    <output className={`save-state ${state}`}>
      {state === "saved" ? (
        <Check size={14} />
      ) : state === "error" ? (
        <CircleAlert size={14} />
      ) : null}
      {state === "saved"
        ? "Saved locally"
        : state === "error"
          ? "Save failed"
          : "Saving…"}
    </output>
  );
};
