from flask import Blueprint, jsonify, request
from src.main.http_types.http_request import HttpRequest

delivery_route_bp = Blueprint("delivery_routes", __name__)


@delivery_route_bp.route("/delivery/order", methods=["POST"])
def registry_order():
    http_request = HttpRequest(body=request.json)
    print(request.json)
    return jsonify({"hello": "world"}), 200
