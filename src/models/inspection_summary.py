from database import db


class InspectionSummary(db.Model):

    __tablename__ = "inspection_summary"

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

    expected_quantity = db.Column(db.Integer)

    detected_quantity = db.Column(db.Integer)

    result = db.Column(
        db.String(20)
    )

    inspection = db.relationship(
        "Inspection",
        back_populates="summaries"
    )

    detection_class = db.relationship("DetectionClass")