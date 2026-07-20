from flask import Blueprint, request, jsonify
import cv2
import numpy as np

from repositories.product_repository import ProductRepository
from repositories.stage_repository import StageRepository
from services.inspection_service import InspectionService

detect_bp = Blueprint("inspection", __name__)

inspection_service = InspectionService()


@detect_bp.route("/inspection", methods=["POST"])
def inspect():

    if "image" not in request.files:
        return jsonify({
            "success": False,
            "message": "Image is required."
        }), 400

    product_code = request.form.get("product_code")
    stage_code = request.form.get("stage")

    if not product_code:
        return jsonify({
            "success": False,
            "message": "product_code is required."
        }), 400

    if not stage_code:
        return jsonify({
            "success": False,
            "message": "stage is required."
        }), 400

    file = request.files["image"]

    image = cv2.imdecode(
        np.frombuffer(file.read(), np.uint8),
        cv2.IMREAD_COLOR
    )

    if image is None:
        return jsonify({
            "success": False,
            "message": "Invalid image."
        }), 400

    product = ProductRepository.find_by_code(product_code)

    if product is None:
        return jsonify({
            "success": False,
            "message": "Product not found."
        }), 404

    stage = StageRepository.find_by_code(stage_code)

    if stage is None:
        return jsonify({
            "success": False,
            "message": "Inspection stage not found."
        }), 404

    try:

        result = inspection_service.inspect(
            image=image,
            product=product,
            stage=stage
        )

        return jsonify(result), 200

    except Exception as ex:

        return jsonify({
            "success": False,
            "message": str(ex)
        }), 500