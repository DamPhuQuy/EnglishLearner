import {
  Copy,
  Download,
  FileText,
  Pencil,
  Plus,
  Trash2,
  X,
  XSquare,
} from "lucide-react";
import React, { useEffect, useRef, useState } from "react";
import type { JupyterNotebookDoc } from "../types/notebook.ts";

interface Props {
  notebooks: JupyterNotebookDoc[];
  activeId: string;
  onSelectTab: (id: string) => void;
  onCloseTab: (id: string) => void;
  onCloseOtherTabs?: (id: string) => void;
  onNewTab: () => void;
  onDuplicateTab?: (id: string) => void;
  onRenameTab?: (id: string, newTitle: string) => void;
  onExportTab?: (notebook: JupyterNotebookDoc) => void;
}

interface ContextMenuState {
  tabId: string;
  x: number;
  y: number;
}

export const NotebookTabs: React.FC<Props> = ({
  notebooks,
  activeId,
  onSelectTab,
  onCloseTab,
  onCloseOtherTabs,
  onNewTab,
  onDuplicateTab,
  onRenameTab,
  onExportTab,
}) => {
  const [editingTabId, setEditingTabId] = useState<string | null>(null);
  const [editTitle, setEditTitle] = useState("");
  const [contextMenu, setContextMenu] = useState<ContextMenuState | null>(null);
  const tabListRef = useRef<HTMLDivElement>(null);
  const editInputRef = useRef<HTMLInputElement>(null);

  // Close context menu on any outside click or Escape
  useEffect(() => {
    const handleClose = () => setContextMenu(null);
    const handleKeyDown = (e: KeyboardEvent) => {
      if (e.key === "Escape") setContextMenu(null);
    };

    window.addEventListener("click", handleClose);
    window.addEventListener("keydown", handleKeyDown);
    return () => {
      window.removeEventListener("click", handleClose);
      window.removeEventListener("keydown", handleKeyDown);
    };
  }, []);

  // Focus rename input when editing starts
  useEffect(() => {
    if (editingTabId && editInputRef.current) {
      editInputRef.current.focus();
      editInputRef.current.select();
    }
  }, [editingTabId]);

  const startRename = (nb: JupyterNotebookDoc) => {
    setEditingTabId(nb.id);
    setEditTitle(nb.title);
    setContextMenu(null);
  };

  const commitRename = (tabId: string) => {
    if (onRenameTab && editTitle.trim()) {
      onRenameTab(tabId, editTitle.trim());
    }
    setEditingTabId(null);
  };

  const handleContextMenu = (e: React.MouseEvent, tabId: string) => {
    e.preventDefault();
    setContextMenu({
      tabId,
      x: e.clientX,
      y: e.clientY,
    });
  };

  const activeNotebook = notebooks.find((n) => n.id === activeId);

  return (
    <div className="notebook-tabs-container">
      <div className="tabs-track" ref={tabListRef} role="tablist">
        {notebooks.map((nb) => {
          const isActive = nb.id === activeId;
          const isEditing = editingTabId === nb.id;
          const displayTitle = nb.title.trim() || "Untitled";

          return (
            <div
              key={nb.id}
              role="tab"
              aria-selected={isActive}
              tabIndex={isActive ? 0 : -1}
              className={`notebook-tab ${isActive ? "active" : ""}`}
              onClick={() => {
                if (!isEditing) onSelectTab(nb.id);
              }}
              onDoubleClick={(e) => {
                e.stopPropagation();
                startRename(nb);
              }}
              onContextMenu={(e) => handleContextMenu(e, nb.id)}
              title={
                isActive
                  ? `${displayTitle} (Double-click to rename)`
                  : `${displayTitle} · ${nb.cells.length} cells`
              }
            >
              <FileText size={13} className="tab-icon" />

              {isEditing ? (
                <input
                  ref={editInputRef}
                  type="text"
                  className="tab-rename-input"
                  value={editTitle}
                  onChange={(e) => setEditTitle(e.target.value)}
                  onBlur={() => commitRename(nb.id)}
                  onKeyDown={(e) => {
                    if (e.key === "Enter") {
                      e.preventDefault();
                      commitRename(nb.id);
                    } else if (e.key === "Escape") {
                      e.preventDefault();
                      setEditingTabId(null);
                    }
                  }}
                  onClick={(e) => e.stopPropagation()}
                />
              ) : (
                <span className="tab-title">{displayTitle}</span>
              )}

              {isActive && !isEditing && (
                <button
                  type="button"
                  className="tab-action-icon"
                  title="Rename notebook"
                  onClick={(e) => {
                    e.stopPropagation();
                    startRename(nb);
                  }}
                >
                  <Pencil size={11} />
                </button>
              )}

              <span className="tab-cell-badge" title={`${nb.cells.length} cells`}>
                {nb.cells.length}
              </span>

              <button
                type="button"
                className="tab-close-btn"
                aria-label={`Close ${displayTitle}`}
                title="Close tab"
                onClick={(e) => {
                  e.stopPropagation();
                  onCloseTab(nb.id);
                }}
              >
                <X size={12} />
              </button>
            </div>
          );
        })}

        <button
          type="button"
          className="tab-add-btn"
          title="New notebook tab (Ctrl+N)"
          aria-label="New notebook tab"
          onClick={onNewTab}
        >
          <Plus size={15} />
        </button>
      </div>

      {/* Context Menu on Right Click */}
      {contextMenu && (
        <div
          className="tab-context-menu"
          style={{ top: contextMenu.y, left: contextMenu.x }}
          onClick={(e) => e.stopPropagation()}
        >
          {(() => {
            const targetNb = notebooks.find((n) => n.id === contextMenu.tabId);
            if (!targetNb) return null;

            return (
              <>
                <button
                  className="context-menu-item"
                  onClick={() => startRename(targetNb)}
                >
                  <Pencil size={13} />
                  Rename
                </button>
                {onDuplicateTab && (
                  <button
                    className="context-menu-item"
                    onClick={() => {
                      onDuplicateTab(targetNb.id);
                      setContextMenu(null);
                    }}
                  >
                    <Copy size={13} />
                    Duplicate
                  </button>
                )}
                {onExportTab && (
                  <button
                    className="context-menu-item"
                    onClick={() => {
                      onExportTab(targetNb);
                      setContextMenu(null);
                    }}
                  >
                    <Download size={13} />
                    Export
                  </button>
                )}
                <div className="context-menu-divider" />
                <button
                  className="context-menu-item"
                  onClick={() => {
                    onCloseTab(targetNb.id);
                    setContextMenu(null);
                  }}
                >
                  <Trash2 size={13} />
                  Close
                </button>
                {notebooks.length > 1 && onCloseOtherTabs && (
                  <button
                    className="context-menu-item"
                    onClick={() => {
                      onCloseOtherTabs(targetNb.id);
                      setContextMenu(null);
                    }}
                  >
                    <XSquare size={13} />
                    Close other tabs
                  </button>
                )}
              </>
            );
          })()}
        </div>
      )}
    </div>
  );
};
