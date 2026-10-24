import React, { useEffect, useRef, useState } from 'react';
import { ArrowDown, ArrowUp, BookOpen, Check, FileText, Headphones, Mic, MoreHorizontal, Paperclip, PenLine, Plus, Square, Trash2, X } from 'lucide-react';
import { readFileData } from '../lib/notebook';
import type { JupyterCell as CellType, SkillType, CellResource } from '../types/notebook';

interface Props {
  cell: CellType; index: number; totalCells: number; isActive: boolean;
  onSelect: () => void;
  onUpdateSource: (id: string, source: string) => void;
  onUpdateSkill: (id: string, skill: SkillType) => void;
  onUpdateResource: (id: string, resource: CellResource | undefined) => void;
  onRun: (id: string) => void; onDelete: (id: string) => void;
  onMoveUp: (index: number) => void; onMoveDown: (index: number) => void;
  onAddAbove: (index: number) => void; onAddBelow: (index: number) => void;
  onInsertTemplate: () => void;
}
const skills = { listening: { label: 'Listening', Icon: Headphones, resource: 'Bài nghe' }, reading: { label: 'Reading', Icon: BookOpen, resource: 'Bài đọc' }, writing: { label: 'Writing', Icon: PenLine, resource: 'Đề bài & tài liệu' }, speaking: { label: 'Speaking', Icon: Mic, resource: 'Thu âm & nghe lại' }, markdown: { label: 'Ghi chú', Icon: FileText, resource: 'Tài liệu đính kèm' } };
const formatTime = (n: number) => `${Math.floor(n / 60)}:${String(n % 60).padStart(2, '0')}`;

export const JupyterCell: React.FC<Props> = ({ cell, index, totalCells, isActive, onSelect, onUpdateSource, onUpdateSkill, onUpdateResource, onRun, onDelete, onMoveUp, onMoveDown, onAddAbove, onAddBelow, onInsertTemplate }) => {
  const fileInput = useRef<HTMLInputElement>(null);
  const audioRef = useRef<HTMLAudioElement>(null);
  const recorder = useRef<MediaRecorder | null>(null);
  const stream = useRef<MediaStream | null>(null);
  const timer = useRef<number | undefined>(undefined);
  const alive = useRef(true);
  const [recording, setRecording] = useState(false);
  const [seconds, setSeconds] = useState(0);
  const [busy, setBusy] = useState(false);
  const [error, setError] = useState('');
  const [dragging, setDragging] = useState(false);
  const [url, setUrl] = useState('');
  const [speed, setSpeed] = useState('1');
  const badge = skills[cell.cellType];
  const resource = cell.resource;
  const stale = resource?.url?.startsWith('blob:');
  useEffect(() => {
    alive.current = true;
    return () => { alive.current = false; window.clearInterval(timer.current); if (recorder.current?.state === 'recording') { recorder.current.onstop = null; recorder.current.stop(); } stream.current?.getTracks().forEach(t => t.stop()); };
  }, []);
  useEffect(() => { setError(''); setSpeed('1'); }, [resource?.url]);

  const attach = async (file: File) => {
    setError('');
    if (file.size > 2 * 1024 * 1024) { setError('Tệp lớn hơn 2 MB. Hãy dùng tệp nhỏ hơn để tự lưu được trong trình duyệt; bài nghe dài có thể dùng URL.'); return; }
    const name = file.name;
    const lower = name.toLowerCase();
    let type: CellResource['type'];
    if (file.type.startsWith('audio/') || /\.(mp3|wav|ogg|m4a|webm)$/.test(lower)) type = 'audio';
    else if (file.type === 'application/pdf' || lower.endsWith('.pdf')) type = 'pdf';
    else if (/^image\/(png|jpeg|webp|gif)$/.test(file.type) || /\.(png|jpe?g|webp|gif)$/.test(lower)) type = 'image';
    else if (/\.(txt|md)$/.test(lower)) type = 'text';
    else { setError('Chọn PDF, ảnh, âm thanh, TXT hoặc Markdown. Với DOCX, hãy xuất sang PDF trước khi đính kèm.'); return; }
    setBusy(true);
    try { const data = type === 'text' ? await file.text() : await readFileData(file); if (alive.current) onUpdateResource(cell.id, { type, name, ...(type === 'text' ? { textContent: data } : { url: data }) }); }
    catch { if (alive.current) setError('Không đọc được tệp. Hãy chọn lại.'); }
    finally { if (alive.current) setBusy(false); }
  };
  const start = async () => {
    setError('');
    if (!navigator.mediaDevices?.getUserMedia || !window.MediaRecorder) { setError('Trình duyệt này chưa hỗ trợ thu âm. Hãy mở bằng Chrome hoặc Firefox qua HTTPS / localhost.'); return; }
    if (resource?.type === 'audio' && !confirm('Bản thu mới sẽ thay tệp âm thanh trong cell này. Tiếp tục?')) return;
    setBusy(true);
    try {
      const input = await navigator.mediaDevices.getUserMedia({ audio: true });
      if (!alive.current) { input.getTracks().forEach(t => t.stop()); return; }
      stream.current = input;
      const media = new MediaRecorder(input); recorder.current = media;
      const chunks: Blob[] = []; let size = 0;
      media.ondataavailable = e => { chunks.push(e.data); size += e.data.size; if (size >= 1.8 * 1024 * 1024 && media.state === 'recording') media.stop(); };
      media.onstop = async () => {
        window.clearInterval(timer.current); input.getTracks().forEach(t => t.stop());
        if (!alive.current) return;
        setRecording(false); setBusy(true);
        try {
          const file = new File(chunks, `Speaking-${new Date().toISOString().slice(0, 10)}.webm`, { type: media.mimeType || 'audio/webm' });
          if (file.size > 2 * 1024 * 1024) throw new Error();
          const data = await readFileData(file);
          if (alive.current) onUpdateResource(cell.id, { type: 'audio', name: file.name, url: data });
        } catch { if (alive.current) setError('Bản thu quá lớn hoặc không đọc được. Hãy thu lại đoạn ngắn hơn.'); }
        finally { if (alive.current) setBusy(false); }
      };
      media.start(1000); setRecording(true); setSeconds(0);
      timer.current = window.setInterval(() => setSeconds(n => n + 1), 1000);
    } catch { stream.current?.getTracks().forEach(t => t.stop()); setError('Không mở được micro. Hãy cho phép micro trong trình duyệt rồi thử lại.'); }
    finally { if (alive.current) setBusy(false); }
  };
  const closeMenu = (e: React.MouseEvent) => { const details = e.currentTarget.closest('details'); if (details) details.open = false; };
  return (
    <section id={`cell-${cell.id}`} className={`notebook-cell ${isActive ? 'active' : ''}`} aria-label={`Cell ${index + 1}: ${badge.label}`} onFocusCapture={onSelect} onClick={onSelect}>
      <div className="cell-gutter" aria-label={`Lượt xem ${cell.executionCount ?? 'chưa có'}`}>In [{cell.executionCount ?? ' '}]:</div>
      <div className="cell-content">
        <header className="cell-header">
          <div className="cell-type"><badge.Icon size={16} /><select aria-label={`Kỹ năng cell ${index + 1}`} value={cell.cellType} disabled={recording || busy} onChange={e => onUpdateSkill(cell.id, e.target.value as SkillType)}>{Object.entries(skills).map(([key, value]) => <option key={key} value={key}>{value.label}</option>)}</select></div>
          <div className="cell-actions"><span className="cell-number">Cell {index + 1}</span><button className="button quiet next-cell" title="Đánh dấu đã xem và chuyển cell (Shift + Enter)" onClick={e => { e.stopPropagation(); onRun(cell.id); }}><Check size={15} />Tiếp theo</button>
            <details className="cell-menu" onClick={e => e.stopPropagation()} onKeyDown={e => { if (e.key === 'Escape') { e.currentTarget.open = false; e.currentTarget.querySelector('summary')?.focus(); } }}><summary className="icon-button" aria-label={`Thao tác cell ${index + 1}`}><MoreHorizontal size={19} /></summary><div className="options-panel" onClick={closeMenu}>
              <button onClick={onInsertTemplate}><FileText size={15} />Chèn dàn ý vào cuối bài</button>
              <button disabled={index === 0} onClick={() => onMoveUp(index)}><ArrowUp size={15} />Di chuyển lên</button>
              <button disabled={index === totalCells - 1} onClick={() => onMoveDown(index)}><ArrowDown size={15} />Di chuyển xuống</button>
              <button onClick={() => onAddAbove(index)}><Plus size={15} />Thêm cell phía trên</button>
              <button onClick={() => onAddBelow(index)}><Plus size={15} />Thêm cell phía dưới</button>
              <button className="danger-action" disabled={totalCells <= 1 || recording || busy} onClick={() => onDelete(cell.id)}><Trash2 size={15} />Xóa cell</button>
            </div></details>
          </div>
        </header>
        <div className="cell-panes">
          <div className="answer-pane"><div className="pane-heading"><label htmlFor={`editor-${cell.id}`}>Bài làm & ghi chú</label><span>Markdown</span></div><textarea id={`editor-${cell.id}`} value={cell.source} onChange={e => onUpdateSource(cell.id, e.target.value)} onKeyDown={e => { if (e.key === 'Enter' && e.shiftKey) { e.preventDefault(); onRun(cell.id); } }} placeholder="Viết bài làm, đáp án hoặc ghi chú ở đây…" spellCheck={false} /><div className="editor-footer">{cell.source.trim() ? cell.source.trim().split(/\s+/).length : 0} từ</div></div>
          <div className={`resource-pane ${dragging ? 'dragging' : ''}`} onDragOver={e => { e.preventDefault(); setDragging(true); }} onDragLeave={e => { if (!e.currentTarget.contains(e.relatedTarget as Node)) setDragging(false); }} onDrop={e => { e.preventDefault(); setDragging(false); if (!recording && !busy && e.dataTransfer.files[0]) void attach(e.dataTransfer.files[0]); }}>
            <div className="pane-heading"><span>{badge.resource}</span><div className="attachment-actions"><input hidden type="file" accept="audio/*,.pdf,.png,.jpg,.jpeg,.webp,.gif,.txt,.md" ref={fileInput} onChange={e => { if (e.target.files?.[0]) void attach(e.target.files[0]); e.target.value = ''; }} /><button className="button quiet" disabled={busy || recording} onClick={() => fileInput.current?.click()}><Paperclip size={14} />{resource && resource.type !== 'voice_recorder' ? 'Thay tệp' : 'Đính kèm'}</button>{resource && resource.type !== 'voice_recorder' && <button className="icon-button" disabled={busy || recording} aria-label="Gỡ tài liệu đính kèm" onClick={() => { if (confirm('Gỡ tài liệu khỏi cell này?')) onUpdateResource(cell.id, undefined); }}><X size={15} /></button>}</div></div>
            {busy && <p className="resource-status" role="status">Đang xử lý…</p>}
            {error && <p className="resource-error" role="alert">{error}</p>}
            {stale ? <div className="resource-empty"><Paperclip size={23} /><p>Tệp cũ cần được đính kèm lại</p><span>Liên kết từ phiên trước đã hết hạn. Chọn lại tệp để lưu cùng notebook.</span></div> : resource && !['voice_recorder', 'none'].includes(resource.type) ? <div className="resource-body">
              <div className="resource-filename" title={resource.name}>{resource.name || 'Tài liệu đính kèm'}</div>
              {resource.type === 'audio' && resource.url && <div className="audio-workspace"><Headphones size={25} /><audio key={resource.url} ref={audioRef} controls src={resource.url} onError={() => setError('Không phát được âm thanh. Hãy kiểm tra URL hoặc chọn lại tệp.')} /><div className="audio-tools"><button className="button outlined" onClick={() => { if (audioRef.current) audioRef.current.currentTime = Math.max(0, audioRef.current.currentTime - 5); }}><ArrowUp size={14} />Lùi 5 giây</button><label>Tốc độ <select aria-label="Tốc độ phát" value={speed} onChange={e => { setSpeed(e.target.value); if (audioRef.current) audioRef.current.playbackRate = Number(e.target.value); }}><option value="0.75">0.75×</option><option value="1">1×</option><option value="1.25">1.25×</option><option value="1.5">1.5×</option></select></label></div></div>}
              {resource.type === 'pdf' && resource.url && <><iframe src={resource.url} title={`PDF: ${resource.name || 'Đề bài'}`} /><a href={resource.url} target="_blank" rel="noreferrer">Mở PDF riêng</a></>}
              {resource.type === 'image' && resource.url && <img src={resource.url} alt={resource.name || 'Hình minh họa đề bài'} />}
              {resource.type === 'text' && <div className="reference-text">{resource.textContent}</div>}
            </div> : cell.cellType !== 'speaking' && <div className="resource-empty"><Paperclip size={23} /><p>Giữ tài liệu ngay bên bài làm</p><span>Kéo thả hoặc đính kèm PDF, ảnh, âm thanh, TXT.<br />Tối đa 2 MB mỗi tệp.</span><button className="button outlined" disabled={busy} onClick={() => fileInput.current?.click()}>Chọn tài liệu</button></div>}
            {cell.cellType === 'listening' && !resource?.url && <form className="audio-url" onSubmit={e => { e.preventDefault(); try { const parsed = new URL(url); if (!['https:', 'http:'].includes(parsed.protocol)) throw new Error(); onUpdateResource(cell.id, { type: 'audio', name: 'Bài nghe từ URL', url: parsed.href }); setError(''); } catch { setError('Nhập đường dẫn âm thanh bắt đầu bằng https:// hoặc http://.'); } }}><label htmlFor={`url-${cell.id}`}>Hoặc dùng đường dẫn bài nghe</label><div><input id={`url-${cell.id}`} type="url" required placeholder="https://…/audio.mp3" value={url} onChange={e => setUrl(e.target.value)} /><button className="button outlined" disabled={busy}>Mở</button></div></form>}
            {cell.cellType === 'speaking' && <div className="recorder"><Mic size={24} /><p>{recording ? 'Đang thu âm' : 'Luyện nói, rồi nghe lại'}</p><span className="recording-time" role="status">{recording ? formatTime(seconds) : 'Bản thu được lưu cùng notebook'}</span>{recording ? <button className="button record-stop" onClick={() => { if (recorder.current?.state === 'recording') recorder.current.stop(); }}><Square size={14} />Dừng thu âm</button> : <button className="button outlined" disabled={busy} onClick={start}><Mic size={15} />Bắt đầu thu âm</button>}</div>}
          </div>
        </div>
      </div>
    </section>
  );
};
