from database import db


class InspectionStandard(db.Model):

    __tablename__ = "inspection_standard"

    id = db.Column(db.Integer, primary_key=True)

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

    class_id = db.Column(
        db.Integer,
        db.ForeignKey("detection_class.id"),
        nullable=False
    )

    required_quantity = db.Column(
        db.Integer,
        nullable=False
    )

    product = db.relationship(
        "Product",
        back_populates="standards"
    )

    stage = db.relationship("InspectionStage")

    detection_class = db.relationship("DetectionClass")