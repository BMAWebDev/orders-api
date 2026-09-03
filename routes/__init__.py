from flask import Flask

from .orders import orders_bp
from .users import users_bp
from .products import products_bp


def register_routes(app: Flask):
    app.register_blueprint(orders_bp)
    app.register_blueprint(users_bp)
    app.register_blueprint(products_bp)
