# Task

- Xây dựng bộ dataset mẫu: 200-500 ảnh cho mỗi loại lỗi (cong, vênh, thiếu chi tiết, sai màu).

- Thực hiện gán nhãn (Annotation): Sử dụng công cụ như LabelImg hoặc CVAT để khoanh vùng chính xác vị trí lỗi.

- Viết script Augmentation: Tự động nhân bản ảnh bằng cách xoay, lật, thay đổi độ tương phản để làm giàu dữ liệu.

- Huấn luyện mô hình phát hiện linh kiện đầu vào (Input Detection).

    - Phân loại - Classification: Huấn luyện mô hình nhận diện linh kiện A, B, C. Nếu công nhân lấy nhầm linh kiện B cho bước lắp ráp A, hệ thống báo lỗi ngay.
    - Phát hiện lỗi ngoại quan - Defect Detection: Huấn luyện AI tìm các điểm bất thường trên linh kiện đơn lẻ:

        - Lỗi trầy xước, sứt mẻ.

        - Lỗi chân cắm bị cong (đối với linh kiện điện tử).

        - Lỗi sai kích thước (ví dụ ốc vít 5mm nhầm thành 4mm).
    - Viết hàm tự động nhận diện vùng chứa linh kiện trong ảnh lớn và cắt (crop) lại để phóng to các chi tiết nhỏ, giúp model AI soi lỗi tốt hơn.
    - Trạng thái sẵn sàng: Xác định linh kiện có nằm đúng chiều để gắp/lắp hay không (định hướng xoay).

- Huấn luyện mô hình so khớp sản phẩm hoàn thiện (Assembly Verification) - so sánh với mẫu chuẩn.

    - Kiểm tra sự hiện diện - Presence Check: AI quét sản phẩm sau khi lắp để đếm số lượng linh kiện. (Ví dụ: Đã đủ 4 con vít chưa? Đã có miếng đệm chưa?)
    - Kiểm tra vị trí & Khớp nối - Alignment Check: Linh kiện có bị lắp lệch (mép không khít) không? Linh kiện có bị lắp ngược chiều không?
    - So sánh mẫu chuẩn - Golden Template Matching: Viết thuật toán trừ ảnh (Image Subtraction) hoặc dùng AI để so sánh ảnh vừa lắp xong với mẫu chuẩn. Bất kỳ điểm khác biệt nào (thừa/thiếu/lệch) sẽ bị khoanh vùng đỏ.
    - Xác nhận công đoạn: Chỉ khi AI báo "OK" cho bước lắp ráp này thì hệ thống mới cho phép chuyền chạy tiếp hoặc nhảy sang bước tiếp theo.

- Thiết kế Dashboard hiển thị: Luồng video trực tiếp/ảnh, khung xanh (OK)/khung đỏ (NG) đè lên linh kiện.

- Làm nút bấm "Reset" hoặc "Bỏ qua": Cho phép công nhân xác nhận lại nếu AI nhận diện nhầm.

- Trang thống kê: Hiển thị số lượng sản phẩm đạt/lỗi trong ca làm việc.

- Viết tài liệu hướng dẫn vận hành và xử lý khi hệ thống báo lỗi sai.
