from .orders_routes import orders_bp
from .users_routes import users_bp
from flask import Flask


def register_routes(app: Flask):
    app.register_blueprint(orders_bp)
    app.register_blueprint(users_bp)
