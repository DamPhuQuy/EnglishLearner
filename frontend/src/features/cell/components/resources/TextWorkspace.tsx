import React from "react";

interface Props {
  content?: string;
}

export const TextWorkspace: React.FC<Props> = ({ content }) => {
  return <div className="reference-text">{content}</div>;
};
