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
  Sliders,
  Square,
  Users,
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
    shortBadge: "US Male · Deep",
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
    shortBadge: "UK Male · Oxford",
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
    shortBadge: "Offline Native",
    description: "Default voice provided directly by your operating system",
    accent: "System",
    targetLang: "en-US",
    gender: "neutral",
    pitch: 1.0,
    rateMultiplier: 1.0,
  },
];

export interface SpeakerColorPalette {
  name: string;
  badgeBg: string;
  badgeText: string;
  border: string;
  glow: string;
}

export const SPEAKER_PALETTES: SpeakerColorPalette[] = [
  {
    name: "purple",
    badgeBg: "rgba(168, 85, 247, 0.16)",
    badgeText: "#d8b4fe",
    border: "rgba(168, 85, 247, 0.45)",
    glow: "rgba(168, 85, 247, 0.25)",
  },
  {
    name: "blue",
    badgeBg: "rgba(59, 130, 246, 0.16)",
    badgeText: "#93c5fd",
    border: "rgba(59, 130, 246, 0.45)",
    glow: "rgba(59, 130, 246, 0.25)",
  },
  {
    name: "emerald",
    badgeBg: "rgba(16, 185, 129, 0.16)",
    badgeText: "#6ee7b7",
    border: "rgba(16, 185, 129, 0.45)",
    glow: "rgba(16, 185, 129, 0.25)",
  },
  {
    name: "amber",
    badgeBg: "rgba(245, 158, 11, 0.16)",
    badgeText: "#fcd34d",
    border: "rgba(245, 158, 11, 0.45)",
    glow: "rgba(245, 158, 11, 0.25)",
  },
];

export interface SpeakerVoiceConfig {
  name: string;
  personaId: VoicePersonaId;
  pitch: number;
  rateMultiplier: number;
  palette: SpeakerColorPalette;
}

export const AudioWorkspace: React.FC<Props> = ({ url, transcript, onError }) => {
  const audioRef = useRef<HTMLAudioElement>(null);
  const activeUtteranceRef = useRef<SpeechSynthesisUtterance | null>(null);
  const isStoppedRef = useRef(false);
  const nextTurnTimerRef = useRef<number | null>(null);

  const [speed, setSpeed] = useState("1");
  const [showTranscript, setShowTranscript] = useState(true);
  const [showCastManager, setShowCastManager] = useState(true);
  const [isSpeaking, setIsSpeaking] = useState(false);
  const [isPaused, setIsPaused] = useState(false);
  const [currentTurnIdx, setCurrentTurnIdx] = useState<number | null>(null);
  const [voices, setVoices] = useState<SpeechSynthesisVoice[]>([]);
  const [speechError, setSpeechError] = useState<string>("");
  const [previewingSpeaker, setPreviewingSpeaker] = useState<string | null>(null);

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

  // Extract unique speaker list
  const uniqueSpeakers = useMemo(() => {
    return Array.from(new Set(turns.map((t) => t.speaker)));
  }, [turns]);

  // Speaker cast voice allocation state
  const [speakerConfigs, setSpeakerConfigs] = useState<Record<string, SpeakerVoiceConfig>>({});

  // Auto-allocate complementary voices when speakers change
  useEffect(() => {
    if (uniqueSpeakers.length === 0) return;

    setSpeakerConfigs((prev) => {
      const next: Record<string, SpeakerVoiceConfig> = {};

      uniqueSpeakers.forEach((name, idx) => {
        // If user already customized this speaker, preserve their choice
        if (prev[name]) {
          next[name] = prev[name];
          return;
        }

        const lower = name.toLowerCase();
        const isFemale = /female|receptionist|chloe|sarah|emma|woman|wife|mary|linda|advisor|clerk/i.test(
          lower
        );
        const isAcademic = /dr\.|professor|tutor|lecturer|patel|teacher/i.test(lower);

        let personaId: VoicePersonaId;
        let pitch: number;
        let rateMultiplier: number;

        if (isFemale) {
          personaId = idx % 2 === 0 ? "uk-female-bbc" : "us-female-clear";
          pitch = 1.04;
          rateMultiplier = 0.98;
        } else if (isAcademic) {
          personaId = "uk-male-oxford";
          pitch = 0.88;
          rateMultiplier = 0.95;
        } else {
          // Primary Male: US English Male warm & deep baritone
          personaId = "us-male-deep";
          pitch = 0.82;
          rateMultiplier = 0.94;
        }

        // If 2 speakers and both are male/neutral, ensure Speaker 1 and 2 sound distinctly different
        if (uniqueSpeakers.length >= 2 && idx === 1 && !isFemale && !isAcademic) {
          if (next[uniqueSpeakers[0]]?.personaId === "us-male-deep") {
            personaId = "uk-male-oxford";
            pitch = 0.90;
            rateMultiplier = 0.96;
          }
        }

        const palette = SPEAKER_PALETTES[idx % SPEAKER_PALETTES.length];

        next[name] = {
          name,
          personaId,
          pitch,
          rateMultiplier,
          palette,
        };
      });

      return next;
    });
  }, [uniqueSpeakers]);

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
          // ignore
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

  // Find best matching browser voice for a specific persona
  const resolveVoiceForPersona = (personaId: VoicePersonaId) => {
    if (personaId === "system-default" || voices.length === 0) {
      return null;
    }

    if (personaId === "us-male-deep") {
      return (
        voices.find(
          (v) =>
            v.lang.startsWith("en-US") &&
            /male|david|aaron|guy|george|christopher|natural/i.test(v.name)
        ) ||
        voices.find((v) => v.name.includes("US English")) ||
        voices.find((v) => v.lang.startsWith("en-US")) ||
        null
      );
    }

    if (personaId === "uk-male-oxford") {
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

    if (personaId === "uk-female-bbc") {
      return (
        voices.find((v) => v.lang.startsWith("en-GB") && /female/i.test(v.name)) ||
        voices.find((v) => v.name.includes("UK English Female")) ||
        voices.find((v) => v.lang.startsWith("en-GB")) ||
        null
      );
    }

    if (personaId === "us-female-clear") {
      return (
        voices.find((v) => v.lang.startsWith("en-US") && /female/i.test(v.name)) ||
        voices.find((v) => v.lang.startsWith("en-US")) ||
        null
      );
    }

    return null;
  };

  // Update a speaker's assigned persona
  const handleUpdateSpeakerPersona = (speakerName: string, newPersonaId: VoicePersonaId) => {
    const persona = VOICE_PERSONAS.find((p) => p.id === newPersonaId) || VOICE_PERSONAS[0];
    setSpeakerConfigs((prev) => ({
      ...prev,
      [speakerName]: {
        ...prev[speakerName],
        personaId: newPersonaId,
        pitch: persona.pitch,
        rateMultiplier: persona.rateMultiplier,
      },
    }));
    setSpeechError("");
  };

  // Preview a specific speaker's voice with a short greeting
  const handleTestSpeakerVoice = (speakerName: string) => {
    if (typeof window === "undefined" || !("speechSynthesis" in window)) return;

    window.speechSynthesis.cancel();
    setPreviewingSpeaker(speakerName);

    const config = speakerConfigs[speakerName];
    const persona = VOICE_PERSONAS.find((p) => p.id === config?.personaId) || VOICE_PERSONAS[0];
    const utterance = new SpeechSynthesisUtterance(
      `Hello! I am ${speakerName}, ready for the IELTS listening test.`
    );

    utterance.rate = Number(speed) * persona.rateMultiplier;
    utterance.pitch = config?.pitch ?? persona.pitch;
    utterance.lang = persona.targetLang || "en-US";

    const voice = resolveVoiceForPersona(persona.id);
    if (voice) {
      utterance.voice = voice;
    }

    utterance.onend = () => setPreviewingSpeaker(null);
    utterance.onerror = () => setPreviewingSpeaker(null);

    window.speechSynthesis.speak(utterance);
  };

  // Speak a single turn safely using its dedicated speaker configuration
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

    const speakerConfig = speakerConfigs[currentTurn.speaker];
    const persona =
      VOICE_PERSONAS.find((p) => p.id === speakerConfig?.personaId) || VOICE_PERSONAS[0];

    const utterance = new SpeechSynthesisUtterance(currentTurn.text);

    // Apply combined speed and persona clarity rate
    const effectiveRate = Number(speed) * (speakerConfig?.rateMultiplier ?? persona.rateMultiplier);
    utterance.rate = Math.min(2.0, Math.max(0.5, effectiveRate));

    // Apply speaker's calibrated acoustic pitch (e.g. 0.82 for deep baritone, 1.04 for female)
    utterance.pitch = speakerConfig?.pitch ?? persona.pitch;
    utterance.lang = persona.targetLang || "en-US";

    // Bind browser voice if not retrying and not system-default
    if (retryCount === 0 && persona.id !== "system-default") {
      const voice = resolveVoiceForPersona(persona.id);
      if (voice) {
        utterance.voice = voice;
      }
    }

    utterance.onstart = () => {
      setIsSpeaking(true);
      setIsPaused(false);
    };

    utterance.onend = () => {
      if (isStoppedRef.current) return;
      if (turnIndex + 1 < turns.length) {
        // Natural conversational pause between turns (340ms)
        nextTurnTimerRef.current = window.setTimeout(() => {
          speakTurn(turnIndex + 1, 0);
        }, 340);
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

      // Transparent retry on native offline engine with speaker's distinct pitch preserved
      if (e.error === "synthesis-failed" && retryCount === 0) {
        console.warn(
          `Voice failed for ${currentTurn.speaker}. Auto-retrying with native engine using baritone profile...`
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

  const activeTurn = currentTurnIdx !== null ? turns[currentTurnIdx] : null;
  const activeSpeakerConfig = activeTurn ? speakerConfigs[activeTurn.speaker] : null;

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
              // Gracefully handle remote audio failure
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
              <span>Multi-Speaker Narration Studio</span>

              {/* Active speaker spotlight badge during narration */}
              {isSpeaking && activeTurn && activeSpeakerConfig && (
                <div
                  className="active-speaker-spotlight"
                  style={{
                    backgroundColor: activeSpeakerConfig.palette.badgeBg,
                    color: activeSpeakerConfig.palette.badgeText,
                    borderColor: activeSpeakerConfig.palette.border,
                  }}
                >
                  <Mic size={11} />
                  <span>
                    Speaking: <strong>{activeTurn.speaker}</strong>
                  </span>
                  <div className="audio-live-waveform" title="Speaking active">
                    <span
                      className="wave-bar bar-1"
                      style={{ backgroundColor: activeSpeakerConfig.palette.badgeText }}
                    />
                    <span
                      className="wave-bar bar-2"
                      style={{ backgroundColor: activeSpeakerConfig.palette.badgeText }}
                    />
                    <span
                      className="wave-bar bar-3"
                      style={{ backgroundColor: activeSpeakerConfig.palette.badgeText }}
                    />
                    <span
                      className="wave-bar bar-4"
                      style={{ backgroundColor: activeSpeakerConfig.palette.badgeText }}
                    />
                  </div>
                </div>
              )}
            </div>

            {/* Toggle Cast Voice Manager */}
            {uniqueSpeakers.length > 0 && (
              <button
                type="button"
                className={`cast-toggle-btn ${showCastManager ? "active" : ""}`}
                onClick={() => setShowCastManager(!showCastManager)}
                title="Configure voice persona for each character"
              >
                <Users size={13} />
                <span>Cast & Voices ({uniqueSpeakers.length})</span>
                {showCastManager ? <ChevronUp size={13} /> : <ChevronDown size={13} />}
              </button>
            )}
          </div>

          {/* Interactive Multi-Speaker Voice Allocation Strip */}
          {showCastManager && uniqueSpeakers.length > 0 && (
            <div className="speaker-cast-manager">
              <div className="cast-manager-header">
                <span className="cast-manager-title">
                  <Sliders size={12} />
                  Character Voice Roles (Hội thoại đa nhân vật)
                </span>
                <span className="cast-manager-hint">
                  Customize the voice actor and accent for each speaker
                </span>
              </div>

              <div className="speaker-cast-grid">
                {uniqueSpeakers.map((speakerName) => {
                  const cfg = speakerConfigs[speakerName];
                  const persona =
                    VOICE_PERSONAS.find((p) => p.id === cfg?.personaId) || VOICE_PERSONAS[0];
                  const isPreviewing = previewingSpeaker === speakerName;

                  return (
                    <div
                      key={speakerName}
                      className="speaker-cast-card"
                      style={{
                        borderColor: cfg?.palette.border || "var(--line)",
                        boxShadow:
                          activeTurn?.speaker === speakerName && isSpeaking
                            ? `0 0 0 1px ${cfg?.palette.border}, 0 0 12px ${cfg?.palette.glow}`
                            : undefined,
                      }}
                    >
                      <div className="speaker-card-header">
                        <span
                          className="speaker-avatar-badge"
                          style={{
                            backgroundColor: cfg?.palette.badgeBg,
                            color: cfg?.palette.badgeText,
                            borderColor: cfg?.palette.border,
                          }}
                        >
                          <Mic size={11} />
                          {speakerName}
                        </span>

                        <button
                          type="button"
                          className={`speaker-test-btn ${isPreviewing ? "testing" : ""}`}
                          onClick={() => handleTestSpeakerVoice(speakerName)}
                          title={`Test voice for ${speakerName}`}
                        >
                          {isPreviewing ? <Volume2 size={11} /> : <Play size={11} />}
                          <span>{isPreviewing ? "Testing…" : "Test"}</span>
                        </button>
                      </div>

                      <select
                        value={cfg?.personaId || "us-male-deep"}
                        onChange={(e) =>
                          handleUpdateSpeakerPersona(
                            speakerName,
                            e.target.value as VoicePersonaId
                          )
                        }
                        className="speaker-persona-select"
                        aria-label={`Select voice persona for ${speakerName}`}
                        title={`Choose accent and tone for ${speakerName}`}
                      >
                        {VOICE_PERSONAS.map((p) => (
                          <option key={p.id} value={p.id}>
                            {p.label}
                          </option>
                        ))}
                      </select>
                    </div>
                  );
                })}
              </div>
            </div>
          )}

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
                  <Play size={14} /> Play Multi-Speaker Audio
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
                <span>
                  Click any dialogue turn to narrate in that character's designated voice
                </span>
              </div>

              {turns.map((turn) => {
                const isActive = currentTurnIdx === turn.id && isSpeaking;
                const spkConfig = speakerConfigs[turn.speaker];
                const palette = spkConfig?.palette || SPEAKER_PALETTES[0];

                return (
                  <div
                    key={turn.id}
                    className={`transcript-turn-card ${isActive ? "active-turn" : ""}`}
                    style={
                      isActive
                        ? {
                            borderColor: palette.border,
                            backgroundColor: palette.badgeBg,
                            boxShadow: `0 0 0 1px ${palette.border}, 0 0 10px ${palette.glow}`,
                          }
                        : undefined
                    }
                    onClick={() => handlePlaySpecificTurn(turn.id)}
                    title={`Click to play from ${turn.speaker}`}
                  >
                    <div className="turn-meta-header">
                      <span
                        className="turn-speaker-badge"
                        style={{
                          backgroundColor: palette.badgeBg,
                          color: palette.badgeText,
                          borderColor: palette.border,
                        }}
                      >
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
