from flask import Blueprint

orders_bp = Blueprint("orders", __name__, url_prefix="/orders")


@orders_bp.get("")
def get_orders():
    return [{"name": "hello"}]
