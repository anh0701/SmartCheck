from database import db


class DetectionResult(db.Model):

    __tablename__ = "detection_result"

    id = db.Column(
        db.BigInteger,
        primary_key=True
    )

    inspection_id = db.Column(
        db.BigInteger,
        db.ForeignKey("inspection.id")
    )

    class_id = db.Column(
        db.Integer,
        db.ForeignKey("detection_class.id")
    )

    confidence = db.Column(db.Float)

    x_min = db.Column(db.Integer)
    y_min = db.Column(db.Integer)
    x_max = db.Column(db.Integer)
    y_max = db.Column(db.Integer)

    inspection = db.relationship(
        "Inspection",
        back_populates="detections"
    )

    detection_class = db.relationship("DetectionClass")