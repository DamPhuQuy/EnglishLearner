import { useEffect, useRef, useState } from "react";
import { BrowserAudioRecorderAdapter } from "../services/audioRecorderAdapter.ts";

export interface VoiceRecorderState {
  recording: boolean;
  seconds: number;
  busy: boolean;
  error: string;
  start: () => Promise<string | undefined>;
  stop: () => void;
  clearError: () => void;
}

export function useVoiceRecorder(
  onRecorded?: (dataUrl: string, fileName: string) => void,
): VoiceRecorderState {
  const [recording, setRecording] = useState(false);
  const [seconds, setSeconds] = useState(0);
  const [busy, setBusy] = useState(false);
  const [error, setError] = useState("");

  const recorderRef = useRef<BrowserAudioRecorderAdapter | null>(null);
  const timerRef = useRef<number | undefined>(undefined);
  const aliveRef = useRef(true);

  if (!recorderRef.current) {
    recorderRef.current = new BrowserAudioRecorderAdapter();
  }

  useEffect(() => {
    aliveRef.current = true;
    return () => {
      aliveRef.current = false;
      window.clearInterval(timerRef.current);
      recorderRef.current?.cancelRecording();
    };
  }, []);

  const clearError = () => setError("");

  const start = async (): Promise<string | undefined> => {
    setError("");
    const recorder = recorderRef.current;
    if (!recorder || !recorder.isSupported()) {
      setError(
        "Audio recording is not supported in this browser. Please open in Chrome or Firefox over HTTPS or localhost.",
      );
      return undefined;
    }

    setBusy(true);
    try {
      await recorder.startRecording(() => {
        // onChunk callback
      });
      if (!aliveRef.current) {
        recorder.cancelRecording();
        return undefined;
      }
      setRecording(true);
      setSeconds(0);
      timerRef.current = window.setInterval(() => {
        if (aliveRef.current) setSeconds((n) => n + 1);
      }, 1000);
      return undefined;
    } catch (err) {
      if (aliveRef.current) {
        setError(
          err instanceof Error
            ? err.message
            : "Could not access microphone. Please allow microphone permissions in your browser and try again.",
        );
      }
      return undefined;
    } finally {
      if (aliveRef.current) setBusy(false);
    }
  };

  const stop = async () => {
    const recorder = recorderRef.current;
    if (!recorder || !recorder.isRecording()) return;

    window.clearInterval(timerRef.current);
    setRecording(false);
    setBusy(true);

    try {
      const result = await recorder.stopRecording();
      if (aliveRef.current) {
        onRecorded?.(result.dataUrl, result.file.name);
      }
    } catch (err) {
      if (aliveRef.current) {
        setError(
          err instanceof Error
            ? err.message
            : "Recording is too large or could not be read. Please record a shorter audio segment.",
        );
      }
    } finally {
      if (aliveRef.current) setBusy(false);
    }
  };

  return {
    recording,
    seconds,
    busy,
    error,
    start,
    stop,
    clearError,
  };
}
