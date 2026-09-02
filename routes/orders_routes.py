from flask import Blueprint, request
from sqlalchemy import select
from pydantic import ValidationError

from models.db import db
from models.orders_models import Order, AddOrderPayload

orders_bp = Blueprint("orders", __name__, url_prefix="/orders")


@orders_bp.get("")
def get_orders():
    items = db.session.execute(select(Order)).scalars()

    return [item.to_dict() for item in items]


@orders_bp.post("/add")
def add_order():
    print("add")
    try:
        payload = AddOrderPayload.model_validate(request.get_json())
    except ValidationError as e:
        return (
            f"Missing fields: {', '.join([str(err.get('loc')[0]) for err in e.errors()])}.",
            400,
        )

    new_order = Order(name=payload.name)

    db.session.add(new_order)

    db.session.commit()

    print(new_order.to_dict())

    return {"message": "Order submitted successfully"}
