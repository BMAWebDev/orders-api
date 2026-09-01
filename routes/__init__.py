from .orders_routes import orders_bp
from flask import Flask


def register_routes(app: Flask):
    app.register_blueprint(orders_bp)
