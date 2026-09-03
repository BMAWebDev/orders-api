from flask import Blueprint

products_bp = Blueprint("products", __name__, url_prefix="/products")


@products_bp.get("")
def get_products():
    return [], 200
