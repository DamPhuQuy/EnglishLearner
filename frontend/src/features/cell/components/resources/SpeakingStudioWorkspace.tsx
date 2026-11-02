import {
  Clock,
  HelpCircle,
  Mic,
  Sparkles,
} from "lucide-react";
import React, { useEffect, useState } from "react";
import type { IeltsSpeakingTaskData } from "../../types/ieltsSchema.ts";
import { VoiceRecorderWorkspace } from "../../../voice-recorder/index.ts";

export interface SpeakingStudioWorkspaceProps {
  speakingTask: IeltsSpeakingTaskData;
  title: string;
  difficulty?: string;
  recording: boolean;
  seconds: number;
  disabled?: boolean;
  onStartRecording: () => void;
  onStopRecording: () => void;
}

export const SpeakingStudioWorkspace: React.FC<SpeakingStudioWorkspaceProps> = ({
  speakingTask,
  title,
  difficulty,
  recording,
  seconds,
  disabled,
  onStartRecording,
  onStopRecording,
}) => {
  const [prepTimer, setPrepTimer] = useState<number | null>(null);
  const [speakTimer, setSpeakTimer] = useState<number | null>(null);

  useEffect(() => {
    let interval: number | undefined;
    if (prepTimer !== null && prepTimer > 0) {
      interval = window.setInterval(() => {
        setPrepTimer((t) => (t !== null && t > 0 ? t - 1 : 0));
      }, 1000);
    }
    return () => clearInterval(interval);
  }, [prepTimer]);

  useEffect(() => {
    let interval: number | undefined;
    if (speakTimer !== null && speakTimer > 0) {
      interval = window.setInterval(() => {
        setSpeakTimer((t) => (t !== null && t > 0 ? t - 1 : 0));
      }, 1000);
    }
    return () => clearInterval(interval);
  }, [speakTimer]);

  return (
    <div className="speaking-studio-workspace">
      {/* Header bar */}
      <div className="speaking-studio-header">
        <div className="speaking-studio-badge">
          <Mic size={13} />
          <span>IELTS SPEAKING PART {speakingTask.part}</span>
        </div>
        {difficulty && <span className="speaking-diff-tag">{difficulty}</span>}
      </div>

      <div className="speaking-studio-topic-row">
        <h3 className="speaking-studio-title">{title}</h3>
        <span className="speaking-topic-pill">Topic: {speakingTask.topic}</span>
      </div>

      {/* Part 1 Questions */}
      {speakingTask.part === 1 && speakingTask.part1Questions && (
        <div className="speaking-prompt-card">
          <div className="prompt-card-label">
            <HelpCircle size={13} />
            <span>Examiner Interview Questions:</span>
          </div>
          <ol className="speaking-questions-ol">
            {speakingTask.part1Questions.map((q) => (
              <li key={q.questionNumber}>{q.question}</li>
            ))}
          </ol>
        </div>
      )}

      {/* Part 2 Cue Card */}
      {speakingTask.part === 2 && speakingTask.cueCard && (
        <div className="speaking-cuecard-card">
          <div className="cuecard-header">
            <h4>{speakingTask.cueCard.title}</h4>
            <span className="cuecard-hint">You should say:</span>
          </div>
          <ul className="cuecard-bullets">
            {speakingTask.cueCard.bulletPoints.map((pt, i) => (
              <li key={i}>{pt}</li>
            ))}
          </ul>
          {speakingTask.cueCard.roundingOffQuestion && (
            <p className="cuecard-rounding">
              <strong>Follow-up question:</strong> {speakingTask.cueCard.roundingOffQuestion}
            </p>
          )}

          {/* Timers */}
          <div className="cuecard-timer-row">
            <div className="timer-unit">
              <button
                type="button"
                className="button quiet small"
                onClick={() => setPrepTimer(60)}
                disabled={disabled}
              >
                <Clock size={12} />
                <span>1-Min Prep</span>
              </button>
              {prepTimer !== null && (
                <span className={`timer-num ${prepTimer <= 10 ? "urgent" : ""}`}>
                  {prepTimer}s
                </span>
              )}
            </div>

            <div className="timer-unit">
              <button
                type="button"
                className="button quiet small"
                onClick={() => setSpeakTimer(120)}
                disabled={disabled}
              >
                <Clock size={12} />
                <span>2-Min Talk</span>
              </button>
              {speakTimer !== null && (
                <span className={`timer-num ${speakTimer <= 15 ? "urgent" : ""}`}>
                  {Math.floor(speakTimer / 60)}:{(speakTimer % 60).toString().padStart(2, "0")}
                </span>
              )}
            </div>
          </div>
        </div>
      )}

      {/* Part 3 Questions */}
      {speakingTask.part === 3 && speakingTask.part3Questions && (
        <div className="speaking-prompt-card">
          <div className="prompt-card-label">
            <HelpCircle size={13} />
            <span>Two-Way In-Depth Discussion:</span>
          </div>
          <ol className="speaking-questions-ol">
            {speakingTask.part3Questions.map((q) => (
              <li key={q.questionNumber}>{q.question}</li>
            ))}
          </ol>
        </div>
      )}

      {/* Recommended Idioms & Collocations */}
      {speakingTask.recommendedIdioms && speakingTask.recommendedIdioms.length > 0 && (
        <div className="speaking-idioms-section">
          <div className="idioms-header">
            <Sparkles size={13} className="text-amber-400" />
            <span>High-Scoring Lexical Collocations & Idioms:</span>
          </div>
          <div className="idioms-grid">
            {speakingTask.recommendedIdioms.map((idm, i) => (
              <div key={i} className="idiom-chip">
                <span className="idiom-phrase">{idm.phrase}</span>
                <span className="idiom-def">{idm.meaning}</span>
                {idm.example && <span className="idiom-ex">"{idm.example}"</span>}
              </div>
            ))}
          </div>
        </div>
      )}

      {/* Integrated Voice Recorder Studio */}
      <div className="speaking-recorder-wrapper">
        <VoiceRecorderWorkspace
          recording={recording}
          seconds={seconds}
          disabled={Boolean(disabled)}
          onStart={onStartRecording}
          onStop={onStopRecording}
        />
      </div>
    </div>
  );
};
