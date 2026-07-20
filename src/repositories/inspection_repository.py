from database import db

from models.inspection_standard import InspectionStandard


class InspectionRepository:

    @staticmethod
    def get_standards(product_id, stage_id):

        return (
            InspectionStandard.query
            .filter_by(
                product_id=product_id,
                stage_id=stage_id
            )
            .all()
        )


    @staticmethod
    def add(entity):

        db.session.add(entity)


    @staticmethod
    def add_all(entities):

        db.session.add_all(entities)


    @staticmethod
    def commit():

        db.session.commit()


    @staticmethod
    def rollback():

        db.session.rollback()