---
name: IELTS Notebook
description: Notebook gọn cho việc học
colors:
  canvas: "#14171c"
  surface: "#1b1f25"
  raised: "#242a32"
  line: "#343b45"
  text: "#e3e7ed"
  muted: "#a5afbc"
  accent: "#a9c5ff"
  accent-bg: "#283c5f"
  danger: "#ffb4ae"
  danger-line: "#754641"
typography:
  headline:
    fontFamily: 'Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif'
    fontSize: "23px"
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: "-0.025em"
  body:
    fontFamily: 'Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif'
    fontSize: "14px"
  control:
    fontFamily: 'Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif'
    fontSize: "13px"
    lineHeight: 1.4
  label:
    fontFamily: 'Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif'
    fontSize: "12px"
  metadata:
    fontFamily: 'Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif'
    fontSize: "11px"
  editor:
    fontFamily: "ui-monospace, SFMono-Regular, Consolas, monospace"
    fontSize: "13px"
    lineHeight: 1.85
rounded:
  menu-item: "4px"
  field: "5px"
  control: "6px"
  container: "8px"
spacing:
  compact: "4px"
  tight: "8px"
  small: "12px"
  medium: "16px"
  pane: "20px"
  section: "24px"
  page: "32px"
components:
  button-primary:
    backgroundColor: "{colors.accent-bg}"
    textColor: "#dce8ff"
    typography: "{typography.control}"
    rounded: "{rounded.control}"
    padding: "7px 10px"
  button-primary-hover:
    backgroundColor: "#354e76"
  button-outlined:
    backgroundColor: "transparent"
    textColor: "{colors.text}"
    typography: "{typography.control}"
    rounded: "{rounded.control}"
    padding: "7px 10px"
  button-quiet:
    backgroundColor: "transparent"
    textColor: "{colors.muted}"
    typography: "{typography.control}"
    rounded: "{rounded.control}"
    padding: "7px 10px"
  url-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.text}"
    typography: "{typography.label}"
    rounded: "{rounded.field}"
    padding: "6px 9px"
  notebook-cell:
    backgroundColor: "{colors.surface}"
    rounded: "{rounded.container}"
  options-menu:
    backgroundColor: "{colors.raised}"
    typography: "{typography.control}"
    rounded: "{rounded.container}"
    padding: "8px"
  notebook-toolbar:
    backgroundColor: "{colors.canvas}"
    padding: "10px 32px"
  resource-empty:
    textColor: "{colors.muted}"
    padding: "18px 12px"
---

# Design System: IELTS Notebook

## Overview

**Creative North Star: "Notebook gọn cho việc học"**

Giao diện notebook tối, gọn như Jupyter/Colab, dành phần lớn không gian cho bài làm và tài liệu. Mật độ vừa phải, chữ nhỏ ở điều khiển và thông tin phụ, vùng viết thoáng hơn nhờ chiều cao dòng. Điểm nhấn xanh dịu giúp nhận ra thao tác chính và vị trí đang chọn.

Đây là bản ghi từ implementation hiện tại, không phải đề xuất thiết kế mới. Nguồn: `src/index.css`, `src/App.tsx`, `src/features/cell/components/JupyterCell.tsx`; mục đích và giới hạn hành vi ở [PRODUCT.md](PRODUCT.md). Chưa có ảnh chụp hay kiểm tra computed style bằng trình duyệt trong phiên này; tài liệu không xác nhận chất lượng hiển thị hoặc khả năng tiếp cận đã được kiểm toán.

DESIGN.md là hợp đồng visual chuẩn của baseline đã được chấp nhận: frontmatter quy định token, phần văn xuôi hướng dẫn áp dụng, sidecar là bản dẫn xuất để hiển thị ví dụ. Khi thay đổi visual được chấp thuận, cập nhật source, DESIGN.md và sidecar cùng nhau. Kế hoạch cũ trong `process/` hoặc token Tailwind còn sót không ghi đè hợp đồng này.

**Key Characteristics:**
- Nền tối nhiều lớp, phân vùng bằng đường viền mảnh.
- Một điểm nhấn xanh dịu dùng cho thao tác và trạng thái chọn.
- Điều khiển gọn, vùng viết monospace, tài liệu dễ đọc.
- Cell lặp lại; hai vùng xếp dọc khi màn hình hẹp.

## Colors

Palette lấy trực tiếp từ custom properties trong stylesheet; YAML là nguồn giá trị chuẩn. Các màu literal chỉ dành cho một trạng thái được giữ ở component hoặc snippet, không nâng thành primitive toàn sản phẩm.

### Primary

- **Xanh dịu — `accent`:** icon nhận diện, liên kết, dấu nháy nhập, gutter cell đang chọn và focus bàn phím.
- **Nền xanh thao tác — `accent-bg`:** nút thêm cell và nền vùng nhận tệp khi kéo thả. Chữ và hover của nút chính là màu riêng trong component.

### Neutral

- **Nền trang — `canvas`:** vùng ngoài cell, toolbar và trường URL.
- **Nền cell — `surface`:** header ứng dụng và thân cell; vùng tài nguyên có sắc nền tối riêng trong snippet.
- **Nền nổi — `raised`:** menu, thông báo hoàn tác và hover thông thường.
- **Đường chia — `line`:** khung cell, nút viền và ranh giới giữa hai vùng.
- **Chữ chính — `text`:** bài làm, nhãn chính và nội dung đọc.
- **Chữ phụ — `muted`:** mô tả, metadata, tên tệp và điều khiển ít ưu tiên.

`danger` và `danger-line` dùng cho lỗi, thao tác xóa hoặc dừng thu âm; không phải màu phân loại kỹ năng.

**The Shared Skill Palette Rule.** Các kỹ năng dùng cùng hệ màu; phân biệt bằng tên và icon, không gán một màu nhấn riêng cho từng kỹ năng.

## Typography

**Body Font:** stack sans-serif trong YAML. Inter đứng đầu stack nhưng dự án chưa tải hoặc tự host Inter; font thực tế phụ thuộc máy người dùng.

**Label/Mono Font:** editor và gutter dùng stack monospace của hệ điều hành. Không có display face riêng hoặc cỡ chữ quảng bá.

### Hierarchy

- **Headline:** tiêu đề tài liệu theo token `headline`; giảm còn (21px) ở màn hình hẹp.
- **Body:** tài liệu chữ và nội dung trạng thái chính dùng (14px); tài liệu chữ có line-height (1.8), rộng tối đa (72ch), giữ xuống dòng và cuộn khi cao quá (320px).
- **Control:** nút và select chủ yếu (13px); nhãn loại cell có weight (500).
- **Label:** nhãn vùng, trạng thái lưu và mô tả phụ dùng (12px).
- **Metadata:** gutter, số cell, đếm từ và tên tệp dùng (11px). Đếm từ và thời gian dùng chữ số tabular.
- **Editor:** token `editor`; tăng lên (14px) khi viewport từ (1500px) hoặc không quá (760px). Editor là textarea Markdown thô.

**The Writing Rhythm Rule.** Giữ line-height (1.85) cho vùng soạn thảo; không nén bài làm theo mật độ của toolbar.

## Layout

Header và toolbar đặt trong khung rộng tối đa (1440px), căn giữa; notebook rộng tối đa (1344px). Desktop dùng padding ngang (32px), notebook padding trên (32px), gutter cell (66px). Tiêu đề tài liệu, nút thêm cuối trang và footer thẳng với thân cell. Khoảng cách giữa các cell là (24px).

Cell có header riêng và hai cột bằng nhau `minmax(0, 1fr)`. Bài làm ở trái, tài nguyên độc lập ở phải. Padding ngang mỗi vùng là (20px). Textarea cao tối thiểu (245px), có thể kéo giãn dọc. Đây là bố cục cell hiện tại; không suy rộng thành mọi bề mặt sản phẩm.

Responsive theo các media query thực tế:
- **Không quá 1100px:** header cho phép xuống dòng; gutter còn (54px), padding ngang vùng cell còn (16px).
- **Không quá 760px:** gutter lên trên cell; bài làm rồi tài nguyên xếp dọc. Header/toolbar có padding ngang (16px), notebook (12px); textarea cao tối thiểu (210px). Nút, summary và select có min-height (44px); input vẫn giữ min-height (36px). Ẩn hướng dẫn toolbar, số cell và nhắc phím tắt footer để giảm chật.
- **Từ 1500px:** notebook padding trên (40px); textarea cao tối thiểu (270px).

Trang có min-width (320px). Các giá trị YAML ghi lại nhịp khoảng cách lặp lại, không ép mọi khoảng cách vào một lưới duy nhất.

## Elevation & Depth

Không có box-shadow trong stylesheet hiện tại. Độ sâu đến từ nền trang, cell, menu và đường viền. Menu dùng position absolute, z-index (20); thông báo hoàn tác cố định dùng z-index (50), skip link (100). Viền menu, viền cell đang chọn và viền hoàn tác là màu trạng thái cục bộ trong snippet.

**The Tonal Depth Rule.** Giữ phân tầng bằng nền và viền như các container hiện có; không thêm shadow mặc định vào cell.

## Shapes

Hình khối chữ nhật bo nhẹ: container và menu theo token `container`, nút theo `control`, field/select/icon button theo `field`, menu item theo `menu-item`. Đường viền thường (1px), không có card nổi hoặc pill phân loại kỹ năng. Textarea riêng có radius (3px). Khi xếp hai cột, góc dưới phải vùng tài nguyên bo (8px); khi xếp dọc, cả hai góc dưới bo (8px).

## Components

### Buttons

Nút chữ gọn, icon nét đi kèm khi hữu ích. Ba biến thể `primary`, `outlined`, `quiet` dùng token ở trên; min-height thông thường (36px). Icon button là ô (36 × 36px), vẫn chịu min-height mobile (44px).

Hover thông thường đổi sang nền `raised`; quiet đổi chữ sang `text`; primary có nền hover riêng. Transition nền và màu chữ (.14s ease). Focus-visible có outline (2px) màu `accent`, offset (3px). Disabled giảm opacity (.45), cursor not-allowed và hover nền transparent. Không có hiệu ứng active riêng trong nguồn.

### Inputs / Fields

Tên notebook là input nền trong suốt, viền xuất hiện khi hover; URL dùng nền `canvas` và viền `line`. Select nền trong suốt, hover dùng `raised`; select thêm cell và tốc độ có viền. Textarea không có viền riêng, caret màu `accent`, placeholder `muted`; focus outline offset (5px). Luôn giữ label và tên truy cập của điều khiển.

### Cards / Containers

Cell dùng nền `surface`, viền `line`, không shadow. Cell được chọn đổi viền sang màu trạng thái riêng và gutter sang `accent`; không tô toàn bộ cell bằng màu nhấn. Header cell có đường chia dưới; vùng tài nguyên có đường chia bên trái, đổi thành phía trên ở mobile.

### Navigation / Toolbar

Không có sidebar hoặc điều hướng nhiều workspace. Header chứa nhận diện, tên notebook, trạng thái lưu và thao tác tệp; toolbar chứa chọn loại cell, thêm cell và menu tùy chọn. Đây là thanh thao tác, không biểu diễn kernel hay môi trường chạy mã.

### Options Menu

Menu `details/summary` neo phải, nền `raised`, bo theo `container`, padding (8px), min-width (235px). Các mục trải hết chiều rộng, bo (4px), padding (8px); hover có nền riêng. Mobile giới hạn chiều rộng theo viewport trừ (40px). Menu cell hỗ trợ Escape đóng và đưa focus về summary.

### Resource Workspace

Vùng rỗng dùng icon Lucide dạng SVG nét, tiêu đề (14px/500), mô tả (12px/1.7), nút viền. Kéo thả dùng nền `accent-bg` và outline dashed (2px), inset (5px). PDF, ảnh, văn bản và audio giữ cách hiển thị phù hợp từng loại; audio dùng điều khiển native của trình duyệt. Không dùng icon ký tự thay cho SVG.

### Status & Feedback

Trạng thái lưu dùng chữ và icon; lỗi dùng `danger` cùng thông điệp. Thông báo hoàn tác nằm giữa đáy viewport, nền `raised`, viền, không shadow. Thời gian và đếm từ dùng tabular-nums. `prefers-reduced-motion: reduce` tắt transition và đặt scroll-behavior auto.

## Do's and Don'ts

### Do:
- **Do** dùng token YAML cho màu, font và bán kính đã có; dùng trạng thái cục bộ đúng component.
- **Do** giữ focus-visible rõ, label truy cập và thông điệp trạng thái thật.
- **Do** giữ bài làm và tài liệu đọc được khi hai vùng xếp dọc ở viewport hẹp.
- **Do** giữ icon SVG nét và chữ thao tác mô tả đúng chức năng.

### Don't:
- **Don't** dùng palette IELTS nhiều màu còn sót trong Tailwind để tạo màu phân loại kỹ năng.
- **Don't** thêm nhãn kernel, trạng thái chạy mã hoặc khả năng chấm bài chưa tồn tại.
- **Don't** coi Inter đã được tải hoặc giao diện đã qua kiểm toán browser/WCAG.
- **Don't** biến màu trạng thái cục bộ hoặc giá trị chỉ dùng một lần thành primitive chung.

Không canonize: palette IELTS cũ trong `tailwind.config.js` vì giao diện hiện tại không dùng; `In [n]:` chỉ là dấu lượt xem còn giữ trong build, không phải quy ước thực thi cần mở rộng. Đây không phải xác nhận rằng mọi chi tiết craft trong build đã qua đánh giá trực quan.
