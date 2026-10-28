# 📘 HƯỚNG DẪN ĐẶC TẢ SCHEMA DÀNH CHO USER CLIENT &amp; AI PROMPTING

## IELTS Notebook — Interactive Mini-IELTS Structured JSON Schema

Tài liệu này cung cấp bản hướng dẫn chi tiết dành cho **Người dùng (Client)**, **Lập trình viên tích hợp**, và **Người dùng tương tác với AI (ChatGPT, Claude, Gemini, DeepSeek)** để tạo ra các tệp `.json` bài tập IELTS chuẩn xác. Khi nạp (upload/paste) tệp JSON này vào hệ thống, ứng dụng sẽ tự động phân tích và dựng thành **Giao diện bài thi tương tác (Interactive Test UI)** tương ứng với từng dạng câu hỏi của cả 4 kỹ năng.

File JSON Schema chuẩn quốc tế độc lập nằm tại: [`ielts-exercise-schema.json`](file:///home/phuqy/Develop/IELTS/ielts-exercise-schema.json).

---

## 📑 MỤC LỤC

1. [Luồng hoạt động từ AI đến Ứng dụng Web](#1-luồng-hoạt-động-từ-ai-đến-ứng-dụng-web)
2. [Cấu trúc Schema Tổng quát (Master Schema)](#2-cấu-trúc-schema-tổng-quát-master-schema)
3. [Đặc tả chi tiết từng Kỹ năng &amp; Dạng câu hỏi](#3-đặc-tả-chi-tiết-từng-kỹ-năng--dạng-câu-hỏi)
   - [3.1 Kỹ năng Reading (Đọc hiểu)](#31-kỹ-năng-reading-đọc-hiểu)
   - [3.2 Kỹ năng Listening (Nghe hiểu)](#32-kỹ-năng-listening-nghe-hiểu)
   - [3.3 Kỹ năng Writing (Viết luận &amp; Báo cáo)](#33-kỹ-năng-writing-viết-luận--báo-cáo)
   - [3.4 Kỹ năng Speaking (Nói &amp; Phản xạ)](#34-kỹ-năng-speaking-nói--phản-xạ)
4. [Prompt Mẫu chuẩn để đưa vào Chat AI](#4-prompt-mẫu-chuẩn-để-đưa-vào-chat-ai)
5. [Hướng dẫn Import lên Giao diện Web](#5-hướng-dẫn-import-lên-giao-diện-web)

---

## 1. Luồng hoạt động từ AI đến Ứng dụng Web

```
+-------------------------------------------------------------+
| 1. Người dùng gửi bài đọc / chủ đề vào AI (ChatGPT, Claude) |
|    kèm theo IELTS Schema Prompt có sẵn                      |
+------------------------------+------------------------------+
                               |  AI trả về tệp .json chuẩn
                               v
+-------------------------------------------------------------+
| 2. Người dùng copy chuỗi JSON hoặc tải tệp .json về máy      |
+------------------------------+------------------------------+
                               |  Upload / Paste vào Cell Web
                               v
+-------------------------------------------------------------+
| 3. Hệ thống IELTS Notebook tự động nhận diện & chuyển đổi:  |
|    - Pane phải: Hiển thị bài đọc [A],[B] / audio player     |
|    - Pane trái: Dựng nút bấm TFNG, MCQ, ô điền từ, timer... |
|    - Nút "Check Answers": Tự chấm điểm, giải thích & tính   |
|      Band điểm IELTS tức thì.                               |
+-------------------------------------------------------------+
```

---

## 2. Cấu trúc Schema Tổng quát (Master Schema)

Mỗi bài tập là một đối tượng JSON đại diện cho 1 Cell (`IeltsExerciseData`):

```typescript
{
  "version": "1.0",                                   // Bắt buộc: luôn là "1.0"
  "skill": "reading" | "listening" | "writing" | "speaking", // Bắt buộc
  "title": string,                                    // Bắt buộc: Tiêu đề bài tập
  "topic"?: string,                                   // Tùy chọn: Chủ đề (e.g. "Environment", "Technology")
  "difficulty"?: string,                              // Tùy chọn: Band mục tiêu (e.g. "Band 6.5–7.5")
  "timeLimitMinutes"?: number,                        // Tùy chọn: Thời gian làm bài (phút)
  
  // TÀI LIỆU KÈM THEO (Hiển thị bên Pane phải)
  "material"?: {
    "type": "text" | "audio" | "image" | "pdf",       // Loại tài liệu
    "title"?: string,                                 // Tên tài liệu
    "content"?: string,                               // Nội dung bài đọc (chia đoạn [A], [B], [C]...)
    "audioUrl"?: string,                              // Link âm thanh (nếu là bài Listening)
    "audioTranscript"?: string,                       // Lời thoại bài nghe
    "imageUrl"?: string,                              // Link hình ảnh biểu đồ/bản đồ
    "imageDescription"?: string                       // Diễn giải số liệu biểu đồ
  },

  // DANH SÁCH NHÓM CÂU HỎI (Cho Reading & Listening)
  "questionGroups"?: [
    {
      "id": string,                                   // Mã nhóm (e.g. "g1", "g2")
      "type": IeltsQuestionType,                      // Dạng câu hỏi (chi tiết ở mục 3)
      "title"?: string,                               // Tiêu đề nhóm (e.g. "Questions 1–4")
      "instruction": string,                          // Yêu cầu đề bài
      "wordLimitRule"?: string,                       // Giới hạn từ (e.g. "NO MORE THAN TWO WORDS")
      "headingsList"?: [ { "id": "i", "heading": string } ], // Dành cho Matching Headings
      "featuresList"?: [ { "key": "A", "name": string } ],   // Dành cho Matching Features
      "endingsList"?: [ { "key": "A", "text": string } ],    // Dành cho Matching Endings
      "boxOptions"?: [ { "key": "A", "word": string } ],     // Dành cho Summary có kho từ vựng
      "questions": [
        {
          "questionNumber": number,                   // Số thứ tự câu hỏi (1, 2, 3...)
          "statement"?: string,                       // Câu phát biểu (TFNG, Matching)
          "question"?: string,                        // Câu hỏi (MCQ)
          "prefix"?: string,                          // Đoạn chữ trước ô điền từ
          "suffix"?: string,                          // Đoạn chữ sau ô điền từ
          "options"?: [ { "key": "A", "text": string } ], // Lựa chọn MCQ
          "answer": string | string[],                // Đáp án đúng để chấm điểm
          "acceptedAnswers"?: string[],               // Các cách viết khác được chấp nhận
          "explanation"?: string,                     // Giải thích vì sao đúng/sai
          "paragraphRef"?: string                     // Đoạn văn chứa đáp án (e.g. "Paragraph B")
        }
      ]
    }
  ],

  // BÀI THI WRITING (Nếu skill = "writing")
  "writingTask"?: {
    "taskType": "task1_academic" | "task1_general" | "task2",
    "academicVisualType"?: "bar_chart" | "line_graph" | "pie_chart" | "table" | "map_plan" | "process_diagram",
    "generalLetterType"?: "formal" | "semi_formal" | "informal",
    "prompt": string,
    "bulletPoints"?: string[],
    "keyDataPoints"?: string[],
    "minWords": 150 | 250,
    "sampleEssay"?: string,
    "sampleExaminerBand"?: string
  },

  // BÀI THI SPEAKING (Nếu skill = "speaking")
  "speakingTask"?: {
    "part": 1 | 2 | 3,
    "topic": string,
    "part1Questions"?: [ { "questionNumber": number, "question": string } ],
    "cueCard"?: {
      "title": string,
      "bulletPoints": string[],
      "roundingOffQuestion"?: string
    },
    "part3Questions"?: [ { "questionNumber": number, "question": string } ],
    "recommendedIdioms"?: [ { "phrase": string, "meaning": string, "example": string } ]
  },

  // SỔ TAY TỪ VỰNG HỌC THUẬT
  "vocabularyNotes"?: [
    {
      "word": string,
      "type"?: "noun" | "verb" | "adj" | "collocation",
      "phonetic"?: string,
      "definition": string,
      "example"?: string
    }
  ]
}
```

---

## 3. Đặc tả chi tiết từng Kỹ năng &amp; Dạng câu hỏi

### 3.1 Kỹ năng Reading (Đọc hiểu)

Khi `skill = "reading"`, các đoạn văn trong `material.content` nên được bắt đầu bằng chữ cái hoa trong ngoặc vuông: `[A] ...`, `[B] ...`, `[C] ...`.

#### Các dạng câu hỏi Reading được hỗ trợ:

1. **`true_false_not_given`** &amp; **`yes_no_not_given`**:
   - `statement`: Câu phát biểu cần kiểm chứng.
   - `answer`: Chuỗi `"TRUE"`, `"FALSE"`, hoặc `"NOT GIVEN"` (hoặc `"YES"`, `"NO"`).
   - *Giao diện tương ứng*: Hiển thị bộ 3 nút pill đổi màu khi chọn và chuyển xanh lá/đỏ khi kiểm tra đáp án.
2. **`multiple_choice`**:
   - `question`: Câu hỏi.
   - `options`: Mảng các lựa chọn `{ "key": "A", "text": "..." }`.
   - `answer`: `"A"` hoặc mảng `["A", "C"]` nếu là dạng chọn 2 đáp án (`isMultiSelect: true`).
   - *Giao diện tương ứng*: Danh sách Choice Cards bấm chọn trực tiếp.
3. **`sentence_completion` / `summary_completion`**:
   - `prefix`: Phần chữ đứng trước ô trống.
   - `suffix`: Phần chữ đứng sau ô trống.
   - `answer`: Từ cần điền (viết thường hoặc đúng chữ cái).
   - `acceptedAnswers`: Các biến thể được chấp nhận (e.g. số ít / số nhiều).
   - *Giao diện tương ứng*: Ô nhập chữ `[Q#: ________]` nằm liền mạch trong câu văn.
4. **`matching_headings`**:
   - `headingsList`: Danh sách các tiêu đề La Mã `{ "id": "i", "heading": "..." }`.
   - `paragraph`: Ký hiệu đoạn văn (e.g. `"A"`, `"B"`).
   - `answer`: Ký hiệu La Mã của tiêu đề tương ứng (e.g. `"iii"`).
   - *Giao diện tương ứng*: Khung tổng hợp các Heading và Dropdown lựa chọn theo từng đoạn.
5. **`matching_features` &amp; `matching_information`**:
   - `featuresList`: Danh sách thực thể (e.g. `{ "key": "A", "name": "Dr. Watson" }`).
   - *Giao diện tương ứng*: Dropdown ghép cặp nhãn cho từng phát biểu.

---

### 3.2 Kỹ năng Listening (Nghe hiểu)

Khi `skill = "listening"`, tệp audio được chỉ định qua `material.audioUrl` và nội dung lời thoại qua `material.audioTranscript`.

#### Các dạng câu hỏi Listening được hỗ trợ:

1. **`form_completion` / `note_completion` / `table_completion`**:
   - `wordLimitRule`: Giới hạn từ (e.g. `"NO MORE THAN TWO WORDS AND/OR A NUMBER"`).
   - `prompt`: Tên trường thông tin (e.g. `"1. Guest Surname: "`).
2. **`multiple_choice`**: Trắc nghiệm theo dòng sự kiện của đoạn hội thoại.
3. **`plan_map_diagram_labelling`**:
   - `labelLocation`: Mô tả vị trí cần xác định (e.g. `"Room next to the cafeteria"`).
   - `answer`: Chữ cái định danh trên bản đồ (e.g. `"B"`).

---

### 3.3 Kỹ năng Writing (Viết luận &amp; Báo cáo)

Khi `skill = "writing"`, trường `writingTask` sẽ được kích hoạt:

```json
"writingTask": {
  "taskType": "task1_academic",
  "academicVisualType": "bar_chart",
  "prompt": "The chart below shows the percentage of households with internet access in three European countries from 2010 to 2020...",
  "minWords": 150,
  "keyDataPoints": [
    "UK: increased from 70% in 2010 to 95% in 2020",
    "Germany: showed steady growth, peaking at 92%"
  ],
  "sampleEssay": "The bar chart illustrates the proportion of households with internet connectivity...",
  "sampleExaminerBand": "Band 8.5"
}
```

*Giao diện tương ứng*:

- Hiển thị thẻ đề bài với huy hiệu Task, số từ mục tiêu (150+ hoặc 250+ từ), các gợi ý phân tích dữ liệu quan trọng.
- Nút bấm xem **Bài luận mẫu Band 8.5+** ẩn/hiện tiện lợi.
- Bên trái là khung soạn thảo với **Bộ đếm từ trực tiếp (Live Word Counter)**.

---

### 3.4 Kỹ năng Speaking (Nói &amp; Phản xạ)

Khi `skill = "speaking"`, trường `speakingTask` sẽ được kích hoạt:

```json
"speakingTask": {
  "part": 2,
  "topic": "An Memorable Journey",
  "cueCard": {
    "title": "Describe an unforgettable journey you have taken",
    "bulletPoints": [
      "Where you went and who you went with",
      "What means of transport you used",
      "What you did during the trip",
      "And explain why this journey was so memorable"
    ],
    "roundingOffQuestion": "Do you still like traveling by that means of transport?"
  },
  "recommendedIdioms": [
    {
      "phrase": "off the beaten track",
      "meaning": "In or to places that are not visited by many people",
      "example": "We decided to explore a mountain village well off the beaten track."
    }
  ]
}
```

*Giao diện tương ứng*:

- Thẻ Cue Card hiển thị trang trọng theo đúng mẫu phòng thi thật.
- **Nút "Start 1-Min Prep"**: Bộ đếm ngược 60 giây để chuẩn bị dàn ý.
- **Nút "Start 2-Min Talk"**: Bộ đếm ngược 120 giây tích hợp cùng Voice Studio để thu âm bài nói.
- Ngân hàng **Thành ngữ ăn điểm (Idioms)** giúp người học vận dụng ngay vào bài nói.

---

## 4. Prompt Mẫu chuẩn để đưa vào Chat AI

Bạn chỉ cần sao chép toàn bộ khối lệnh dưới đây, dán vào **ChatGPT**, **Claude**, **Gemini** hoặc **DeepSeek** kèm nội dung bạn muốn:

```markdown
You are an expert Cambridge IELTS test designer.
Generate an authentic IELTS practice test strictly according to the JSON format below.
Return ONLY raw, valid JSON with NO surrounding conversational text.

### JSON STRUCTURE:
{
  "version": "1.0",
  "skill": "reading", // or "listening" | "writing" | "speaking"
  "title": "[Insert Title]",
  "difficulty": "Band 6.5–7.5",
  "timeLimitMinutes": 20,
  "material": {
    "type": "text",
    "title": "[Passage Title]",
    "content": "[A] Paragraph 1 text...\n\n[B] Paragraph 2 text..."
  },
  "questionGroups": [
    {
      "id": "g1",
      "type": "true_false_not_given",
      "title": "Questions 1–4: True / False / Not Given",
      "instruction": "Do the following statements agree with the information in the reading passage? Write TRUE, FALSE, or NOT GIVEN.",
      "questions": [
        {
          "questionNumber": 1,
          "statement": "Statement text...",
          "answer": "TRUE",
          "explanation": "Quote from paragraph A explaining why.",
          "paragraphRef": "Paragraph A"
        }
      ]
    }
  ],
  "vocabularyNotes": [
    {
      "word": "mitigate",
      "type": "verb",
      "definition": "To make something less severe",
      "example": "...mitigated these concerns."
    }
  ]
}

---
TEXT / TOPIC TO GENERATE FROM:
[Dán bài báo, văn bản hoặc chủ đề của bạn vào đây]
```

---

## 5. Hướng dẫn Import lên Giao diện Web

Hệ thống hỗ trợ 3 cách cực kỳ thuận tiện để đưa JSON vào cell:

### Cách 1: Sử dụng nút `AI JSON` (Khuyên dùng)

1. Trong Cell bất kỳ trên màn hình, nhìn lên góc trên bên phải của Pane bên trái (Response &amp; Notes), bấm nút **`AI JSON`**.
2. Tại popup mở ra:
   - Tab **"Paste or Upload JSON"**: Dán chuỗi JSON vừa copy từ AI vào ô hoặc bấm **"Upload .json File"**.
   - Bấm **"Apply to this Cell"**.
3. Hệ thống sẽ ngay lập tức:
   - Dựng bài đọc vào Pane bên phải.
   - Dựng các nút tương tác câu hỏi vào Pane bên trái.

### Cách 2: Tự động phát hiện khi Dán vào ô Ghi chú (Smart Paste)

1. Nhấp chuột vào khung soạn thảo của bất kỳ Cell nào.
2. Dán (`Ctrl + V`) chuỗi JSON bắt đầu bằng `{ "version": "1.0" ... }`.
3. Hệ thống sẽ xuất hiện một dải thông báo màu xanh:
 `✨ Valid AI IELTS JSON detected! [Render Interactive Test]`
4. Bấm vào nút **"Render Interactive Test"** để chuyển đổi ngay lập tức.

### Cách 3: Nạp tệp Notebook `.ilnb` từ thanh Header

- Bấm nút **Open** trên thanh tiêu đề ứng dụng để chọn các tệp `.ilnb` hoặc `.json` chứa nhiều cell bài tập cùng lúc.