from models.inspection_stage import InspectionStage


class StageRepository:

    @staticmethod
    def find_by_code(code):

        return InspectionStage.query.filter_by(
            code=code
        ).first()