from database import db


class DetectionClass(db.Model):

    __tablename__ = "detection_class"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(
        db.String(50),
        unique=True,
        nullable=False
    )

    description = db.Column(db.Text)