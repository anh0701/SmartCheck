# SmartCheck

Pre-process and Post-process Quality Inspection

## I. Bài toán

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

## II. Mục tiêu hiện tại

- import ảnh → nhận diện → hiển thị kết quả

## III. System Design

```sh
Camera
      │
      ▼
YOLO Detection
      │
      ▼
Có đủ linh kiện?

NO
│
└──────────────► FAIL

YES
│
▼
Defect Detection
│
├── Scratch
├── Crack
├── Missing Screw
├── Burn
└── Bent Pin
│
▼
PASS / FAIL
```

> Hiện tại đang làm ở mức đủ số lượng hay không? Bước detect lỗi linh kiện phải train lại model, thêm ảnh lỗi và vẽ label.

### 1. Summary

```sh
                         +----------------+
                         |     Camera     |
                         +--------+-------+
                                  |
                                  v
                         +----------------+
                         |  Flask API     |
                         +--------+-------+
                                  |
                                  v
                         +----------------+
                         | Image Validate |
                         +--------+-------+
                                  |
                                  v
                         +----------------+
                         | YOLO Inference |
                         +--------+-------+
                                  |
                                  v
                       +----------------------+
                       | Detection Result     |
                       | RAM = 2              |
                       | SSD = 1              |
                       | Battery = 0          |
                       +----------+-----------+
                                  |
                                  v
                    +-----------------------------+
                    | Read Inspection Standard    |
                    | PostgreSQL                  |
                    +-------------+---------------+
                                  |
                                  v
                    +-----------------------------+
                    | Compare Expected vs Actual  |
                    +-------------+---------------+
                                  |
                    PASS          |          FAIL
                        \         |        /
                         \        |       /
                          v       v      v
                     +---------------------------+
                     | Save Inspection Result    |
                     +-------------+-------------+
                                   |
                                   v
                           JSON Response
```

### 2. PRE-PROCESS

```sh
                 PCB
                 CPU
                 RAM x2
                 SSD
                 Battery
                 Fan

                     ↓

               Camera Capture

                     ↓

                YOLO Detect

                     ↓

        +-------------------------+
        | PCB      = 1            |
        | CPU      = 1            |
        | RAM      = 2            |
        | SSD      = 1            |
        | Battery  = 0            |
        | Fan      = 1            |
        +-------------------------+

                     ↓

            Đọc Inspection Standard

                     ↓

                Required

                PCB = 1
                CPU = 1
                RAM = 2
                SSD = 1
                Battery = 1
                Fan = 1

                     ↓

                Compare

                Battery

                Expected = 1

                Actual = 0

                     ↓

                    FAIL

                     ↓

            Save inspection_result
            Save detection_result
            Save inspection_summary

                     ↓

                Response

                {
                status : FAIL,
                reason : Missing Battery
                }
```

### 3. POST-PROCESS

```sh
             Laptop Finished

                     ↓

                Camera Capture

                     ↓

                 YOLO Detect

                     ↓

                Laptop = 1

                Monitor = 1

                Keyboard = 1

                Mouse = 1

                     ↓

        Read Inspection Standard

                     ↓

                Required

                Laptop = 1

                Monitor = 1

                Keyboard = 1

                Mouse = 1

                     ↓

                Compare

                     ↓

                PASS

                     ↓

                Save DB

                     ↓

                {
                status : PASS
                }
```
