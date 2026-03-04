# CONTEXT TÓM TẮT DỰ ÁN: DỊCH THUẬT CỔ PHONG AI (V5)

## 📝 VAI TRÒ VÀ CÁCH SỬ DỤNG CÁC FILE PROMPT/GUIDE

Hệ thống dịch thuật được thiết kế để xử lý văn bản từ thô (Raw Chinese) sang bản dịch văn học hoàn chỉnh (HTML) thông qua 3 giai đoạn chặt chẽ.

### 📂 1. DANH SÁCH FILE & VAI TRÒ
*   **[preprocess_glossary.py](file:///d:/Duc/script/xtruyen-crawling/output/69shuba-84221/instruction/preprocess_glossary.py):** Script Python thực thi. Dùng để làm sạch metadata và thay thế thuật ngữ theo thuật toán **Longest Match First**.
*   **[master_glossary.csv](file:///d:/Duc/script/xtruyen-crawling/output/69shuba-84221/instruction/master_glossary.csv):** Cơ sở dữ liệu thuật ngữ (Tên riêng, địa danh, chức vụ).
*   **[translation_orchestrator.md](file:///d:/Duc/script/xtruyen-crawling/output/69shuba-84221/instruction/translation_orchestrator.md):** "Bản đồ" điều phối luồng công việc và template câu lệnh.
*   **[ai_translation_prompt.md](file:///d:/Duc/script/xtruyen-crawling/output/69shuba-84221/instruction/ai_translation_prompt.md):** Prompt hệ thống cho **Scholar Agent (Dịch thuật)**. Quy định IQ nhân vật, xưng hô, đơn vị cổ phong, và luật cấm tóm tắt.
*   **[ai_reviewer_prompt.md](file:///d:/Duc/script/xtruyen-crawling/output/69shuba-84221/instruction/ai_reviewer_prompt.md):** Prompt hệ thống cho **Editor Agent (Review)**. Chứa danh sách "Red Flags" lỗi xưng hô và thuật ngữ hiện đại.
*   **[quanhe.txt](file:///d:/Duc/script/xtruyen-crawling/output/69shuba-84221/instruction/quanhe.txt):** Context về mối quan hệ nhân vật để tra cứu xưng hô Hán Việt.

### ⚙️ 2. QUY TRÌNH THỰC THI (WORKFLOW)

#### Bước 1: Tiền xử lý (Pre-processing)
*   Chạy script Python để làm sạch rác metadata và replace glossary.
*   **Mục tiêu:** Tạo ra file "Mixed-Source" sạch sẽ cho AI.

#### Bước 2: Dịch thuật (Scholar - Agent 2)
*   Dựa trên `ai_translation_prompt.md` và `quanhe.txt`.
*   **Quy tắc "Sắt" (Mandatory):**
    *   **STRICT FIDELITY:** Dịch đủ 100% số câu, tuyệt đối không tóm tắt nội dung.
    *   **Xưng hô Peer-to-Peer:** Người lạ đồng trang lứa dùng *Ta/Muội/Huynh*. Cấm dùng *Chàng/Nàng*.
    *   **Xưng hô Hierarchy:** Dùng *Phụ thân/Mẫu thân/Tổ phụ* trong đối thoại và thoại nội tâm.
    *   **Đơn vị cổ phong:** Tự động đổi Km -> Lý; Giờ -> Khắc/Canh; Tiền -> Bạc/Ngân tử.

#### Bước 3: Rà soát (Editor - Agent 3)
*   Dựa trên `ai_reviewer_prompt.md`.
*   Kiểm tra lỗi tiếng Trung sót lại và các "Red Flags" xưng hô hiện đại.

### ⚠️ LƯU Ý CHO PHIÊN LÀM VIỆC TIẾP THEO
*   Nhân vật Hoa Trường Hy phải thể hiện rõ chất giọng logic của một PhD y khoa (PhD Voice).
*   Luôn phân biệt sắc thái giữa **Dẫn chuyện** (thân mật: Cha, Mẹ) và **Đối thoại/Thoại nội tâm** (trang trọng: Phụ thân, Mẫu thân).
*   Đảm bảo bản dịch có cấu trúc HTML chuẩn (`<h1>`, `<p>`).
