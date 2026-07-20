from ultralytics import YOLO

import cv2
import uuid
import os

from collections import Counter


class Detector:

    def __init__(self, model_path):

        self.model = YOLO(model_path)


    def detect(self, image):

        results = self.model(image, conf=0.5)

        detections = []

        counter = Counter()

        plotted = results[0].plot()

        filename = f"{uuid.uuid4().hex}.jpg"

        save_path = os.path.join(
            "results",
            filename
        )

        cv2.imwrite(save_path, plotted)

        for box in results[0].boxes:

            cls = int(box.cls[0])

            name = self.model.names[cls]

            counter[name] += 1

            detections.append({

                "class_name": name,

                "confidence": float(box.conf[0]),

                "bbox": {

                    "x1": float(box.xyxy[0][0]),

                    "y1": float(box.xyxy[0][1]),

                    "x2": float(box.xyxy[0][2]),

                    "y2": float(box.xyxy[0][3])

                }

            })

        return {

            "detections": detections,

            "counter": counter,

            "result_image": filename

        }