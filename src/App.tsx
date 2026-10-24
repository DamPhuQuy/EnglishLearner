import React, { useState, useEffect, useRef } from 'react';
import { Plus, Download, Upload, RotateCcw, BookOpen, Check, CircleAlert, Undo2 } from 'lucide-react';
import { JupyterCell } from './components/JupyterCell';
import { sampleNotebook } from './data/initialSample';
import { isNotebook } from './lib/notebook';
import type { JupyterNotebookDoc, JupyterCell as CellType, SkillType, CellResource } from './types/notebook';

const STORAGE_KEY = 'ielts_jupyter_notebook_v2';
const skillNames: Record<SkillType, string> = { listening: 'Listening', reading: 'Reading', writing: 'Writing', speaking: 'Speaking', markdown: 'Ghi chú' };
const templates: Record<SkillType, string> = {
  listening: '### Listening\n\n1. \n2. \n3. \n\n### Từ vựng & nối âm\n\n- ',
  reading: '### Reading\n\n1. \n2. \n3. \n\n### Bằng chứng trong bài\n\n> \n\n### Từ vựng\n\n- ',
  writing: '### Writing\n\n### Dàn ý\n\n- \n\n### Bài viết\n\n',
  speaking: '### Speaking Part 2\n\nChủ đề: \n\n- What:\n- When:\n- Why:\n\n### Tự nhận xét\n\n',
  markdown: '### Ghi chú\n\n'
};

export const App: React.FC = () => {
  const [initial] = useState(() => {
    try {
      const saved = localStorage.getItem(STORAGE_KEY);
      if (saved) {
        const parsed: unknown = JSON.parse(saved);
        if (isNotebook(parsed)) return { doc: parsed, error: '' };
        return { doc: structuredClone(sampleNotebook), error: 'Notebook đã lưu không đúng định dạng. Đang mở bản mẫu; hãy nhập lại bản đã xuất nếu cần khôi phục.' };
      }
      return { doc: structuredClone(sampleNotebook), error: '' };
    } catch {
      return { doc: structuredClone(sampleNotebook), error: 'Không đọc được notebook trong trình duyệt. Đang mở bản mẫu; hãy nhập lại bản đã xuất nếu có.' };
    }
  });
  const [loadError, setLoadError] = useState(initial.error);
  const [doc, setDoc] = useState<JupyterNotebookDoc>(initial.doc);
  const [activeId, setActiveId] = useState(doc.cells[0]?.id ?? '');
  const [saveState, setSaveState] = useState<'saving' | 'saved' | 'error'>('saving');
  const [addType, setAddType] = useState<SkillType>('markdown');
  const [deleted, setDeleted] = useState<{ cell: CellType; index: number } | null>(null);
  const fileInput = useRef<HTMLInputElement>(null);
  const pendingFocus = useRef<string | null>(null);
  const activeIndex = doc.cells.findIndex(c => c.id === activeId);

  useEffect(() => {
    setSaveState('saving');
    const timer = window.setTimeout(() => {
      try { localStorage.setItem(STORAGE_KEY, JSON.stringify(doc)); setSaveState('saved'); }
      catch { setSaveState('error'); }
    }, 350);
    return () => window.clearTimeout(timer);
  }, [doc]);

  useEffect(() => {
    const save = () => { try { localStorage.setItem(STORAGE_KEY, JSON.stringify(doc)); } catch { /* visible save error is handled above */ } };
    window.addEventListener('pagehide', save);
    return () => { window.removeEventListener('pagehide', save); save(); };
  }, [doc]);

  useEffect(() => {
    if (pendingFocus.current) {
      document.getElementById(`editor-${pendingFocus.current}`)?.focus();
      pendingFocus.current = null;
    }
  }, [doc, activeId]);

  const patch = (id: string, change: Partial<CellType>) => setDoc(p => ({ ...p, cells: p.cells.map(c => c.id === id ? { ...c, ...change } : c) }));
  const add = (index: number, skill: SkillType = addType) => {
    const cell: CellType = { id: crypto.randomUUID(), executionCount: null, cellType: skill, source: '' };
    pendingFocus.current = cell.id;
    setDoc(p => { const cells = [...p.cells]; cells.splice(index + 1, 0, cell); return { ...p, cells }; });
    setActiveId(cell.id);
  };
  const run = (id: string) => {
    const index = doc.cells.findIndex(c => c.id === id);
    patch(id, { executionCount: Math.max(0, ...doc.cells.map(c => c.executionCount ?? 0)) + 1 });
    const next = doc.cells[index + 1]?.id ?? id;
    pendingFocus.current = next;
    setActiveId(next);
  };
  const remove = (id: string) => {
    if (doc.cells.length <= 1) return;
    const index = doc.cells.findIndex(c => c.id === id);
    setDeleted({ cell: doc.cells[index], index });
    setDoc(p => ({ ...p, cells: p.cells.filter(c => c.id !== id) }));
    const next = doc.cells[index + 1]?.id ?? doc.cells[index - 1].id;
    pendingFocus.current = next;
    setActiveId(next);
  };
  const move = (index: number, delta: number) => {
    if (index < 0 || index + delta < 0 || index + delta >= doc.cells.length) return;
    setDoc(p => { const cells = [...p.cells]; [cells[index], cells[index + delta]] = [cells[index + delta], cells[index]]; return { ...p, cells }; });
  };
  const exportDoc = () => {
    const url = URL.createObjectURL(new Blob([JSON.stringify(doc, null, 2)], { type: 'application/json' }));
    const a = document.createElement('a'); a.href = url; a.download = `${doc.title.replace(/\.(ipynb|json|ilnb)$/i, '') || 'IELTS Notebook'}.ilnb`; a.click();
    window.setTimeout(() => URL.revokeObjectURL(url), 1000);
  };
  const importDoc = async (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0]; e.target.value = ''; if (!file) return;
    try {
      if (file.size > 20 * 1024 * 1024) throw new Error('Tệp lớn hơn 20 MB. Hãy chọn notebook nhỏ hơn.');
      const parsed: unknown = JSON.parse(await file.text());
      if (!isNotebook(parsed)) throw new Error('Tệp không đúng định dạng IELTS Notebook. Hãy chọn tệp .ilnb đã xuất từ ứng dụng.');
      if (!window.confirm('Mở notebook này sẽ thay nội dung hiện tại. Bạn đã xuất bản cần giữ chưa?')) return;
      setDoc(parsed); setActiveId(parsed.cells[0].id); setDeleted(null); setLoadError('');
    } catch (error) { setLoadError(error instanceof SyntaxError ? 'Tệp không đọc được dưới dạng JSON. Hãy chọn notebook đã xuất từ ứng dụng.' : (error as Error).message); }
  };
  return (
    <div className="app-shell">
      <a className="skip-link" href="#notebook">Đến nội dung notebook</a>
      <header className="app-header">
        <div className="header-inner">
          <div className="notebook-identity"><BookOpen size={21} className="brand-mark" /><span>IELTS Notebook</span><span className="identity-divider" />
            <input aria-label="Tên notebook" className="notebook-title" value={doc.title} onChange={e => setDoc(p => ({ ...p, title: e.target.value }))} />
          </div>
          <div className="file-actions">
            <span className={`save-state ${saveState}`} role="status">{saveState === 'saved' ? <Check size={14} /> : saveState === 'error' ? <CircleAlert size={14} /> : null}{saveState === 'saved' ? 'Đã lưu trên máy' : saveState === 'error' ? 'Chưa lưu được' : 'Đang lưu…'}</span>
            <input ref={fileInput} type="file" accept=".ilnb,.json,.ipynb" onChange={importDoc} hidden />
            <button className="button quiet" onClick={() => fileInput.current?.click()}><Upload size={15} />Mở tệp</button>
            <button className="button outlined" onClick={exportDoc}><Download size={15} />Xuất notebook</button>
          </div>
        </div>
      </header>
      <div className="notebook-toolbar"><div className="toolbar-inner">
        <div className="add-control"><select aria-label="Loại cell mới" value={addType} onChange={e => setAddType(e.target.value as SkillType)}>{Object.entries(skillNames).map(([key, label]) => <option key={key} value={key}>{label}</option>)}</select><button className="button primary" onClick={() => add(activeIndex)}><Plus size={16} />Thêm cell</button></div>
        <span className="toolbar-hint">Viết bên trái. Tài liệu bên phải.</span>
        <details className="notebook-options"><summary className="button quiet">Tùy chọn</summary><div className="options-panel"><p>Shift + Enter: đánh dấu đã xem và chuyển cell tiếp theo.</p><p>Notebook tự lưu trong trình duyệt này. Xuất tệp để giữ một bản riêng.</p><button className="button quiet" onClick={() => { if (confirm('Thay notebook hiện tại bằng bản mẫu? Hãy xuất tệp nếu cần giữ bài làm.')) { setDoc(structuredClone(sampleNotebook)); setActiveId(sampleNotebook.cells[0].id); setDeleted(null); } }}><RotateCcw size={15} />Mở lại bản mẫu</button></div></details>
      </div></div>
      <main id="notebook" className="notebook" tabIndex={-1}>
        {(saveState === 'error' || loadError) && <div className="notice error" role="alert"><CircleAlert size={18} /><span>{loadError || 'Bộ nhớ trình duyệt không đủ hoặc bị chặn. Bài làm vẫn đang mở; hãy xuất notebook để giữ nội dung.'}</span>{loadError && <button className="button quiet" onClick={() => setLoadError('')}>Đóng</button>}</div>}
        <div className="document-heading"><div><h1>Không gian luyện tập</h1><p>Ghi lại bài làm, giữ tài liệu ngay bên cạnh.</p></div><span>{doc.cells.length} cell · {activeIndex >= 0 ? `Đang chọn ${activeIndex + 1}` : 'Chọn một cell'}</span></div>
        {doc.cells.map((cell, index) => <JupyterCell key={cell.id} cell={cell} index={index} totalCells={doc.cells.length} isActive={cell.id === activeId} onSelect={() => setActiveId(cell.id)} onUpdateSource={(id, source) => patch(id, { source })} onUpdateSkill={(id, cellType) => patch(id, { cellType })} onUpdateResource={(id, resource: CellResource | undefined) => patch(id, { resource })} onRun={run} onDelete={remove} onMoveUp={index => move(index, -1)} onMoveDown={index => move(index, 1)} onAddAbove={index => add(index - 1, cell.cellType)} onAddBelow={index => add(index, cell.cellType)} onInsertTemplate={() => patch(cell.id, { source: cell.source ? `${cell.source}\n\n${templates[cell.cellType]}` : templates[cell.cellType] })} />)}
        <button className="append-cell" onClick={() => add(doc.cells.length - 1)}><Plus size={17} />Thêm {skillNames[addType].toLowerCase()}<span>vào cuối notebook</span></button>
        <footer className="notebook-footer"><span>Nội dung lưu trên trình duyệt này</span><span>Shift + Enter · Cell tiếp theo</span></footer>
      </main>
      {deleted && <div className="undo-notice" role="status"><span>Đã xóa cell.</span><button className="button quiet" onClick={() => { const { cell, index } = deleted; setDoc(p => { const cells = [...p.cells]; cells.splice(index, 0, cell); return { ...p, cells }; }); pendingFocus.current = cell.id; setActiveId(cell.id); setDeleted(null); }}><Undo2 size={15} />Hoàn tác</button><button className="button quiet" aria-label="Đóng thông báo" onClick={() => setDeleted(null)}>Đóng</button></div>}
    </div>
  );
};
export default App;
