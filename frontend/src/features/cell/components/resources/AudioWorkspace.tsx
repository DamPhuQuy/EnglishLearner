import {
  AlertCircle,
  ArrowUp,
  Check,
  ChevronDown,
  ChevronUp,
  FileText,
  Headphones,
  Mic,
  Pause,
  Play,
  RotateCcw,
  Sparkles,
  Sliders,
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

export type VoicePersonaId =
  | "us-male-deep"
  | "uk-male-oxford"
  | "uk-female-bbc"
  | "us-female-clear"
  | "system-default";

export interface VoicePersona {
  id: VoicePersonaId;
  label: string;
  shortBadge: string;
  description: string;
  accent: "US" | "UK" | "System";
  targetLang: string;
  gender: "male" | "female" | "neutral";
  pitch: number;
  rateMultiplier: number;
}

export const VOICE_PERSONAS: VoicePersona[] = [
  {
    id: "us-male-deep",
    label: "US English Male (Warm & Deep Baritone)",
    shortBadge: "US Male · Deep & Clear",
    description: "Warm, resonant baritone with crisp American pronunciation",
    accent: "US",
    targetLang: "en-US",
    gender: "male",
    pitch: 0.82,
    rateMultiplier: 0.94,
  },
  {
    id: "uk-male-oxford",
    label: "UK English Male (Examiner Academic)",
    shortBadge: "UK Male · Deep RP",
    description: "Refined British RP baritone with academic cadence",
    accent: "UK",
    targetLang: "en-GB",
    gender: "male",
    pitch: 0.86,
    rateMultiplier: 0.95,
  },
  {
    id: "uk-female-bbc",
    label: "UK English Female (BBC Standard)",
    shortBadge: "UK Female · BBC",
    description: "Clear, warm standard British received pronunciation",
    accent: "UK",
    targetLang: "en-GB",
    gender: "female",
    pitch: 1.02,
    rateMultiplier: 0.98,
  },
  {
    id: "us-female-clear",
    label: "US English Female (Natural Clear)",
    shortBadge: "US Female · Clear",
    description: "Professional, articulate American broadcast cadence",
    accent: "US",
    targetLang: "en-US",
    gender: "female",
    pitch: 1.0,
    rateMultiplier: 1.0,
  },
  {
    id: "system-default",
    label: "System Default Voice (Offline Engine)",
    shortBadge: "Offline · Native",
    description: "Default voice provided directly by your operating system",
    accent: "System",
    targetLang: "en-US",
    gender: "neutral",
    pitch: 1.0,
    rateMultiplier: 1.0,
  },
];

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
  const [selectedPersonaId, setSelectedPersonaId] = useState<VoicePersonaId>("us-male-deep");
  const [speechError, setSpeechError] = useState<string>("");

  const activePersona = useMemo(() => {
    return (
      VOICE_PERSONAS.find((p) => p.id === selectedPersonaId) || VOICE_PERSONAS[0]
    );
  }, [selectedPersonaId]);

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

    const loadVoices = () => {
      const allVoices = window.speechSynthesis.getVoices();
      if (!allVoices || allVoices.length === 0) return;

      const englishVoices = allVoices.filter(
        (v) => v.lang.startsWith("en") || v.lang.startsWith("EN")
      );
      setVoices(englishVoices.length > 0 ? englishVoices : allVoices);
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

  // Find best matching voice for a persona
  const resolveVoiceForPersona = (persona: VoicePersona, isFemaleTurn: boolean) => {
    if (persona.id === "system-default" || voices.length === 0) {
      return null;
    }

    if (persona.id === "us-male-deep") {
      if (isFemaleTurn) {
        // Complementary female speaker in dialogue
        return (
          voices.find((v) => v.lang.startsWith("en-US") && /female|natural/i.test(v.name)) ||
          voices.find((v) => v.lang.startsWith("en-US")) ||
          null
        );
      }
      // Primary US English Male
      return (
        voices.find(
          (v) =>
            v.lang.startsWith("en-US") &&
            /male|david|aaron|guy|george|christopher|james|john/i.test(v.name)
        ) ||
        voices.find((v) => v.name.includes("US English")) ||
        voices.find((v) => v.lang.startsWith("en-US")) ||
        null
      );
    }

    if (persona.id === "uk-male-oxford") {
      if (isFemaleTurn) {
        return (
          voices.find((v) => v.lang.startsWith("en-GB") && /female/i.test(v.name)) ||
          voices.find((v) => v.lang.startsWith("en-GB")) ||
          null
        );
      }
      return (
        voices.find(
          (v) =>
            v.lang.startsWith("en-GB") &&
            /male|daniel|oliver|george|arthur/i.test(v.name)
        ) ||
        voices.find((v) => v.name.includes("UK English Male")) ||
        voices.find((v) => v.lang.startsWith("en-GB")) ||
        null
      );
    }

    if (persona.id === "uk-female-bbc") {
      return (
        voices.find((v) => v.lang.startsWith("en-GB") && /female/i.test(v.name)) ||
        voices.find((v) => v.name.includes("UK English Female")) ||
        voices.find((v) => v.lang.startsWith("en-GB")) ||
        null
      );
    }

    if (persona.id === "us-female-clear") {
      return (
        voices.find((v) => v.lang.startsWith("en-US") && /female/i.test(v.name)) ||
        voices.find((v) => v.lang.startsWith("en-US")) ||
        null
      );
    }

    return null;
  };

  // Speak a single turn safely with persona acoustic profile and automatic fallback
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

    if (window.speechSynthesis.paused) {
      window.speechSynthesis.resume();
    }

    const utterance = new SpeechSynthesisUtterance(currentTurn.text);

    // Apply speed multiplier from speed control and persona's clarity multiplier
    const effectiveRate = Number(speed) * activePersona.rateMultiplier;
    utterance.rate = Math.min(2.0, Math.max(0.5, effectiveRate));

    // Detect female speaker in dialogue
    const speakerLower = currentTurn.speaker.toLowerCase();
    const isFemaleTurn =
      /female|receptionist|chloe|sarah|emma|woman|wife|mary|linda/i.test(speakerLower);

    // If retryCount === 0 and persona is not offline system-default, try resolved voice
    if (retryCount === 0 && selectedPersonaId !== "system-default") {
      const voice = resolveVoiceForPersona(activePersona, isFemaleTurn);
      if (voice) {
        utterance.voice = voice;
      }

      if (isFemaleTurn && activePersona.gender === "male") {
        utterance.pitch = 1.05; // Slightly higher pitch for female speaker turn
      } else {
        // Apply persona's acoustic pitch (e.g. 0.82 for warm & deep US Male)
        utterance.pitch = activePersona.pitch;
      }
      utterance.lang = activePersona.targetLang;
    } else {
      // Default / offline engine fallback: still apply deep pitch and clear rate!
      utterance.pitch = isFemaleTurn ? 1.05 : activePersona.pitch;
      utterance.lang = activePersona.targetLang || "en-US";
    }

    utterance.onstart = () => {
      setIsSpeaking(true);
      setIsPaused(false);
    };

    utterance.onend = () => {
      if (isStoppedRef.current) return;
      if (turnIndex + 1 < turns.length) {
        // Natural dialogue turn pause (320ms)
        nextTurnTimerRef.current = window.setTimeout(() => {
          speakTurn(turnIndex + 1, 0);
        }, 320);
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

      // If remote cloud voice failed with synthesis-failed, transparently fallback to native engine with the same warm deep pitch
      if (
        e.error === "synthesis-failed" &&
        retryCount === 0 &&
        selectedPersonaId !== "system-default"
      ) {
        console.warn(
          "Cloud voice synthesis-failed. Auto-retrying with native engine using baritone profile..."
        );
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
              <span>AI Voice Narration</span>
              <span className="persona-badge" title={activePersona.description}>
                {activePersona.shortBadge}
              </span>
              {isSpeaking && !isPaused && (
                <div className="audio-live-waveform" title="Narration active">
                  <span className="wave-bar bar-1" />
                  <span className="wave-bar bar-2" />
                  <span className="wave-bar bar-3" />
                  <span className="wave-bar bar-4" />
                </div>
              )}
            </div>

            {/* Voice Persona Selector */}
            <div className="narration-persona-picker">
              <select
                value={selectedPersonaId}
                onChange={(e) => {
                  setSelectedPersonaId(e.target.value as VoicePersonaId);
                  setSpeechError("");
                }}
                className="voice-select persona-select"
                aria-label="Select speech persona"
                title="Select IELTS speaker accent and vocal tone"
              >
                {VOICE_PERSONAS.map((p) => (
                  <option key={p.id} value={p.id}>
                    {p.label}
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
                <span>Click any dialogue turn to narrate in US English Male (warm & deep)</span>
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
