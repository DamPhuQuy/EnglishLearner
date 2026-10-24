# Product — IELTS Notebook

<!-- impeccable:product-schema 1 -->

Nguồn sự thật về mục đích, hành vi và giới hạn sản phẩm. Baseline: giao diện compact notebook đã được người dùng chấp nhận ngày 2026-10-25. [DESIGN.md](DESIGN.md) quy định hệ thống giao diện; tài liệu trong `process/` giữ lịch sử nghiên cứu và quyết định, không thay thế baseline này.

Thay đổi yêu cầu sản phẩm phải cập nhật tài liệu này cùng implementation. Khi phát hiện sai khác, ghi rõ đó là lỗi implementation hay thay đổi yêu cầu; không tự dùng kế hoạch cũ để mở rộng phạm vi.

## Platform

web

## Users

Người học IELTS tự luyện Listening, Reading, Writing và Speaking. Nhu cầu cốt lõi là viết bài, ghi đáp án hoặc ghi chú trong khi xem tài liệu hay nghe âm thanh ngay bên cạnh. Hướng đã chốt: gọn như Jupyter/Colab, ưu tiên học và viết.

## Product Purpose

Một notebook tương tác chạy trong trình duyệt, tổ chức bài luyện theo cell. Mỗi cell đặt vùng viết Markdown cạnh vùng tài nguyên độc lập để người học giữ bài làm và ngữ cảnh trong cùng không gian.

Thành công nghĩa là người học thêm cell, viết bài, dùng tài liệu hoặc thu âm, tiếp tục sang cell khác và giữ lại nội dung qua lưu cục bộ hoặc xuất tệp. Không có cơ chế chấm band hay đánh giá đúng/sai tự động.

## Positioning

Mô hình notebook phục vụ luyện ngôn ngữ: Markdown ở bên trái, tài liệu hoặc công cụ nghe/nói ở bên phải. Vùng phải không phải bản render của Markdown bên trái. Lấy thao tác theo cell từ notebook, không yêu cầu Python, kernel hay cài runtime học tập riêng.

## Operating Context

- Một ứng dụng React/TypeScript chạy bằng Vite, dùng CSS và Tailwind; icon từ Lucide React. Lệnh phát triển: `npm run dev`; kiểm tra: `npm test`, `npm run build`.
- Một notebook đang mở tại một thời điểm, không có điều hướng nhiều workspace hay thư viện notebook.
- Nội dung chủ yếu xử lý và lưu trên trình duyệt. Audio URL và URL tài nguyên được nhập có thể truy cập mạng; không cam kết toàn bộ ứng dụng hoạt động offline.
- Thu âm cần trình duyệt hỗ trợ `MediaRecorder`, quyền micro và môi trường HTTPS hoặc localhost.
- Ngôn ngữ UI là tiếng Việt; giữ tên kỹ năng IELTS bằng tiếng Anh. Người học có thể viết nội dung tiếng Anh hoặc tiếng Việt.

## Capabilities and Constraints

### Notebook và thao tác cell

- Đổi tên notebook; thêm, xóa, đổi thứ tự cell. Có ít nhất một cell; xóa cell có một bước hoàn tác cho cell vừa xóa.
- Năm loại cell: `listening`, `reading`, `writing`, `speaking`, `markdown` (nhãn UI: Ghi chú).
- Bên trái luôn là textarea soạn Markdown thô, có đếm từ theo khoảng trắng. Chưa có chế độ render Markdown, rich text hoặc thực thi mã.
- Đổi kỹ năng không tự thay bài làm hoặc loại tài nguyên đang đính kèm.
- “Tiếp theo” và Shift + Enter tăng `executionCount`, đánh dấu lượt xem và đưa focus sang editor kế tiếp; ở cell cuối giữ focus tại đó. `In [n]:` là dấu hiệu notebook được giữ lại, không phải số lần chạy chương trình hay điểm hoàn thành bài học.
- Chèn dàn ý nối thêm nội dung vào cuối bài, không ghi đè bài hiện có.

### Tài nguyên và luyện tập

- Mỗi cell có một trường `resource`: âm thanh, PDF, ảnh, văn bản hoặc trạng thái công cụ thu âm. Chưa hỗ trợ nhiều tệp song song trong cùng cell.
- Kéo thả hoặc chọn tệp: âm thanh, PDF, PNG/JPEG/WebP/GIF, TXT, Markdown. Giới hạn tệp cục bộ là 2 MiB (`2 × 1024 × 1024` byte); UI gọi là 2 MB.
- DOCX chưa được giải mã hoặc preview trực tiếp. Hướng dẫn người học chuyển sang PDF.
- Loại tài nguyên quyết định cách hiển thị, độc lập với kỹ năng của cell. PDF dùng iframe của trình duyệt và có liên kết mở riêng; ảnh và văn bản có vùng xem riêng.
- Audio dùng player native, tua lùi 5 giây và tốc độ 0.75×, 1×, 1.25×, 1.5×. Listening cho phép nhập URL HTTP/HTTPS khi chưa có URL tài nguyên.
- Speaking thu âm, dừng và nghe lại; bản thu được đưa vào trường `resource`. Nếu cell đang có audio, thu mới cần xác nhận thay audio đó. Chưa có hai bản audio mẫu/bản thu lưu song song, waveform hoặc so sánh phát âm tự động.

### Lưu, nhập và xuất

- Tự lưu notebook JSON vào `localStorage`, khóa `ielts_jupyter_notebook_v2`, sau khoảng 350 ms không đổi nội dung; có thêm ghi khi rời trang. Hiển thị đang lưu, đã lưu hoặc lỗi lưu thực tế.
- Lưu cục bộ gắn với trình duyệt và origin. Không có đồng bộ tài khoản, cloud backup hay lưu trực tiếp vào Git. Tổng dung lượng phụ thuộc quota trình duyệt; giới hạn mỗi tệp không bảo đảm toàn notebook luôn vừa quota.
- Tệp nhị phân mới dùng data URL; TXT/Markdown lưu nội dung văn bản. Liên kết blob cũ được báo cần đính kèm lại.
- Xuất JSON theo cấu trúc riêng với đuôi `.ilnb`; có thể nhập `.ilnb`, `.json`, `.ipynb` nếu nội dung tuân theo cấu trúc riêng này. Đuôi `.ipynb` không đồng nghĩa tương thích chuẩn Jupyter Notebook.
- Notebook nhập tối đa 20 MiB. Kiểm tra trường dữ liệu, loại cell, ID không trùng, bộ đếm và scheme URL; cần xác nhận trước khi thay notebook hiện tại.
- Dữ liệu chính: notebook `{ id, title, cells }`; cell `{ id, executionCount, cellType, source, resource? }`; resource `{ type, url?, name?, textContent? }`. Định nghĩa cụ thể ở [src/types/notebook.ts](src/types/notebook.ts), kiểm tra import ở [src/lib/notebook.ts](src/lib/notebook.ts).

### Chưa có trong baseline

Tài khoản, backend, đồng bộ nhiều thiết bị, nhiều người cùng sửa, AI chấm bài, dự đoán band, ngân hàng đề IELTS chính thức, transcript đồng bộ, dictation chấm tự động, phân tích AST, xuất Markdown hoặc tích hợp VS Code thực tế đều chưa được triển khai. Các ý tưởng trong kế hoạch ban đầu không tự trở thành tính năng sản phẩm.

## Brand Commitments

Tên hiển thị: **IELTS Notebook**. Giọng điệu trực tiếp, ngắn, hữu ích cho người học. Tên thao tác phải mô tả hành động thật; không dựng trạng thái kernel, engine hay năng lực đánh giá không tồn tại. Giữ hướng notebook gọn đã được người dùng chọn và chấp nhận; các quy định visual nằm trong [DESIGN.md](DESIGN.md).

## Evidence on Hand

- [src/App.tsx](src/App.tsx): shell notebook, thêm/xóa/chuyển cell, import/export, lưu cục bộ.
- [src/components/JupyterCell.tsx](src/components/JupyterCell.tsx): editor, tài nguyên, audio, thu âm.
- [src/data/initialSample.ts](src/data/initialSample.ts): notebook mẫu bốn kỹ năng. Nội dung là demo; audio sonar được ghi nhãn demo, không phải bài Cambridge. Các prompt/số liệu mẫu không phải đề chính thức đã được kiểm chứng.
- [tests/notebook.test.js](tests/notebook.test.js): cấu trúc mẫu và một số ràng buộc import; không thay thế kiểm thử tương tác trình duyệt.
- [review-ui.md](process/features/active/ielts-notebook-workbench/review-ui.md): bằng chứng kiểm tra của đợt sửa UI. Người dùng chấp nhận bản hiện tại; phiên làm việc chưa có ảnh desktop/mobile hoặc xác nhận browser smoke test.
- Không có bằng chứng về hiệu quả tăng band, chứng nhận IELTS, tích hợp Cambridge, khách hàng, testimonial hoặc số liệu sử dụng. Không tự thêm các claim này.

## Product Principles

1. Ưu tiên bài làm và tài liệu: cơ chế notebook phải giảm thao tác trong lúc học.
2. Giữ vùng viết và vùng tài nguyên độc lập; đổi loại cell không làm mất ngữ cảnh.
3. Bảo vệ nội dung người học bằng lưu có trạng thái thật, khả năng xuất tệp và thao tác có đường phục hồi.
4. Nói đúng khả năng hiện có; phân biệt demo, kế hoạch tương lai và chức năng đã triển khai.
5. Giữ sản phẩm nhẹ, dùng trực tiếp trong trình duyệt, không yêu cầu runtime notebook riêng.

## Accessibility & Inclusion

Baseline có nhãn cho editor và các điều khiển chính, focus bàn phím nhìn thấy, skip link, status/alert cho trạng thái động, và Shift + Enter chuyển cell. Responsive xếp hai vùng theo chiều dọc trên màn hình hẹp; CSS tôn trọng reduced motion. Chưa có kiểm toán WCAG hoặc kiểm thử screen reader đầy đủ; không ghi nhận như chứng nhận đạt chuẩn.
