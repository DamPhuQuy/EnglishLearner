import React from "react";

interface Props {
  url: string;
  name?: string;
}

export const PdfWorkspace: React.FC<Props> = ({ url, name }) => {
  return (
    <>
      <iframe src={url} title={`PDF: ${name || "Document"}`} />
      <a href={url} target="_blank" rel="noreferrer">
        Open PDF separately
      </a>
    </>
  );
};
