from collections import Counter
from time import perf_counter

from database import db

from models.inspection import Inspection
from models.detection_result import DetectionResult
from models.inspection_summary import InspectionSummary

from repositories.inspection_repository import InspectionRepository
from repositories.class_repository import DetectionClassRepository

from services.detector import Detector


class InspectionService:

    def __init__(self):

        self.detector = Detector("models/best.pt")

    def inspect(
        self,
        image,
        product,
        stage
    ):

        start = perf_counter()

        try:

            detect_result = self.detector.detect(image)

            detections = detect_result["detections"]

            result_image = detect_result["result_image"]

            counter = Counter()

            for detection in detections:

                counter[detection["class_name"]] += 1

            standards = InspectionRepository.get_standards(
                product.id,
                stage.id
            )

            inspection = Inspection(

                product_id=product.id,

                stage_id=stage.id,

                image_path=result_image

            )

            db.session.add(inspection)

            # flush để lấy inspection.id
            db.session.flush()

            detection_entities = []

            for detection in detections:

                cls = DetectionClassRepository.find_by_name(
                    detection["class_name"]
                )

                bbox = detection["bbox"]

                detection_entities.append(

                    DetectionResult(

                        inspection_id=inspection.id,

                        class_id=cls.id,

                        confidence=detection["confidence"],

                        x_min=int(bbox["x1"]),

                        y_min=int(bbox["y1"]),

                        x_max=int(bbox["x2"]),

                        y_max=int(bbox["y2"])

                    )

                )

            db.session.add_all(detection_entities)

            overall = True

            response_summary = []

            summary_entities = []

            for standard in standards:

                class_name = standard.detection_class.name

                expected = standard.required_quantity

                actual = counter.get(
                    class_name,
                    0
                )

                status = "PASS"

                if actual != expected:

                    status = "FAIL"

                    overall = False

                summary_entities.append(

                    InspectionSummary(

                        inspection_id=inspection.id,

                        class_id=standard.class_id,

                        expected_quantity=expected,

                        detected_quantity=actual,

                        result=status

                    )

                )

                response_summary.append({

                    "class": class_name,

                    "expected": expected,

                    "detected": actual,

                    "status": status

                })

            db.session.add_all(summary_entities)

            db.session.commit()

            elapsed = round(
                (perf_counter() - start) * 1000,
                2
            )

            return {

                "success": True,

                "inspection_status":
                    "PASS"
                    if overall
                    else "FAIL",

                "processing_time_ms": elapsed,

                "total_detected": len(detections),

                "summary": response_summary,

                "detections": detections,

                "result_image": result_image

            }

        except Exception as ex:

            db.session.rollback()

            raise ex