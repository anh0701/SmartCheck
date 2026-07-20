from flask import Blueprint, jsonify, request, send_from_directory
from ultralytics import YOLO
import cv2
import numpy as np
import os
import uuid


detect_bp = Blueprint("image", __name__)

model = YOLO("models/best.pt")

UPLOAD_FOLDER = "uploads"
RESULT_FOLDER = "results"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(RESULT_FOLDER, exist_ok=True)


@detect_bp.route("/detect", methods=["POST"])
def detect():

    if "image" not in request.files:
        return jsonify({
            "success": False,
            "message": "No image uploaded."
        }), 400

    file = request.files["image"]

    if file.filename == "":
        return jsonify({
            "success": False,
            "message": "Empty filename."
        }), 400

    image_bytes = file.read()

    image = cv2.imdecode(
        np.frombuffer(image_bytes, np.uint8),
        cv2.IMREAD_COLOR
    )

    # Predict
    results = model(image, conf=0.5)

    detections = []

    for box in results[0].boxes:

        cls = int(box.cls[0])
        conf = float(box.conf[0])

        x1, y1, x2, y2 = box.xyxy[0].tolist()

        detections.append({
            "class_id": cls,
            "class_name": model.names[cls],
            "confidence": round(conf, 3),
            "bbox": {
                "x1": round(x1, 2),
                "y1": round(y1, 2),
                "x2": round(x2, 2),
                "y2": round(y2, 2)
            }
        })

    # Vẽ bounding box
    plotted = results[0].plot()

    filename = f"{uuid.uuid4().hex}.jpg"
    save_path = os.path.join(RESULT_FOLDER, filename)

    cv2.imwrite(save_path, plotted)

    return jsonify({
        "success": True,
        "total": len(detections),
        "detections": detections,
        "result_image": f"/results/{filename}"
    })


@detect_bp.route("/results/<filename>")
def get_image(filename):
    return send_from_directory(RESULT_FOLDER, filename)
