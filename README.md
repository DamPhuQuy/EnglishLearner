# IELTS Notebook — Mini-IELTS Architecture & Cloudflare Backend

---

## 1. Kiến trúc luồng dữ liệu & Nền tảng Cloudflare

```
+-----------------------------------------------------------------+
|                         FRONTEND (Vite + React)                 |
|  - UI State & LocalStorage Cache (Offline-ready, debounce 350ms)|
|  - Cấu trúc Mini-IELTS: Mỗi Cell là một bài tập thực chiến      |
|    (Reading, Listening, Writing, Speaking)                     |
|  - Tích hợp Cloudflare R2 Uploads cho Audio/Files/Recordings    |
+--------------------------------+--------------------------------+
                                 |  /api/v1/... (JSON REST)
                                 v
+--------------------------------+--------------------------------+
|          BACKEND (Hono on Cloudflare Workers Runtime)           |
|  - Ultra-low latency Serverless API                             |
|  - Health & Metrics API (/api/v1/health)                        |
|  - Atomic Notebook & Cells Sync (/api/v1/notebooks/:id/sync)    |
|  - Versioned Snapshots & Rollback (/api/v1/.../snapshots)       |
|  - Cloudflare R2 Asset Engine (/api/v1/upload & /api/v1/files)  |
+--------------------------------+--------------------------------+
                                 |  D1 DDL / Prepared Batch SQL
                                 v
+--------------------------------+--------------------------------+
|                     DATABASE & OBJECT STORAGE                   |
|  - Cloudflare D1 (SQLite Engine: notebooks, cells, snapshots)   |
|  - Cloudflare R2 (Object Storage for audio, recordings, docs)   |
+-----------------------------------------------------------------+
```

### Điểm cốt lõi:

1. **Mô hình Mini-IELTS theo từng Cell**:
   - Giao diện và cơ chế split-pane (giao diện, thao tác chuột, phím tắt `Shift + Enter`, gutter số thứ tự) được giữ nguyên vẹn.
   - Mỗi cell đại diện cho một "bài tập nhỏ" chuẩn phong cách **Mini-IELTS**:
     - **Reading Cell**: Bên phải là bài đọc học thuật hoàn chỉnh chia đoạn [A], [B], [C]...; Bên trái là phiếu câu hỏi (True/False/Not Given, Summary Completion, Lexical bank) với các ô điền `[Q1]`, `[Q2]`...
     - **Listening Cell**: Bên phải là Audio Player kết hợp script; Bên trái là hệ thống câu hỏi Notes/Table completion và phân tích Connected speech.
     - **Writing Cell**: Bên phải là đề bài và biểu đồ số liệu Task 1/2; Bên trái là dàn bài, bài luận draft, bộ đếm từ và rubric tự đánh giá.
     - **Speaking Cell**: Bên phải là Voice Recorder Studio; Bên trái là Cue Card Part 2, dàn ý 1 phút chuẩn bị và checklist tiêu chí chấm điểm.
2. **Backend Serverless chuẩn Cloudflare**:
   - Xây dựng hoàn toàn trên **Hono Framework** tối ưu cho **Cloudflare Workers**.
   - Cơ sở dữ liệu: **Cloudflare D1** (Serverless SQLite) với bảng `notebooks`, `cells` và `notebook_snapshots` đánh chỉ mục `[notebook_id, position]`.
   - Lưu trữ tệp tin: **Cloudflare R2** qua endpoint `/api/v1/upload` và streaming `/api/v1/files/*` giúp lưu audio, hình ảnh, file PDF và bản ghi âm mà không làm phình to SQLite/localStorage.
3. **Structured Schema & AI Prompting cho User Client**:
   - Đặc tả chuẩn quốc tế cho cả 4 kỹ năng trong tệp [`SCHEMA_README.md`](file:///home/phuqy/Develop/IELTS/SCHEMA_README.md) và JSON Schema độc lập tại [`ielts-exercise-schema.json`](file:///home/phuqy/Develop/IELTS/ielts-exercise-schema.json).
   - Cho phép người dùng copy prompt đưa vào ChatGPT / Claude / Gemini / DeepSeek tạo bài tập `.json`, sau đó kéo thả / dán trực tiếp lên ứng dụng web để tự động render giao diện câu hỏi tương tác (TFNG, MCQ, matching, ô điền từ, timer...).
4. **Quản trị dòng lệnh với Cloudflare CLI (Wrangler)**:
   - Toàn bộ thao tác cơ sở dữ liệu và triển khai đều tích hợp sẵn qua `wrangler`.
   - Cấu trúc backend phân tầng theo mô hình Java Clean Architecture (`controller/` -> `service/` -> `repository/` -> `model/` / `dto/`).

---

## 2. Hướng dẫn chạy Development

### Khởi động Backend (Hono + Cloudflare Worker):

```bash
cd backend
npm install

# 1. Chạy migration cho database Cloudflare D1 local:
npm run db:migrate:local

# 2. Khởi động Worker dev server trên port 3000:
npm run dev
```

Backend API sẽ lắng nghe tại `http://localhost:3000`.
- Endpoint kiểm tra sức khỏe: `http://localhost:3000/api/v1/health` (thông báo trạng thái Cloudflare D1 và R2).
- Thử upload file lên R2: `POST http://localhost:3000/api/v1/upload`.

### Các lệnh Cloudflare CLI hữu ích:

```bash
# Nạp lại dữ liệu mẫu Mini-IELTS vào D1 local:
npm run db:seed

# Chạy migration lên Cloudflare D1 production:
npm run db:migrate:remote

# Deploy Worker lên Cloudflare toàn cầu:
npm run deploy
```

### Khởi động Frontend (React + Vite):

```bash
cd frontend
npm install
npm run dev
```

Frontend sẽ mở tại `http://localhost:5173`. Các request `/api` tự động được proxy sang `http://127.0.0.1:3000` của Cloudflare Worker.
