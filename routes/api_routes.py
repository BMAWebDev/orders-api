from flask import Blueprint, request
from sqlalchemy import select, or_
from pydantic import ValidationError
from bcrypt import hashpw, gensalt, checkpw

from models.db import db
from models.users_models import RegisterUserPayload, User, LoginUserPayload

from utils import responses

from constants.validators import EMAIL_REGEX, MIN_PASSWORD_LENGTH, MIN_USERNAME_LENGTH

bp = Blueprint("api", __name__)


@bp.post("/register")
def register_user():
    try:
        payload = RegisterUserPayload.model_validate(request.get_json())
    except ValidationError as e:
        return responses.get_payload_missing_fields_error(e)

    if not EMAIL_REGEX.match(payload.email):
        return responses.get_invalid_email_error()

    if len(payload.password) < MIN_PASSWORD_LENGTH:
        return responses.get_min_password_length_error()

    if len(payload.username) < MIN_USERNAME_LENGTH:
        return responses.get_base_response(
            f"Please enter a username with at least {MIN_USERNAME_LENGTH} characters",
            400,
        )

    existing_user = db.session.execute(
        select(User).where(
            or_(User.username == payload.username, User.email == payload.email)
        )
    ).scalar_one_or_none()

    if existing_user:
        return responses.get_base_response("User already exists", 400)

    password_hash = hashpw(payload.password.encode(), gensalt()).decode()

    new_user = User(
        username=payload.username, email=payload.email, password_hash=password_hash
    )

    db.session.add(new_user)
    db.session.commit()

    return responses.get_base_response(
        "Account created",
    )


@bp.post("/login")
def login_user():
    try:
        payload = LoginUserPayload.model_validate(request.get_json())
    except ValidationError as e:
        return responses.get_payload_missing_fields_error(e)

    user = db.session.execute(
        select(User).where(User.username == payload.username)
    ).scalar_one_or_none()

    if not user:
        return responses.get_base_response("User not found", 404)

    if not checkpw(payload.password.encode(), user.password_hash.encode()):
        return responses.get_base_response("Invalid password", 400)

    return responses.get_base_response("Successfully logged in")
