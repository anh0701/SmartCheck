from database import db


class Product(db.Model):

    __tablename__ = "product"

    id = db.Column(db.Integer, primary_key=True)

    code = db.Column(
        db.String(30),
        unique=True,
        nullable=False
    )

    name = db.Column(
        db.String(100),
        nullable=False
    )

    description = db.Column(db.Text)

    created_at = db.Column(
        db.DateTime,
        server_default=db.func.now()
    )

    standards = db.relationship(
        "InspectionStandard",
        back_populates="product"
    )

    inspections = db.relationship(
        "Inspection",
        back_populates="product"
    )