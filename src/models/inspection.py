from database import db


class Inspection(db.Model):

    __tablename__ = "inspection"

    id = db.Column(
        db.BigInteger,
        primary_key=True
    )

    product_id = db.Column(
        db.Integer,
        db.ForeignKey("product.id"),
        nullable=False
    )

    stage_id = db.Column(
        db.Integer,
        db.ForeignKey("inspection_stage.id"),
        nullable=False
    )

    image_path = db.Column(db.Text)

    processing_time_ms = db.Column(db.Integer)

    inspected_at = db.Column(
        db.DateTime,
        server_default=db.func.now()
    )

    product = db.relationship(
        "Product",
        back_populates="inspections"
    )

    stage = db.relationship("InspectionStage")

    detections = db.relationship(
        "DetectionResult",
        cascade="all, delete-orphan",
        back_populates="inspection"
    )

    summaries = db.relationship(
        "InspectionSummary",
        cascade="all, delete-orphan",
        back_populates="inspection"
    )