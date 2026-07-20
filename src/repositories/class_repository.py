from models.detection_class import DetectionClass


class DetectionClassRepository:

    @staticmethod
    def find_by_name(name):

        return DetectionClass.query.filter_by(
            name=name
        ).first()


    @staticmethod
    def find_by_id(class_id):

        return DetectionClass.query.get(class_id)