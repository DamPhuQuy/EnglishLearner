import {
  AlertCircle,
  ArrowUp,
  ChevronDown,
  ChevronUp,
  FileText,
  Headphones,
  Mic,
  Pause,
  Play,
  RotateCcw,
  Sparkles,
  Square,
  Volume2,
} from "lucide-react";
import React, { useEffect, useMemo, useRef, useState } from "react";

interface Props {
  url: string;
  transcript?: string;
  onError: (msg: string) => void;
}

interface DialogueTurn {
  id: number;
  speaker: string;
  text: string;
  raw: string;
}

export const AudioWorkspace: React.FC<Props> = ({ url, transcript, onError }) => {
  const audioRef = useRef<HTMLAudioElement>(null);
  const activeUtteranceRef = useRef<SpeechSynthesisUtterance | null>(null);
  const isStoppedRef = useRef(false);
  const nextTurnTimerRef = useRef<number | null>(null);

  const [speed, setSpeed] = useState("1");
  const [showTranscript, setShowTranscript] = useState(true);
  const [isSpeaking, setIsSpeaking] = useState(false);
  const [isPaused, setIsPaused] = useState(false);
  const [currentTurnIdx, setCurrentTurnIdx] = useState<number | null>(null);
  const [voices, setVoices] = useState<SpeechSynthesisVoice[]>([]);
  const [selectedVoiceURI, setSelectedVoiceURI] = useState<string>("system-default");
  const [speechError, setSpeechError] = useState<string>("");

  // Parse transcript into distinct conversational turns
  const turns: DialogueTurn[] = useMemo(() => {
    if (!transcript) return [];
    const lines = transcript.split("\n").map((l) => l.trim()).filter(Boolean);
    const parsed: DialogueTurn[] = [];
    let currentSpeaker = "Narrator";

    for (const line of lines) {
      if (
        line.startsWith("[Audio Transcript") ||
        line.startsWith("###") ||
        line.startsWith("===")
      ) {
        continue;
      }

      const match = line.match(/^\[([^\]]+)\]:\s*(.*)$/);
      if (match) {
        currentSpeaker = match[1].trim();
        parsed.push({
          id: parsed.length,
          speaker: currentSpeaker,
          text: match[2].trim(),
          raw: line,
        });
      } else if (parsed.length > 0) {
        parsed[parsed.length - 1].text += " " + line;
        parsed[parsed.length - 1].raw += " " + line;
      } else {
        parsed.push({
          id: parsed.length,
          speaker: currentSpeaker,
          text: line,
          raw: line,
        });
      }
    }

    return parsed;
  }, [transcript]);

  // Load and listen for available speech synthesis voices
  useEffect(() => {
    if (typeof window === "undefined" || !("speechSynthesis" in window)) {
      return;
    }

    const isLinux =
      typeof navigator !== "undefined" && /linux/i.test(navigator.userAgent);

    const loadVoices = () => {
      const allVoices = window.speechSynthesis.getVoices();
      if (!allVoices || allVoices.length === 0) return;

      const englishVoices = allVoices.filter(
        (v) => v.lang.startsWith("en") || v.lang.startsWith("EN")
      );
      const displayVoices = englishVoices.length > 0 ? englishVoices : allVoices;
      setVoices(displayVoices);

      // On Linux, default to "system-default" to prevent remote Google TTS synthesis-failed errors
      setSelectedVoiceURI((prev) => {
        if (prev === "system-default") return "system-default";
        if (prev && displayVoices.some((v) => v.voiceURI === prev)) {
          return prev;
        }
        if (isLinux) {
          return "system-default";
        }
        const preferred =
          displayVoices.find(
            (v) => v.lang.startsWith("en-GB") && /female|natural/i.test(v.name)
          ) ||
          displayVoices.find((v) => v.lang.startsWith("en-GB")) ||
          displayVoices.find((v) => v.lang.startsWith("en-US")) ||
          displayVoices[0];
        return preferred?.voiceURI || "system-default";
      });
    };

    loadVoices();
    window.speechSynthesis.onvoiceschanged = loadVoices;

    return () => {
      if (typeof window !== "undefined" && window.speechSynthesis) {
        window.speechSynthesis.cancel();
      }
      if (nextTurnTimerRef.current) {
        window.clearTimeout(nextTurnTimerRef.current);
      }
    };
  }, []);

  const playExamChime = () => {
    try {
      const AudioCtx =
        window.AudioContext ||
        (window as unknown as { webkitAudioContext: typeof AudioContext })
          .webkitAudioContext;
      if (!AudioCtx) return;
      const ctx = new AudioCtx();
      const osc = ctx.createOscillator();
      const gain = ctx.createGain();

      osc.type = "sine";
      osc.frequency.setValueAtTime(587.33, ctx.currentTime); // D5
      osc.frequency.setValueAtTime(880, ctx.currentTime + 0.14); // A5

      gain.gain.setValueAtTime(0.12, ctx.currentTime);
      gain.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + 0.45);

      osc.connect(gain);
      gain.connect(ctx.destination);
      osc.start();
      osc.stop(ctx.currentTime + 0.5);

      osc.onended = () => {
        try {
          ctx.close();
        } catch {
          // ignore close error
        }
      };
    } catch {
      // AudioContext non-critical fallback
    }
  };

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

  // Speak a single turn safely with automatic fallback
  const speakTurn = (turnIndex: number, retryCount = 0) => {
    if (
      isStoppedRef.current ||
      turnIndex < 0 ||
      turnIndex >= turns.length ||
      typeof window === "undefined" ||
      !("speechSynthesis" in window)
    ) {
      setIsSpeaking(false);
      setIsPaused(false);
      setCurrentTurnIdx(null);
      return;
    }

    const currentTurn = turns[turnIndex];
    setCurrentTurnIdx(turnIndex);
    setSpeechError("");

    // Ensure Chrome paused queue is resumed
    if (window.speechSynthesis.paused) {
      window.speechSynthesis.resume();
    }

    const utterance = new SpeechSynthesisUtterance(currentTurn.text);
    utterance.rate = Number(speed);

    // If retryCount === 0 and voice is not "system-default", use chosen voice
    if (retryCount === 0 && selectedVoiceURI !== "system-default") {
      const availableVoices = window.speechSynthesis.getVoices();
      let chosenVoice = availableVoices.find((v) => v.voiceURI === selectedVoiceURI);
      if (!chosenVoice) {
        chosenVoice =
          availableVoices.find((v) => v.lang.startsWith("en-GB")) ||
          availableVoices.find((v) => v.lang.startsWith("en-US")) ||
          availableVoices.find((v) => v.lang.startsWith("en"));
      }

      const uniqueSpeakers = Array.from(new Set(turns.map((t) => t.speaker)));
      const speakerRank = uniqueSpeakers.indexOf(currentTurn.speaker);

      if (chosenVoice) {
        if (speakerRank % 2 === 1) {
          const altVoice = availableVoices.find(
            (v) => v.lang.startsWith("en") && v.voiceURI !== chosenVoice?.voiceURI
          );
          if (altVoice) {
            utterance.voice = altVoice;
          } else {
            utterance.voice = chosenVoice;
            utterance.pitch = 0.9;
          }
        } else {
          utterance.voice = chosenVoice;
          utterance.pitch = 1.05;
        }
      }
    } else {
      // Use browser default offline engine without forcing a remote voice object
      utterance.lang = "en-US";
    }

    utterance.onstart = () => {
      setIsSpeaking(true);
      setIsPaused(false);
    };

    utterance.onend = () => {
      if (isStoppedRef.current) return;
      if (turnIndex + 1 < turns.length) {
        nextTurnTimerRef.current = window.setTimeout(() => {
          speakTurn(turnIndex + 1, 0);
        }, 300);
      } else {
        setIsSpeaking(false);
        setIsPaused(false);
        setCurrentTurnIdx(null);
      }
    };

    utterance.onerror = (e) => {
      if (e.error === "canceled" || e.error === "interrupted") {
        return;
      }

      // Automatic Fallback: If remote voice failed with synthesis-failed, transparently fallback to system-default!
      if (
        e.error === "synthesis-failed" &&
        retryCount === 0 &&
        selectedVoiceURI !== "system-default"
      ) {
        console.warn(
          "Remote voice failed (synthesis-failed). Auto-retrying with native system voice..."
        );
        setSelectedVoiceURI("system-default");
        speakTurn(turnIndex, 1);
        return;
      }

      console.warn("Speech synthesis error event:", e);
      const msg =
        e.error === "not-allowed"
          ? "Browser blocked audio autoplay. Click 'Play Script Audio' again to grant audio permission."
          : `Speech synthesis error (${e.error || "unavailable"}). You can read along with the interactive transcript below.`;
      setSpeechError(msg);
      onError(msg);
      setIsSpeaking(false);
      setIsPaused(false);
      setCurrentTurnIdx(null);
    };

    // Keep active utterance on ref and window to prevent Chromium GC freeze bug
    activeUtteranceRef.current = utterance;
    (window as unknown as { __activeUtterance: SpeechSynthesisUtterance }).__activeUtterance =
      utterance;

    try {
      window.speechSynthesis.speak(utterance);
    } catch (err) {
      console.error("speechSynthesis.speak call threw:", err);
      if (retryCount === 0) {
        speakTurn(turnIndex, 1);
      } else {
        setSpeechError("Could not invoke Web Speech engine. Please verify browser audio permissions.");
        setIsSpeaking(false);
        setIsPaused(false);
      }
    }
  };

  const handleToggleSpeech = () => {
    if (typeof window === "undefined" || !("speechSynthesis" in window)) {
      const msg = "Speech synthesis is not supported in this browser.";
      setSpeechError(msg);
      onError(msg);
      return;
    }

    // 1. If currently speaking and active: Pause
    if (isSpeaking && !isPaused) {
      window.speechSynthesis.pause();
      setIsPaused(true);
      return;
    }

    // 2. If paused: Resume
    if (isSpeaking && isPaused) {
      window.speechSynthesis.resume();
      setIsPaused(false);
      return;
    }

    // 3. Otherwise: Start from beginning or current turn
    if (turns.length === 0) {
      const msg = "No audio transcript or dialogue turns available to narrate.";
      setSpeechError(msg);
      onError(msg);
      return;
    }

    isStoppedRef.current = false;
    playExamChime();

    const startIdx = currentTurnIdx !== null && currentTurnIdx < turns.length ? currentTurnIdx : 0;
    speakTurn(startIdx, 0);
  };

  const handleStopSpeech = () => {
    isStoppedRef.current = true;
    if (nextTurnTimerRef.current) {
      window.clearTimeout(nextTurnTimerRef.current);
    }
    if (typeof window !== "undefined" && window.speechSynthesis) {
      window.speechSynthesis.cancel();
    }
    setIsSpeaking(false);
    setIsPaused(false);
    setCurrentTurnIdx(null);
    setSpeechError("");
  };

  const handlePlaySpecificTurn = (index: number) => {
    handleStopSpeech();
    isStoppedRef.current = false;
    setTimeout(() => {
      speakTurn(index, 0);
    }, 60);
  };

  return (
    <div className="audio-workspace">
      {/* Remote Audio Track Card */}
      <div className="audio-player-card">
        <Headphones size={24} className="audio-icon" />

        {url ? (
          <audio
            key={url}
            ref={audioRef}
            controls
            src={url}
            onError={() => {
              // Gracefully handle remote audio failure without freezing
            }}
          />
        ) : (
          <div className="audio-empty-notice">
            <span>No remote audio file attached. Use speech narration below:</span>
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

      {/* AI Speech Narration Control Bar */}
      {turns.length > 0 && (
        <div className="audio-narration-bar">
          <div className="narration-header-row">
            <div className="narration-info">
              <Volume2 size={16} className="text-purple-400" />
              <span>AI Voice Narration (Web Speech Engine)</span>
              {isSpeaking && !isPaused && (
                <div className="audio-live-waveform" title="Narration active">
                  <span className="wave-bar bar-1" />
                  <span className="wave-bar bar-2" />
                  <span className="wave-bar bar-3" />
                  <span className="wave-bar bar-4" />
                </div>
              )}
            </div>

            {/* Voice Selector with System Default option */}
            <div className="narration-voice-picker">
              <select
                value={selectedVoiceURI}
                onChange={(e) => {
                  setSelectedVoiceURI(e.target.value);
                  setSpeechError("");
                }}
                className="voice-select"
                aria-label="Select speech voice"
                title="Choose IELTS narrator voice"
              >
                <option value="system-default">
                  Default System Voice (Offline Engine)
                </option>
                {voices.map((v) => (
                  <option key={v.voiceURI} value={v.voiceURI}>
                    {v.name} ({v.lang})
                  </option>
                ))}
              </select>
            </div>
          </div>

          {/* Action buttons and turn indicator */}
          <div className="narration-actions">
            <button
              type="button"
              className={`button ${isSpeaking && !isPaused ? "active" : "primary"} narration-toggle-btn`}
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
                <Square size={13} /> Stop
              </button>
            )}

            {currentTurnIdx !== null && (
              <span className="turn-progress-pill">
                Turn {currentTurnIdx + 1} of {turns.length}
              </span>
            )}
          </div>

          {speechError && (
            <div className="narration-error-alert" role="alert">
              <AlertCircle size={14} />
              <span>{speechError}</span>
            </div>
          )}
        </div>
      )}

      {/* Interactive Transcript Viewer with dialogue turns */}
      {turns.length > 0 && (
        <div className="audio-transcript-wrapper">
          <button
            type="button"
            className="transcript-toggle-btn"
            onClick={() => setShowTranscript(!showTranscript)}
            aria-expanded={showTranscript}
          >
            <span className="transcript-toggle-left">
              <FileText size={15} />
              <span>Audio Transcript & Dialogue Turns ({turns.length} turns)</span>
            </span>
            {showTranscript ? <ChevronUp size={16} /> : <ChevronDown size={16} />}
          </button>

          {showTranscript && (
            <div className="audio-transcript-content">
              <div className="transcript-hint">
                <Sparkles size={12} />
                <span>Click any dialogue turn to narrate from that line</span>
              </div>

              {turns.map((turn) => {
                const isActive = currentTurnIdx === turn.id && isSpeaking;
                return (
                  <div
                    key={turn.id}
                    className={`transcript-turn-card ${isActive ? "active-turn" : ""}`}
                    onClick={() => handlePlaySpecificTurn(turn.id)}
                    title={`Click to play from ${turn.speaker}`}
                  >
                    <div className="turn-meta-header">
                      <span className="turn-speaker-badge">
                        <Mic size={11} /> {turn.speaker}
                      </span>
                      <button
                        type="button"
                        className="turn-play-btn"
                        aria-label={`Play turn ${turn.id + 1} by ${turn.speaker}`}
                      >
                        {isActive ? <Volume2 size={12} /> : <Play size={12} />}
                      </button>
                    </div>
                    <p className="turn-text">{turn.text}</p>
                  </div>
                );
              })}
            </div>
          )}
        </div>
      )}
    </div>
  );
};
