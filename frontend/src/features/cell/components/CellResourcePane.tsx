import { Paperclip, X } from "lucide-react";
import React, { useRef, useState } from "react";
import type { CellResource, SkillType } from "../../notebook/types/notebook.ts";
import { defaultNotebookFileAdapter } from "../../notebook/services/notebookFile.ts";
import { defaultNotebookApiClient } from "../../notebook/services/notebookApiClient.ts";
import { useVoiceRecorder, VoiceRecorderWorkspace } from "../../voice-recorder/index.ts";
import { SKILL_RESOURCE_LABELS } from "../services/skillTemplates.ts";
import { AudioUrlForm } from "./resources/AudioUrlForm.tsx";
import { AudioWorkspace } from "./resources/AudioWorkspace.tsx";
import { EmptyResourceWorkspace } from "./resources/EmptyResourceWorkspace.tsx";
import { ImageWorkspace } from "./resources/ImageWorkspace.tsx";
import { PdfWorkspace } from "./resources/PdfWorkspace.tsx";
import { TextWorkspace } from "./resources/TextWorkspace.tsx";

export interface CellResourcePaneProps {
  cellId: string;
  cellType: SkillType;
  resource?: CellResource;
  onUpdateResource: (resource: CellResource | undefined) => void;
}

export const CellResourcePane: React.FC<CellResourcePaneProps> = ({
  cellId,
  cellType,
  resource,
  onUpdateResource,
}) => {
  const fileInputRef = useRef<HTMLInputElement>(null);
  const [dragging, setDragging] = useState(false);
  const [busy, setBusy] = useState(false);
  const [error, setError] = useState("");

  const resourceTitle = SKILL_RESOURCE_LABELS[cellType] ?? "Attached Document";
  const isStaleBlob = Boolean(resource?.url?.startsWith("blob:"));

  const recorder = useVoiceRecorder(async (dataUrl, fileName, file) => {
    onUpdateResource({
      type: "audio",
      name: fileName,
      url: dataUrl,
    });

    if (file) {
      try {
        const uploadResult = await defaultNotebookApiClient.uploadFile(file, fileName);
        if (uploadResult?.url) {
          onUpdateResource({
            type: "audio",
            name: fileName,
            url: uploadResult.url,
          });
        }
      } catch (uploadErr) {
        console.warn("Could not upload recording to Cloudflare R2, using local audio data:", uploadErr);
      }
    }
  });

  const attachFile = async (file: File) => {
    setError("");
    setBusy(true);
    try {
      const isText =
        file.type.startsWith("text/") ||
        file.name.endsWith(".txt") ||
        file.name.endsWith(".md");

      if (isText) {
        const textContent = await file.text();
        onUpdateResource({
          type: "text",
          name: file.name,
          textContent,
        });
        return;
      }

      // Try uploading binary asset (audio/pdf/image) to Cloudflare R2
      try {
        const uploaded = await defaultNotebookApiClient.uploadFile(file);
        let resType: "audio" | "image" | "pdf" | "none" = "none";
        if (file.type.startsWith("audio/")) resType = "audio";
        else if (file.type.startsWith("image/")) resType = "image";
        else if (file.type.includes("pdf") || file.name.endsWith(".pdf")) resType = "pdf";

        onUpdateResource({
          type: resType,
          name: file.name,
          url: uploaded.url,
        });
        return;
      } catch (uploadErr) {
        console.info("R2 upload fallback to local reader:", uploadErr);
      }

      const res = await defaultNotebookFileAdapter.readFileAsResource(file);
      onUpdateResource(res);
    } catch (err) {
      setError(
        err instanceof Error ? err.message : "Could not read file. Please try again.",
      );
    } finally {
      setBusy(false);
    }
  };

  const handleStartRecording = async () => {
    if (
      resource?.type === "audio" &&
      !confirm("Recording a new audio will replace the current audio file in this cell. Continue?")
    ) {
      return;
    }
    await recorder.start();
  };

  const isInteracting = busy || recorder.busy || recorder.recording;

  return (
    <div
      className={`resource-pane ${dragging ? "dragging" : ""}`}
      onDragOver={(e) => {
        e.preventDefault();
        setDragging(true);
      }}
      onDragLeave={(e) => {
        if (!e.currentTarget.contains(e.relatedTarget as Node)) {
          setDragging(false);
        }
      }}
      onDrop={(e) => {
        e.preventDefault();
        setDragging(false);
        if (!isInteracting && e.dataTransfer.files[0]) {
          void attachFile(e.dataTransfer.files[0]);
        }
      }}
    >
      <div className="pane-heading">
        <span>{resourceTitle}</span>
        <div className="attachment-actions">
          <input
            hidden
            type="file"
            accept="audio/*,.pdf,.png,.jpg,.jpeg,.webp,.gif,.txt,.md"
            ref={fileInputRef}
            onChange={(e) => {
              if (e.target.files?.[0]) void attachFile(e.target.files[0]);
              e.target.value = "";
            }}
          />
          <button
            className="button quiet"
            disabled={isInteracting}
            onClick={() => fileInputRef.current?.click()}
          >
            <Paperclip size={14} />
            {resource && resource.type !== "voice_recorder"
              ? "Replace file"
              : "Attach"}
          </button>
          {resource && resource.type !== "voice_recorder" && (
            <button
              className="icon-button"
              disabled={isInteracting}
              aria-label="Remove attached document"
              onClick={() => {
                if (confirm("Remove attached document from this cell?")) {
                  onUpdateResource(undefined);
                }
              }}
            >
              <X size={15} />
            </button>
          )}
        </div>
      </div>

      {(busy || recorder.busy) && (
        <output className="resource-status">
          Processing…
        </output>
      )}

      {(error || recorder.error) && (
        <p className="resource-error" role="alert">
          {error || recorder.error}
        </p>
      )}

      {isStaleBlob ? (
        <div className="resource-empty">
          <Paperclip size={23} />
          <p>Previous file needs to be re-attached</p>
          <span>
            Session link has expired. Please select the file again to save with your
            notebook.
          </span>
        </div>
      ) : resource &&
        !["voice_recorder", "none"].includes(resource.type) ? (
        <div className="resource-body">
          <div className="resource-filename" title={resource.name}>
            {resource.name || "Attached Document"}
          </div>
          {resource.type === "audio" && resource.url && (
            <AudioWorkspace url={resource.url} onError={setError} />
          )}
          {resource.type === "pdf" && resource.url && (
            <PdfWorkspace url={resource.url} name={resource.name} />
          )}
          {resource.type === "image" && resource.url && (
            <ImageWorkspace url={resource.url} name={resource.name} />
          )}
          {resource.type === "text" && (
            <TextWorkspace content={resource.textContent} />
          )}
        </div>
      ) : (
        cellType !== "speaking" && (
          <EmptyResourceWorkspace
            disabled={isInteracting}
            onSelectFile={() => fileInputRef.current?.click()}
          />
        )
      )}

      {cellType === "listening" && !resource?.url && (
        <AudioUrlForm
          cellId={cellId}
          disabled={isInteracting}
          onSubmitUrl={(audioUrl) => {
            onUpdateResource({
              type: "audio",
              name: "Audio track from URL",
              url: audioUrl,
            });
            setError("");
          }}
          onError={setError}
        />
      )}

      {cellType === "speaking" && (
        <VoiceRecorderWorkspace
          recording={recorder.recording}
          seconds={recorder.seconds}
          disabled={isInteracting}
          onStart={handleStartRecording}
          onStop={recorder.stop}
        />
      )}
    </div>
  );
};
