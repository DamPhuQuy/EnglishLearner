import { useEffect, useRef, useState } from "react";
import {
  addCellAt,
  createCell,
  executeCellInList,
  moveCell,
  patchCell,
  removeCellById,
  type CellResource,
  type JupyterCell,
  type JupyterNotebookDoc,
  type SkillType,
} from "../types/notebook.ts";
import { appendTemplateToSource } from "../../cell/services/skillTemplates.ts";
import {
  BrowserNotebookFileAdapter,
  defaultNotebookFileAdapter,
} from "../services/notebookFile.ts";
import {
  defaultNotebookStorage,
  LocalStorageNotebookStorage,
} from "../services/notebookStorage.ts";
import { sampleNotebook } from "../data/initialSampleNotebook.ts";

export type SaveState = "saving" | "saved" | "error";

interface UseNotebookOptions {
  storage?: LocalStorageNotebookStorage;
  fileAdapter?: BrowserNotebookFileAdapter;
}

export function useNotebook(options?: UseNotebookOptions) {
  const storage = options?.storage ?? defaultNotebookStorage;
  const filePort = options?.fileAdapter ?? defaultNotebookFileAdapter;

  const [initial] = useState(() => {
    try {
      const saved = storage.load();
      if (saved) return { doc: saved, error: "" };
      return { doc: structuredClone(sampleNotebook), error: "" };
    } catch {
      return {
        doc: structuredClone(sampleNotebook),
        error:
          "Unable to read notebook from browser storage. Loading default sample; import a previously exported file if you need to restore your work.",
      };
    }
  });

  const [doc, setDoc] = useState<JupyterNotebookDoc>(initial.doc);
  const [loadError, setLoadError] = useState(initial.error);
  const [activeId, setActiveId] = useState(doc.cells[0]?.id ?? "");
  const [saveState, setSaveState] = useState<SaveState>("saving");
  const [deleted, setDeleted] = useState<{
    cell: JupyterCell;
    index: number;
  } | null>(null);

  const pendingFocus = useRef<string | null>(null);

  // Auto-save debounce
  useEffect(() => {
    setSaveState("saving");
    const timer = window.setTimeout(() => {
      try {
        storage.save(doc);
        setSaveState("saved");
      } catch {
        setSaveState("error");
      }
    }, 350);
    return () => window.clearTimeout(timer);
  }, [doc, storage]);

  // Pagehide fallback save
  useEffect(() => {
    const handleSave = () => {
      try {
        storage.save(doc);
      } catch {
        /* handled above */
      }
    };
    window.addEventListener("pagehide", handleSave);
    return () => {
      window.removeEventListener("pagehide", handleSave);
      handleSave();
    };
  }, [doc, storage]);

  // Focus pending cell editor
  useEffect(() => {
    if (pendingFocus.current) {
      document.getElementById(`editor-${pendingFocus.current}`)?.focus();
      pendingFocus.current = null;
    }
  }, [doc, activeId]);

  const patch = (id: string, change: Partial<JupyterCell>) => {
    setDoc((prev) => ({
      ...prev,
      cells: patchCell(prev.cells, id, change),
    }));
  };

  const add = (index: number, skill: SkillType = "markdown") => {
    const newCell = createCell(skill);
    pendingFocus.current = newCell.id;
    setDoc((prev) => ({
      ...prev,
      cells: addCellAt(prev.cells, index, newCell),
    }));
    setActiveId(newCell.id);
  };

  const run = (id: string) => {
    setDoc((prev) => {
      const { cells, nextActiveId } = executeCellInList(prev.cells, id);
      pendingFocus.current = nextActiveId;
      setActiveId(nextActiveId);
      return { ...prev, cells };
    });
  };

  const remove = (id: string) => {
    if (doc.cells.length <= 1) return;
    setDoc((prev) => {
      const { cells, removed, index } = removeCellById(prev.cells, id);
      if (removed) {
        setDeleted({ cell: removed, index });
      }
      const nextId = cells[index]?.id ?? cells[index - 1]?.id ?? "";
      pendingFocus.current = nextId;
      setActiveId(nextId);
      return { ...prev, cells };
    });
  };

  const move = (index: number, delta: number) => {
    setDoc((prev) => ({
      ...prev,
      cells: moveCell(prev.cells, index, delta),
    }));
  };

  const undoDelete = () => {
    if (!deleted) return;
    const { cell, index } = deleted;
    setDoc((prev) => {
      const cells = [...prev.cells];
      cells.splice(index, 0, cell);
      return { ...prev, cells };
    });
    pendingFocus.current = cell.id;
    setActiveId(cell.id);
    setDeleted(null);
  };

  const resetToSample = () => {
    setDoc(structuredClone(sampleNotebook));
    setActiveId(sampleNotebook.cells[0]?.id ?? "");
    setDeleted(null);
  };

  const setTitle = (title: string) => {
    setDoc((prev) => ({ ...prev, title }));
  };

  const exportDoc = () => {
    filePort.exportNotebook(doc);
  };

  const importDoc = async (file: File) => {
    try {
      const parsed = await filePort.parseNotebookFile(file);
      if (
        !window.confirm(
          "Opening this notebook will replace your current workspace. Have you saved or exported any work you want to keep?",
        )
      ) {
        return;
      }
      setDoc(parsed);
      setActiveId(parsed.cells[0]?.id ?? "");
      setDeleted(null);
      setLoadError("");
    } catch (error) {
      setLoadError((error as Error).message);
    }
  };

  const insertTemplate = (cellId: string) => {
    const target = doc.cells.find((c) => c.id === cellId);
    if (!target) return;
    patch(cellId, {
      source: appendTemplateToSource(target.source, target.cellType),
    });
  };

  const updateSource = (cellId: string, source: string) =>
    patch(cellId, { source });
  const updateSkill = (cellId: string, cellType: SkillType) =>
    patch(cellId, { cellType });
  const updateResource = (
    cellId: string,
    resource: CellResource | undefined,
  ) => patch(cellId, { resource });

  return {
    doc,
    activeId,
    activeIndex: doc.cells.findIndex((c) => c.id === activeId),
    saveState,
    loadError,
    deleted,
    setActiveId,
    setLoadError,
    setTitle,
    add,
    run,
    remove,
    move,
    undoDelete,
    dismissUndo: () => setDeleted(null),
    resetToSample,
    exportDoc,
    importDoc,
    insertTemplate,
    updateSource,
    updateSkill,
    updateResource,
  };
}
