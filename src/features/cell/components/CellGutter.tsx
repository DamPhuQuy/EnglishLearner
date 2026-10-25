import React from "react";

export interface CellGutterProps {
  executionCount: number | null;
}

export const CellGutter: React.FC<CellGutterProps> = ({ executionCount }) => {
  return (
    <div
      className="cell-gutter"
      aria-label={`Execution count ${executionCount ?? "none"}`}
    >
      In [{executionCount ?? " "}]:
    </div>
  );
};
