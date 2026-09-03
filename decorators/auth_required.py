from flask import current_app, request
from jwt import decode, ExpiredSignatureError
from functools import wraps

from utils import responses


def auth_required(func):
    """
    Decorator used to require JWT Authentication Token
    """

    @wraps(func)
    def handle_auth_required(*args, **kwargs):
        try:
            if not request.authorization or not request.authorization.token:
                return responses.get_base_response(
                    "Sorry, but you are not allowed to make this request", 401
                )

            decode(
                request.authorization.token,
                current_app.config.get("SECRET_KEY"),
                algorithms=["HS256"],
            )

            return func(*args, **kwargs)

        except ExpiredSignatureError as e:
            print("error")
            return e

    return handle_auth_required
