from ultralytics import YOLO

# Load model có sẵn
model = YOLO("yolov8n.pt")

# Train model
model.train(
    data="dataset/data.yaml",
    epochs=50,
    imgsz=640
)