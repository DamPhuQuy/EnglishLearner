import React from "react";

interface Props {
  url: string;
  name?: string;
}

export const ImageWorkspace: React.FC<Props> = ({ url, name }) => {
  return (
    <img
      src={url}
      alt={name || "Prompt illustration image"}
    />
  );
};
