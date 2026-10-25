# IELTS Notebook — Fullstack Architecture & Data Persistence

Hệ thống IELTS Notebook gồm hai phần độc lập nhưng liên kết chặt chẽ:
- **Frontend (`frontend/`)**: Ứng dụng React 19 + TypeScript + Vite, cung cấp giao diện Notebook chia đôi màn hình (trái: Markdown editor, phải: Tài nguyên Audio/PDF/Text/Voice Recorder).
- **Backend (`backend/`)**: Dịch vụ Ruby on Rails 8 API kết nối cơ sở dữ liệu quan hệ (SQLite3 / PostgreSQL), hỗ trợ giao dịch nguyên tử (ACID transactions), quản lý phiên bản snapshot tự động và tác vụ quản trị database dài hạn.

---

## 1. Kiến trúc luồng dữ liệu & Quản trị Database

```
+-----------------------------------------------------------------+
|                         FRONTEND (Vite)                         |
|  - UI State & LocalStorage Cache (Offline-ready, debounce 350ms)|
|  - Auto-Sync / Checkpoint / Snapshot Restoration UI             |
+--------------------------------+--------------------------------+
                                 |  /api/v1/... (JSON REST)
                                 v
+--------------------------------+--------------------------------+
|                       BACKEND (Rails 8 API)                     |
|  - Health & Metrics API (/api/v1/health)                        |
|  - Atomic Notebook & Cells Sync (/api/v1/notebooks/:id/sync)    |
|  - Snapshots & Rollback (/api/v1/notebooks/:id/snapshots)       |
+--------------------------------+--------------------------------+
                                 |  ActiveRecord (Foreign Keys, WAL)
                                 v
+--------------------------------+--------------------------------+
|                     DATABASE & PERSISTENCE                      |
|  - `notebooks` (id, title, timestamps)                          |
|  - `cells` (id, notebook_id, position, cell_type, source, res) |
|  - `notebook_snapshots` (checkpoint history & recovery)         |
|  - Storage: `storage/development.sqlite3` / `production.sqlite3` |
+-----------------------------------------------------------------+
```

### Điểm cốt lõi đảm bảo dữ liệu khi deploy lâu dài:
1. **Lưu trữ hai lớp (Hybrid Resilience)**: Dữ liệu được ghi lập tức vào `localStorage` của trình duyệt phòng mất kết nối, đồng thời gửi đồng bộ nguyên tử tới Rails database qua debounced API call.
2. **Toàn vẹn quan hệ (Relational Integrity)**: Cấu trúc Notebook - Cell được liên kết bằng Foreign Key `on_delete: :cascade`, đánh chỉ mục kép `[:notebook_id, :position]` giúp truy vấn và sắp xếp thứ tự cell cực nhanh.
3. **Quản trị phiên bản & Snapshot (Disaster Recovery)**: Mỗi lần đồng bộ hoặc người dùng bấm "Create Checkpoint", hệ thống lưu bản sao JSON vào bảng `notebook_snapshots`. Người dùng có thể quay ngược lại (rollback) bất kỳ phiên bản nào trực tiếp từ giao diện hoặc qua API.
4. **Tác vụ Rake quản trị cơ sở dữ liệu**:
   - `bin/rake notebook:stats`: Xem thống kê dung lượng, số lượng notebook, phân bổ cell theo kỹ năng.
   - `bin/rake notebook:backup`: Xuất bản sao lưu toàn bộ dữ liệu ra thư mục `storage/backups/`.
   - `bin/rake notebook:restore[file_path]`: Khôi phục cơ sở dữ liệu từ file backup JSON.
   - `bin/rake notebook:prune_snapshots`: Dọn dẹp snapshot cũ giữ tối đa 25 phiên bản gần nhất mỗi notebook.

---

## 2. Hướng dẫn chạy Development

### Khởi động Backend (Rails 8):
```bash
cd backend
bin/rails db:migrate
bin/rails db:seed    # Nạp dữ liệu mẫu ban đầu nếu trống
bin/rails server -p 3000
```
Backend API sẽ lắng nghe tại `http://localhost:3000`. Endpoint kiểm tra sức khỏe: `http://localhost:3000/api/v1/health`.

### Khởi động Frontend (React + Vite):
```bash
cd frontend
npm install
npm run dev
```
Frontend sẽ mở tại `http://localhost:5173`. Các request tới `/api` được cấu hình proxy tự động sang `http://127.0.0.1:3000`.

---

## 3. Kiểm thử (Testing)

- **Frontend tests (18 tests)**:
  ```bash
  cd frontend
  npm test
  npm run build
  ```
- **Backend tests (5 integration tests)**:
  ```bash
  cd backend
  bin/rails test
  ```

---

## 4. Hướng dẫn Triển khai Lâu dài (Production Deployment)

### Tùy chọn A: Docker / Kamal (Mặc định trong Rails 8)
1. Thư mục `backend/Dockerfile` và `backend/config/deploy.yml` đã được cấu hình sẵn.
2. Thư mục `storage/` chứa file database SQLite `production.sqlite3` và thư mục bản sao lưu `storage/backups/`. Khi deploy bằng Docker, mount volume ra persistent volume máy chủ (ví dụ: `/var/data/ielts/storage:/rails/storage`).

### Tùy chọn B: Sử dụng PostgreSQL cho quy mô lớn
Nếu chuyển sang PostgreSQL:
1. Thêm gem `pg` vào `Gemfile` (đã có sẵn trong hệ thống).
2. Thiết lập biến môi trường `DATABASE_URL=postgres://user:pass@host:5432/ielts_db`.
3. Chạy `bin/rails db:migrate`.

### Cấu hình biến môi trường Production
- `FRONTEND_URL`: Danh sách URL frontend được phép truy cập CORS (phân cách bằng dấu phẩy, ví dụ `https://ielts.yourdomain.com`).
- `RAILS_ENV=production`
- `SECRET_KEY_BASE`: Khóa bí mật của Rails (tạo bằng `bin/rails secret`).
- `VITE_API_URL`: Trên frontend (khi build), cấu hình trỏ tới URL backend API nếu không đặt cùng domain reverse-proxy.
