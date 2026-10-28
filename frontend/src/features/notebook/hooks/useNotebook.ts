import { useEffect, useRef, useState, useCallback } from "react";
import type { IeltsExerciseData } from "../../cell/types/ieltsSchema.ts";
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
import {
  appendTemplateToSource,
  getSkillTemplate,
} from "../../cell/services/skillTemplates.ts";
import {
  BrowserNotebookFileAdapter,
  defaultNotebookFileAdapter,
} from "../services/notebookFile.ts";
import {
  defaultNotebookStorage,
  LocalStorageNotebookStorage,
} from "../services/notebookStorage.ts";
import {
  defaultNotebookApiClient,
  NotebookApiClient,
  type DatabaseHealth,
  type SnapshotSummary,
} from "../services/notebookApiClient.ts";
import { sampleNotebook } from "../data/initialSampleNotebook.ts";

export type SaveState = "saving" | "saved" | "error";
export type DatabaseStatus = "connected" | "disconnected" | "syncing" | "connecting";

interface UseNotebookOptions {
  storage?: LocalStorageNotebookStorage;
  fileAdapter?: BrowserNotebookFileAdapter;
  apiClient?: NotebookApiClient;
  enableDatabaseSync?: boolean;
}

export function useNotebook(options?: UseNotebookOptions) {
  const storage = options?.storage ?? defaultNotebookStorage;
  const filePort = options?.fileAdapter ?? defaultNotebookFileAdapter;
  const apiClient = options?.apiClient ?? defaultNotebookApiClient;
  const enableDatabaseSync = options?.enableDatabaseSync ?? true;

  const [initial] = useState(() => {
    try {
      const savedMulti = storage.loadAll();
      if (savedMulti && savedMulti.notebooks.length > 0) {
        return {
          notebooks: savedMulti.notebooks,
          activeId: savedMulti.activeId,
          error: "",
        };
      }
      const single = storage.load();
      if (single) {
        return {
          notebooks: [single],
          activeId: single.id,
          error: "",
        };
      }
      const sample = structuredClone(sampleNotebook);
      return {
        notebooks: [sample],
        activeId: sample.id,
        error: "",
      };
    } catch {
      const sample = structuredClone(sampleNotebook);
      return {
        notebooks: [sample],
        activeId: sample.id,
        error: "Unable to read notebook from storage. Loading default sample.",
      };
    }
  });

  const [notebooks, setNotebooks] = useState<JupyterNotebookDoc[]>(initial.notebooks);
  const [activeNotebookId, setActiveNotebookId] = useState<string>(initial.activeId);

  // Computed active document
  const doc =
    notebooks.find((n) => n.id === activeNotebookId) ||
    notebooks[0] ||
    structuredClone(sampleNotebook);

  const docRef = useRef(doc);
  useEffect(() => {
    docRef.current = doc;
  }, [doc]);

  // Track the serialized JSON content of active doc that was last saved
  const lastSavedContentRef = useRef<string>(JSON.stringify(doc));
  const isInitialLoadDone = useRef(false);

  const [loadError, setLoadError] = useState(initial.error);
  const [activeId, setActiveId] = useState(doc.cells[0]?.id ?? "");
  const [saveState, setSaveState] = useState<SaveState>("saved");
  const [databaseStatus, setDatabaseStatus] = useState<DatabaseStatus>("connecting");
  const [dbHealth, setDbHealth] = useState<DatabaseHealth | null>(null);
  const [snapshots, setSnapshots] = useState<SnapshotSummary[]>([]);
  const [deleted, setDeleted] = useState<{
    cell: JupyterCell;
    index: number;
  } | null>(null);

  const pendingFocus = useRef<string | null>(null);

  // Helper to update the currently active notebook
  const updateActiveDoc = useCallback(
    (updater: (prevDoc: JupyterNotebookDoc) => JupyterNotebookDoc) => {
      setNotebooks((prev) =>
        prev.map((nb) => (nb.id === doc.id ? updater(nb) : nb)),
      );
    },
    [doc.id],
  );

  // 1. Initial Load from Database (Runs EXACTLY ONCE on mount)
  useEffect(() => {
    if (!enableDatabaseSync) {
      setDatabaseStatus("disconnected");
      isInitialLoadDone.current = true;
      return;
    }

    let active = true;

    async function initializeFromDatabase() {
      try {
        const health = await apiClient.checkHealth();
        if (!active) return;
        setDbHealth(health);

        if (health.status === "ok" && health.database === "connected") {
          setDatabaseStatus("connected");

          // Fetch current active notebook from database
          const remoteDoc = await apiClient.fetchCurrentNotebook();
          if (!active) return;

          if (remoteDoc) {
            setNotebooks((prev) => {
              const next = [...prev];
              const idx = next.findIndex((n) => n.id === remoteDoc.id);
              if (idx >= 0) {
                next[idx] = remoteDoc;
              } else {
                next.push(remoteDoc);
              }
              return next;
            });
            setActiveNotebookId(remoteDoc.id);
            lastSavedContentRef.current = JSON.stringify(remoteDoc);
            storage.save(remoteDoc);
            setActiveId(remoteDoc.cells[0]?.id ?? "");
          } else {
            // Seed the remote database with initial notebook
            const currentDoc = docRef.current;
            await apiClient.syncNotebook(currentDoc, "initial_client_seed");
            lastSavedContentRef.current = JSON.stringify(currentDoc);
          }

          // Fetch snapshots for active doc
          const currentId = remoteDoc?.id ?? docRef.current.id;
          const snaps = await apiClient.listSnapshots(currentId);
          if (active) setSnapshots(snaps);
        } else {
          setDatabaseStatus("disconnected");
        }
      } catch {
        if (active) setDatabaseStatus("disconnected");
      } finally {
        isInitialLoadDone.current = true;
      }
    }

    initializeFromDatabase();

    return () => {
      active = false;
    };
  }, [apiClient, enableDatabaseSync, storage]);

  // 2. Manual refresh of metadata (snapshots & health)
  const refreshDatabase = useCallback(async () => {
    if (!enableDatabaseSync) return;
    try {
      const health = await apiClient.checkHealth();
      setDbHealth(health);
      if (health.status === "ok" && health.database === "connected") {
        setDatabaseStatus("connected");
        const snaps = await apiClient.listSnapshots(docRef.current.id);
        setSnapshots(snaps);
      } else {
        setDatabaseStatus("disconnected");
      }
    } catch {
      setDatabaseStatus("disconnected");
    }
  }, [apiClient, enableDatabaseSync]);

  // 3. Auto-save debounce: ONLY triggers when active doc content changed
  useEffect(() => {
    const currentJson = JSON.stringify(doc);

    // If active doc is unchanged, skip saving
    if (currentJson === lastSavedContentRef.current) {
      return;
    }

    setSaveState("saving");

    const timer = window.setTimeout(async () => {
      try {
        storage.saveAll(notebooks, activeNotebookId);
        setSaveState("saved");
      } catch {
        setSaveState("error");
        return;
      }

      if (enableDatabaseSync && isInitialLoadDone.current) {
        try {
          const res = await apiClient.syncNotebook(doc, "auto_sync");
          if (res.success) {
            lastSavedContentRef.current = currentJson;
            setDatabaseStatus("connected");
          } else {
            setDatabaseStatus("disconnected");
          }
        } catch {
          setDatabaseStatus("disconnected");
        }
      } else {
        lastSavedContentRef.current = currentJson;
      }
    }, 350);

    return () => window.clearTimeout(timer);
  }, [doc, notebooks, activeNotebookId, storage, apiClient, enableDatabaseSync]);

  // Pagehide fallback save
  useEffect(() => {
    const handleSave = () => {
      try {
        storage.saveAll(notebooks, activeNotebookId);
      } catch {
        /* handled above */
      }
    };
    window.addEventListener("pagehide", handleSave);
    return () => {
      window.removeEventListener("pagehide", handleSave);
      handleSave();
    };
  }, [notebooks, activeNotebookId, storage]);

  // Focus pending cell editor
  useEffect(() => {
    if (pendingFocus.current) {
      document.getElementById(`editor-${pendingFocus.current}`)?.focus();
      pendingFocus.current = null;
    }
  }, [doc, activeId]);

  // Tab operations
  const switchTab = (tabId: string) => {
    const target = notebooks.find((n) => n.id === tabId);
    if (!target) return;
    setActiveNotebookId(tabId);
    setActiveId(target.cells[0]?.id ?? "");
    setDeleted(null);
    lastSavedContentRef.current = JSON.stringify(target);
    storage.saveAll(notebooks, tabId);
    if (enableDatabaseSync) {
      apiClient.listSnapshots(tabId).then((snaps) => setSnapshots(snaps));
    }
  };

  const createTab = (title?: string) => {
    const newNb: JupyterNotebookDoc = {
      id: crypto.randomUUID(),
      title: title || `Notebook_${notebooks.length + 1}.json`,
      cells: [createCell("markdown")],
    };
    const nextNotebooks = [...notebooks, newNb];
    setNotebooks(nextNotebooks);
    setActiveNotebookId(newNb.id);
    setActiveId(newNb.cells[0]?.id ?? "");
    setDeleted(null);
    lastSavedContentRef.current = JSON.stringify(newNb);
    storage.saveAll(nextNotebooks, newNb.id);
    if (enableDatabaseSync) {
      apiClient.syncNotebook(newNb, "create_tab");
      setSnapshots([]);
    }
  };

  const closeTab = (tabId: string) => {
    if (notebooks.length <= 1) {
      // If closing the only tab, replace with a fresh empty notebook
      const fresh: JupyterNotebookDoc = {
        id: crypto.randomUUID(),
        title: "Untitled.json",
        cells: [],
      };
      setNotebooks([fresh]);
      setActiveNotebookId(fresh.id);
      setActiveId("");
      setDeleted(null);
      lastSavedContentRef.current = JSON.stringify(fresh);
      storage.saveAll([fresh], fresh.id);
      return;
    }

    const closingIdx = notebooks.findIndex((n) => n.id === tabId);
    const nextNotebooks = notebooks.filter((n) => n.id !== tabId);

    if (activeNotebookId === tabId) {
      const nextIdx = closingIdx > 0 ? closingIdx - 1 : 0;
      const nextActive = nextNotebooks[nextIdx];
      setActiveNotebookId(nextActive.id);
      setActiveId(nextActive.cells[0]?.id ?? "");
      lastSavedContentRef.current = JSON.stringify(nextActive);
      storage.saveAll(nextNotebooks, nextActive.id);
      if (enableDatabaseSync) {
        apiClient.listSnapshots(nextActive.id).then((snaps) => setSnapshots(snaps));
      }
    } else {
      storage.saveAll(nextNotebooks, activeNotebookId);
    }

    setNotebooks(nextNotebooks);
    setDeleted(null);
  };

  const renameTab = (tabId: string, newTitle: string) => {
    const trimmed = newTitle.trim();
    if (!trimmed) return;
    setNotebooks((prev) => {
      const next = prev.map((nb) =>
        nb.id === tabId ? { ...nb, title: trimmed } : nb,
      );
      storage.saveAll(next, activeNotebookId);
      return next;
    });

    if (tabId === activeNotebookId) {
      if (enableDatabaseSync && isInitialLoadDone.current) {
        const updatedNb = { ...doc, title: trimmed };
        lastSavedContentRef.current = JSON.stringify(updatedNb);
        apiClient.syncNotebook(updatedNb, "rename_tab");
      }
    }
  };

  const duplicateTab = (tabId: string) => {
    const target = notebooks.find((n) => n.id === tabId);
    if (!target) return;
    const copyTitle = target.title.replace(
      /\.(ilnb|json|ipynb)$/i,
      (ext) => `_copy${ext}`,
    );
    const finalTitle =
      copyTitle === target.title ? `${target.title} (Copy)` : copyTitle;
    const clonedNb: JupyterNotebookDoc = {
      ...structuredClone(target),
      id: crypto.randomUUID(),
      title: finalTitle,
      cells: target.cells.map((c) => ({
        ...structuredClone(c),
        id: crypto.randomUUID(),
      })),
    };
    const targetIdx = notebooks.findIndex((n) => n.id === tabId);
    const nextNotebooks = [...notebooks];
    nextNotebooks.splice(targetIdx + 1, 0, clonedNb);
    setNotebooks(nextNotebooks);
    setActiveNotebookId(clonedNb.id);
    setActiveId(clonedNb.cells[0]?.id ?? "");
    setDeleted(null);
    lastSavedContentRef.current = JSON.stringify(clonedNb);
    storage.saveAll(nextNotebooks, clonedNb.id);
    if (enableDatabaseSync) {
      apiClient.syncNotebook(clonedNb, "duplicate_tab");
      setSnapshots([]);
    }
  };

  const closeOtherTabs = (tabId: string) => {
    const kept = notebooks.find((n) => n.id === tabId);
    if (!kept) return;
    const nextNotebooks = [kept];
    setNotebooks(nextNotebooks);
    setActiveNotebookId(kept.id);
    setActiveId(kept.cells[0]?.id ?? "");
    setDeleted(null);
    lastSavedContentRef.current = JSON.stringify(kept);
    storage.saveAll(nextNotebooks, kept.id);
    if (enableDatabaseSync) {
      apiClient.listSnapshots(kept.id).then((snaps) => setSnapshots(snaps));
    }
  };

  const importFiles = async (files: File[]) => {
    const loadedDocs: JupyterNotebookDoc[] = [];
    const errors: string[] = [];

    for (const file of files) {
      try {
        const parsed = await filePort.parseNotebookFile(file);
        loadedDocs.push(parsed);
      } catch (err) {
        errors.push(`${file.name}: ${(err as Error).message}`);
      }
    }

    if (errors.length > 0) {
      setLoadError(errors.join(" | "));
    }

    if (loadedDocs.length > 0) {
      setNotebooks((prev) => {
        const next = [...prev];
        for (const doc of loadedDocs) {
          const existingIdx = next.findIndex((n) => n.id === doc.id);
          if (existingIdx >= 0) {
            next[existingIdx] = doc;
          } else {
            next.push(doc);
          }
        }
        return next;
      });

      const lastDoc = loadedDocs[loadedDocs.length - 1];
      setActiveNotebookId(lastDoc.id);
      setActiveId(lastDoc.cells[0]?.id ?? "");
      setDeleted(null);
      lastSavedContentRef.current = JSON.stringify(lastDoc);

      const merged = [...notebooks, ...loadedDocs];
      storage.saveAll(merged, lastDoc.id);

      if (enableDatabaseSync) {
        for (const doc of loadedDocs) {
          apiClient.syncNotebook(doc, "import_file");
        }
        apiClient.listSnapshots(lastDoc.id).then((snaps) => setSnapshots(snaps));
      }
    }
  };

  const importDoc = async (file: File) => {
    await importFiles([file]);
  };

  // Cell and Document operations (applied to active doc)
  const patch = (id: string, change: Partial<JupyterCell>) => {
    updateActiveDoc((prev) => ({
      ...prev,
      cells: patchCell(prev.cells, id, change),
    }));
  };

  const add = (index: number, skill: SkillType = "markdown") => {
    let initialResource: CellResource | undefined = undefined;
    if (skill === "speaking") {
      initialResource = { type: "voice_recorder", name: "Speaking_Voice_Studio" };
    }
    const initialSource = getSkillTemplate(skill);
    const newCell = createCell(skill, initialSource, initialResource);
    pendingFocus.current = newCell.id;
    updateActiveDoc((prev) => ({
      ...prev,
      cells: addCellAt(prev.cells, index, newCell),
    }));
    setActiveId(newCell.id);
  };

  const run = (id: string) => {
    updateActiveDoc((prev) => {
      const { cells, nextActiveId } = executeCellInList(prev.cells, id);
      pendingFocus.current = nextActiveId;
      setActiveId(nextActiveId);
      return { ...prev, cells };
    });
  };

  const remove = (id: string) => {
    updateActiveDoc((prev) => {
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
    updateActiveDoc((prev) => ({
      ...prev,
      cells: moveCell(prev.cells, index, delta),
    }));
  };

  const undoDelete = () => {
    if (!deleted) return;
    const { cell, index } = deleted;
    updateActiveDoc((prev) => {
      const cells = [...prev.cells];
      cells.splice(index, 0, cell);
      return { ...prev, cells };
    });
    pendingFocus.current = cell.id;
    setActiveId(cell.id);
    setDeleted(null);
  };

  const resetToSample = async () => {
    const clone = structuredClone(sampleNotebook);
    clone.id = doc.id; // Preserve active tab ID
    updateActiveDoc(() => clone);
    setActiveId(clone.cells[0]?.id ?? "");
    setDeleted(null);
    lastSavedContentRef.current = JSON.stringify(clone);
    storage.save(clone);
    if (enableDatabaseSync) {
      await apiClient.syncNotebook(clone, "reset_to_sample");
      const snaps = await apiClient.listSnapshots(clone.id);
      setSnapshots(snaps);
    }
  };

  const setTitle = (title: string) => {
    updateActiveDoc((prev) => ({ ...prev, title }));
  };

  const exportDoc = (targetDoc?: JupyterNotebookDoc) => {
    filePort.exportNotebook(targetDoc || doc);
  };

  const insertTemplate = (cellId: string) => {
    const target = doc.cells.find((c) => c.id === cellId);
    if (!target) return;
    patch(cellId, {
      source: appendTemplateToSource(target.source, target.cellType),
    });
  };

  const restoreSnapshot = async (snapshotId: number) => {
    const res = await apiClient.restoreSnapshot(doc.id, snapshotId);
    if (res.success && res.notebook) {
      lastSavedContentRef.current = JSON.stringify(res.notebook);
      updateActiveDoc(() => res.notebook!);
      storage.save(res.notebook);
      setActiveId(res.notebook.cells[0]?.id ?? "");
      const snaps = await apiClient.listSnapshots(res.notebook.id);
      setSnapshots(snaps);
      return true;
    }
    return false;
  };

  const createSnapshotNow = async () => {
    const res = await apiClient.syncNotebook(doc, "manual_checkpoint");
    if (res.success) {
      const snaps = await apiClient.listSnapshots(doc.id);
      setSnapshots(snaps);
      return true;
    }
    return false;
  };

  const updateSource = (cellId: string, source: string) =>
    patch(cellId, { source });
  const updateSkill = (cellId: string, cellType: SkillType) =>
    patch(cellId, { cellType });
  const updateResource = (
    cellId: string,
    resource: CellResource | undefined,
  ) => patch(cellId, { resource });
  const updateStructuredData = (
    cellId: string,
    structuredData: IeltsExerciseData | undefined,
  ) => {
    patch(cellId, {
      structuredData,
      ...(structuredData?.skill ? { cellType: structuredData.skill as SkillType } : {}),
    });
  };

  return {
    doc,
    notebooks,
    activeNotebookId,
    activeId,
    activeIndex: doc.cells.findIndex((c) => c.id === activeId),
    saveState,
    databaseStatus,
    dbHealth,
    snapshots,
    loadError,
    deleted,
    switchTab,
    createTab,
    closeTab,
    renameTab,
    duplicateTab,
    closeOtherTabs,
    importFiles,
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
    restoreSnapshot,
    createSnapshotNow,
    refreshDatabase,
    updateSource,
    updateSkill,
    updateResource,
    updateStructuredData,
  };
}
