import {
  ArrowUp,
  ChevronDown,
  ChevronUp,
  FileText,
  Headphones,
  Pause,
  Play,
  Square,
  Volume2,
} from "lucide-react";
import React, { useEffect, useRef, useState } from "react";

interface Props {
  url: string;
  transcript?: string;
  onError: (msg: string) => void;
}

export const AudioWorkspace: React.FC<Props> = ({ url, transcript, onError }) => {
  const audioRef = useRef<HTMLAudioElement>(null);
  const [speed, setSpeed] = useState("1");
  const [showTranscript, setShowTranscript] = useState(false);
  const [isSpeaking, setIsSpeaking] = useState(false);
  const [isPaused, setIsPaused] = useState(false);

  useEffect(() => {
    return () => {
      if (typeof window !== "undefined" && window.speechSynthesis) {
        window.speechSynthesis.cancel();
      }
    };
  }, []);

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
    if (typeof window !== "undefined" && window.speechSynthesis && isSpeaking) {
      // Apply speed change to TTS by restarting if needed
    }
  };

  const cleanTranscriptForSpeech = (rawText: string) => {
    return rawText
      .replace(/\[Audio Transcript.*?\]/gi, "")
      .replace(/\[(.*?)\]:/g, "$1 says:")
      .trim();
  };

  const handleToggleSpeech = () => {
    if (typeof window === "undefined" || !window.speechSynthesis) {
      onError("Speech synthesis is not supported in this browser.");
      return;
    }

    if (isSpeaking && !isPaused) {
      window.speechSynthesis.pause();
      setIsPaused(true);
      return;
    }

    if (isSpeaking && isPaused) {
      window.speechSynthesis.resume();
      setIsPaused(false);
      return;
    }

    if (!transcript) {
      onError("No audio transcript available to narrate.");
      return;
    }

    window.speechSynthesis.cancel();
    const textToSpeak = cleanTranscriptForSpeech(transcript);
    const utterance = new SpeechSynthesisUtterance(textToSpeak);
    utterance.lang = "en-GB";
    utterance.rate = Number(speed);

    const voices = window.speechSynthesis.getVoices();
    const englishVoice =
      voices.find((v) => v.lang.startsWith("en-GB")) ||
      voices.find((v) => v.lang.startsWith("en-US")) ||
      voices.find((v) => v.lang.startsWith("en"));
    if (englishVoice) {
      utterance.voice = englishVoice;
    }

    utterance.onend = () => {
      setIsSpeaking(false);
      setIsPaused(false);
    };

    utterance.onerror = () => {
      setIsSpeaking(false);
      setIsPaused(false);
    };

    window.speechSynthesis.speak(utterance);
    setIsSpeaking(true);
    setIsPaused(false);
  };

  const handleStopSpeech = () => {
    if (typeof window !== "undefined" && window.speechSynthesis) {
      window.speechSynthesis.cancel();
    }
    setIsSpeaking(false);
    setIsPaused(false);
  };

  return (
    <div className="audio-workspace">
      <div className="audio-player-card">
        <Headphones size={24} className="audio-icon" />

        {url ? (
          <audio
            key={url}
            ref={audioRef}
            controls
            src={url}
            onError={() =>
              onError(
                "Could not play remote audio. You can use the AI Speech Narration below or attach a local file."
              )
            }
          />
        ) : (
          <div className="audio-empty-notice">
            <span>No remote audio URL specified. Use speech narration below:</span>
          </div>
        )}

        <div className="audio-tools">
          {url && (
            <button className="button outlined" onClick={rewind5s} title="Rewind 5 seconds">
              <ArrowUp size={14} />
              Back 5s
            </button>
          )}

          <label className="audio-speed-label">
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

      {/* TTS Audio Narration Bar */}
      {transcript && (
        <div className="audio-narration-bar">
          <div className="narration-info">
            <Volume2 size={16} className="text-purple-400" />
            <span>AI Voice Narration (Web Speech Engine)</span>
          </div>
          <div className="narration-actions">
            <button
              type="button"
              className={`button ${isSpeaking && !isPaused ? "active" : "primary"}`}
              onClick={handleToggleSpeech}
            >
              {isSpeaking && !isPaused ? (
                <>
                  <Pause size={14} /> Pause Narration
                </>
              ) : isSpeaking && isPaused ? (
                <>
                  <Play size={14} /> Resume Narration
                </>
              ) : (
                <>
                  <Play size={14} /> Play Script Audio
                </>
              )}
            </button>
            {isSpeaking && (
              <button
                type="button"
                className="button quiet"
                onClick={handleStopSpeech}
                title="Stop narration"
              >
                <Square size={14} /> Stop
              </button>
            )}
          </div>
        </div>
      )}

      {/* Interactive Transcript Viewer */}
      {transcript && (
        <div className="audio-transcript-wrapper">
          <button
            type="button"
            className="transcript-toggle-btn"
            onClick={() => setShowTranscript(!showTranscript)}
          >
            <span className="transcript-toggle-left">
              <FileText size={15} />
              Audio Transcript & Dialogue Turns
            </span>
            {showTranscript ? <ChevronUp size={16} /> : <ChevronDown size={16} />}
          </button>

          {showTranscript && (
            <div className="audio-transcript-content">
              {transcript.split("\n").map((line, idx) => {
                if (!line.trim()) return null;
                const isSpeaker = line.startsWith("[") && line.includes("]:");
                return (
                  <p key={idx} className={isSpeaker ? "transcript-speaker-line" : "transcript-line"}>
                    {line}
                  </p>
                );
              })}
            </div>
          )}
        </div>
      )}
    </div>
  );
};
