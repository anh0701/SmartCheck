from database import db


class InspectionStage(db.Model):

    __tablename__ = "inspection_stage"

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