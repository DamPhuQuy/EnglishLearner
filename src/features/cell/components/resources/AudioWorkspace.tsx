import { ArrowUp, Headphones } from "lucide-react";
import React, { useRef, useState } from "react";

interface Props {
  url: string;
  onError: (msg: string) => void;
}

export const AudioWorkspace: React.FC<Props> = ({ url, onError }) => {
  const audioRef = useRef<HTMLAudioElement>(null);
  const [speed, setSpeed] = useState("1");

  const rewind5s = () => {
    if (audioRef.current) {
      audioRef.current.currentTime = Math.max(0, audioRef.current.currentTime - 5);
    }
  };

  const handleSpeedChange = (e: React.ChangeEvent<HTMLSelectElement>) => {
    const val = e.target.value;
    setSpeed(val);
    if (audioRef.current) {
      audioRef.current.playbackRate = Number(val);
    }
  };

  return (
    <div className="audio-workspace">
      <Headphones size={25} />
      <audio
        key={url}
        ref={audioRef}
        controls
        src={url}
        onError={() =>
          onError(
            "Could not play audio. Please check the URL or select the file again.",
          )
        }
      />
      <div className="audio-tools">
        <button className="button outlined" onClick={rewind5s}>
          <ArrowUp size={14} />
          Back 5s
        </button>
        <label>
          Speed{" "}
          <select
            aria-label="Playback speed"
            value={speed}
            onChange={handleSpeedChange}
          >
            <option value="0.75">0.75×</option>
            <option value="1">1×</option>
            <option value="1.25">1.25×</option>
            <option value="1.5">1.5×</option>
          </select>
        </label>
      </div>
    </div>
  );
};
