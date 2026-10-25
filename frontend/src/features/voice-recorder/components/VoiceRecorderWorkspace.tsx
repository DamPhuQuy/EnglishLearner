import { Mic, Square } from "lucide-react";
import React from "react";

interface Props {
  recording: boolean;
  seconds: number;
  disabled: boolean;
  onStart: () => void;
  onStop: () => void;
}

const formatTime = (n: number) =>
  `${Math.floor(n / 60)}:${String(n % 60).padStart(2, "0")}`;

export const VoiceRecorderWorkspace: React.FC<Props> = ({
  recording,
  seconds,
  disabled,
  onStart,
  onStop,
}) => {
  return (
    <div className="recorder">
      <Mic size={24} />
      <p>{recording ? "Recording in progress" : "Practice speaking, then review"}</p>
      <output className="recording-time">
        {recording ? formatTime(seconds) : "Recording saved with your notebook"}
      </output>
      {recording ? (
        <button className="button record-stop" onClick={onStop}>
          <Square size={14} />
          Stop recording
        </button>
      ) : (
        <button
          className="button outlined"
          disabled={disabled}
          onClick={onStart}
        >
          <Mic size={15} />
          Start recording
        </button>
      )}
    </div>
  );
};
