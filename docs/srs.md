# SmartCheck

Pre-process and Post-process Quality Inspection

## Bài toán

### 1. Kiểm tra linh kiện đầu vào

- có đủ linh kiện không
- có đúng loại không (ví dụ nhầm ốc, nhầm IC,...)
- có lỗi ngoại quan (vỡ, xước,...)

### 2. Kiểm tra sản phầm sau lắp ráp

- lắp có đúng vị trí chưa
- có thiếu linh kiện không
- có lỗi sai lệch (lệch vị trí, hở,...)

### 3. Vấn đề

- Nhận diện qua camera:

    - ánh sáng thay đổi
    - linh kiện hơi xoay
    - có nhiều loại sản phẩm

- Setup phần cứng:

    - camera Industrial camera (Basler, Hikvision)
    - ánh sáng: đèn led cố định, tránh bóng, phản xạ
    - góc chụp: cố định, không rung

### 4. Cấu trúc hệ thống

- 1. Camera chụp frame
- 2. Backend xử lý: Python (OpenCV, YOLO)
- 3. Trả kết quả: OK/NG
- 4. Hiển thị: webapp/desktop app

## Mục tiêu hiện tại

- import ảnh → nhận diện → hiển thị kết quả
