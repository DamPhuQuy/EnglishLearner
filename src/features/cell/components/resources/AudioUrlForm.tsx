import React, { useState } from "react";

interface Props {
  cellId: string;
  disabled: boolean;
  onSubmitUrl: (url: string) => void;
  onError: (msg: string) => void;
}

export const AudioUrlForm: React.FC<Props> = ({
  cellId,
  disabled,
  onSubmitUrl,
  onError,
}) => {
  const [url, setUrl] = useState("");

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    try {
      const parsed = new URL(url);
      if (!["https:", "http:"].includes(parsed.protocol)) {
        throw new Error();
      }
      onSubmitUrl(parsed.href);
      setUrl("");
    } catch {
      onError("Enter an audio URL starting with https:// or http://.");
    }
  };

  return (
    <form className="audio-url" onSubmit={handleSubmit}>
      <label htmlFor={`url-${cellId}`}>Or use an audio track URL</label>
      <div>
        <input
          id={`url-${cellId}`}
          type="url"
          required
          placeholder="https://…/audio.mp3"
          value={url}
          onChange={(e) => setUrl(e.target.value)}
        />
        <button className="button outlined" disabled={disabled}>
          Load
        </button>
      </div>
    </form>
  );
};
