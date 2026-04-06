from flask import Blueprint, jsonify
from db import get_engine
from sqlalchemy import text
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

@image_bp.route("/test-db", methods=["GET"])
def test_db():
    try:
        engine = get_engine()

        with engine.connect() as conn:
            result = conn.execute(text("SELECT 1"))

            return jsonify({
                "status": "success",
                "result": [row[0] for row in result]
            })
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500