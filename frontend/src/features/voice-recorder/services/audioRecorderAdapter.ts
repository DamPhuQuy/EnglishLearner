export interface RecordingResult {
  file: File;
  dataUrl: string;
}

export class BrowserAudioRecorderAdapter {
  private mediaRecorder: MediaRecorder | null = null;
  private mediaStream: MediaStream | null = null;
  private chunks: Blob[] = [];

  isSupported(): boolean {
    return Boolean(
      typeof navigator !== "undefined" &&
        typeof navigator.mediaDevices?.getUserMedia === "function" &&
        typeof window !== "undefined" &&
        typeof window.MediaRecorder === "function",
    );
  }

  isRecording(): boolean {
    return this.mediaRecorder?.state === "recording";
  }

  async startRecording(
    onDataChunk?: (size: number) => void,
    maxSizeBytes: number = 1.8 * 1024 * 1024,
  ): Promise<void> {
    if (!this.isSupported()) {
      throw new Error(
        "Audio recording is not supported in this browser. Please open in Chrome or Firefox over HTTPS or localhost.",
      );
    }

    try {
      this.mediaStream = await navigator.mediaDevices.getUserMedia({
        audio: true,
      });
      this.chunks = [];
      let totalSize = 0;

      const recorder = new MediaRecorder(this.mediaStream);
      this.mediaRecorder = recorder;

      recorder.ondataavailable = (event: BlobEvent) => {
        if (event.data && event.data.size > 0) {
          this.chunks.push(event.data);
          totalSize += event.data.size;
          onDataChunk?.(totalSize);
          if (totalSize >= maxSizeBytes && recorder.state === "recording") {
            recorder.stop();
          }
        }
      };

      recorder.start(1000);
    } catch {
      this.cleanupStream();
      throw new Error(
        "Could not access microphone. Please allow microphone permissions in your browser and try again.",
      );
    }
  }

  stopRecording(): Promise<RecordingResult> {
    return new Promise((resolve, reject) => {
      const recorder = this.mediaRecorder;
      if (!recorder || recorder.state !== "recording") {
        this.cleanupStream();
        reject(new Error("No active audio recording found."));
        return;
      }

      recorder.onstop = () => {
        try {
          const mimeType = recorder.mimeType || "audio/webm";
          const dateStr = new Date().toISOString().slice(0, 10);
          const file = new File(this.chunks, `Speaking-${dateStr}.webm`, {
            type: mimeType,
          });

          if (file.size > 2 * 1024 * 1024) {
            throw new Error(
              "Recording is too large or could not be read. Please record a shorter audio segment.",
            );
          }

          const reader = new FileReader();
          reader.onload = () => {
            const dataUrl = String(reader.result);
            this.cleanupStream();
            resolve({ file, dataUrl });
          };
          reader.onerror = () => {
            this.cleanupStream();
            reject(new Error("Could not read recorded audio data."));
          };
          reader.readAsDataURL(file);
        } catch (err) {
          this.cleanupStream();
          reject(err);
        }
      };

      recorder.stop();
    });
  }

  cancelRecording(): void {
    if (this.mediaRecorder && this.mediaRecorder.state === "recording") {
      this.mediaRecorder.onstop = null;
      this.mediaRecorder.stop();
    }
    this.cleanupStream();
  }

  private cleanupStream(): void {
    if (this.mediaStream) {
      this.mediaStream.getTracks().forEach((track) => track.stop());
      this.mediaStream = null;
    }
    this.mediaRecorder = null;
    this.chunks = [];
  }
}
