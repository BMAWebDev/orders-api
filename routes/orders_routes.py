from flask import Blueprint
from sqlalchemy import select

from models.db import db
from models.orders_models import Order

orders_bp = Blueprint("orders", __name__, url_prefix="/orders")


@orders_bp.get("")
def get_orders():
    items = db.session.execute(select(Order)).scalars()

    return [item.to_dict() for item in items]
