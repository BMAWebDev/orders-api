from flask import Blueprint

from models.db import db
from models.products import Product
from utils import responses

products_bp = Blueprint("products", __name__, url_prefix="/products")


@products_bp.get("")
def get_products():
    return [], 200


@products_bp.post("/add")
def add_product():
    product = Product(name="Laptop", price=124.99, quantity=100)

    db.session.add(product)
    db.session.commit()

    return responses.get_base_response("Product added successfully")
