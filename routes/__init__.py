from .orders import orders_bp
from .users import users_bp
from flask import Flask


def register_routes(app: Flask):
    app.register_blueprint(orders_bp)
    app.register_blueprint(users_bp)
