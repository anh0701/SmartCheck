from flask import Blueprint, jsonify
from services.image_service import augment_dataset

image_bp = Blueprint("image", __name__)


@image_bp.route("/augment-dataset", methods=["POST"])
def augment_dataset_api():
    try:
        results = augment_dataset(num_aug=3)
        return jsonify({
            "message": "Done augmentation",
            "total": len(results)
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500