# IELTS Backend — Java-Style Clean Layered Architecture

Hệ thống backend được tái cấu trúc theo mô hình **Clean Layered Architecture chuẩn Java / Spring Boot**, vận hành tối ưu trên nền tảng **Hono Framework** và **Cloudflare Workers (D1 SQLite + R2 Storage)**.

---

## 🏛 Cấu trúc thư mục (Layered Architecture)

```
backend/src/
├── config/                         # [Configuration Layer]
│   └── env.ts                      # Cloudflare Bindings (DB, BUCKET) & tham số cấu hình
│
├── controller/                     # [Presentation Layer / REST Controllers]
│   ├── HealthController.ts         # GET /api/v1/health (System telemetry)
│   ├── NotebookController.ts       # CRUD /api/v1/notebooks, sync, import, export
│   ├── SnapshotController.ts       # Versioned checkpoints & rollback
│   └── StorageController.ts        # POST /api/v1/upload, GET & DELETE /api/v1/files/*
│
├── service/                        # [Business Logic Layer]
│   ├── HealthService.ts            # Thu thập metrics & kiểm tra trạng thái D1/R2
│   ├── NotebookService.ts          # Nghiệp vụ sổ tay, sắp xếp cell, điều phối snapshot
│   ├── SnapshotService.ts          # Quản lý checkpoint, pruning snapshot cũ (>25 bản)
│   └── StorageService.ts           # Upload, stream file, quản lý object storage R2
│
├── repository/                     # [Data Access Layer (DAO)]
│   ├── CellRepository.ts           # Batch SQL statements & truy vấn bảng cells
│   ├── NotebookRepository.ts       # DDL & truy vấn bảng notebooks
│   └── SnapshotRepository.ts       # Truy vấn & dọn dẹp bảng notebook_snapshots
│
├── model/                          # [Domain Models & Entities]
│   ├── Cell.ts                     # Entity Cell, CellRow, CellResource
│   ├── Notebook.ts                 # Entity Notebook, NotebookRow
│   └── Snapshot.ts                 # Entity Snapshot, SnapshotRow
│
├── dto/                            # [Data Transfer Objects]
│   ├── HealthDto.ts                # DTO trả về trạng thái hệ thống
│   ├── NotebookDto.ts              # Request/Response DTO cho notebooks & sync
│   ├── SnapshotDto.ts              # DTO cho danh sách và chi tiết snapshot
│   └── StorageDto.ts               # DTO cho kết quả upload file lên R2
│
└── index.ts                        # [Application Bootstrap / Router Entry]
```

---

## 🛠 Nguyên lý thiết kế (Design Principles)

1. **Separation of Concerns (SoC)**:
   - **Controller**: Chỉ chịu trách nhiệm tiếp nhận HTTP Request, routing, validate dữ liệu đầu vào và trả về HTTP Status Code.
   - **Service**: Xử lý logic nghiệp vụ, điều phối giữa các Repository và Storage, không phụ thuộc vào Hono Context.
   - **Repository**: Đóng gói các câu lệnh SQL D1 Prepared Statements và D1 Batch Execution.
   - **Model & DTO**: Tách bạch rõ ràng giữa Database Entity (`*Row`) và Data Transfer Object (`*Dto`).
2. **Cloudflare Native**:
   - Sử dụng `D1Database` (SQLite Serverless) cho dữ liệu quan hệ và quan hệ cascade.
   - Sử dụng `R2Bucket` cho tệp đính kèm (Audio, PDF, Image, Voice Recording).
