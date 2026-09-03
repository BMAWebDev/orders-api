from flask import Blueprint
from models.db import db
from sqlalchemy import select
from models.users_models import User

users_bp = Blueprint("users", __name__, url_prefix="/users")


@users_bp.get("")
def get_users():
    page_size = 5
    page = 10

    users = (
        db.session.execute(select(User).limit(page_size).offset((page - 1) * page_size))
        .scalars()
        .all()
    )

    return [user.to_dict() for user in users], 200
