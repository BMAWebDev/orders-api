from flask import current_app, request
from jwt import decode, ExpiredSignatureError, InvalidSignatureError
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
                    "No authentication token was present on request", 401
                )

            decode(
                request.authorization.token,
                current_app.config.get("SECRET_KEY"),
                algorithms=["HS256"],
            )

            return func(*args, **kwargs)

        except InvalidSignatureError:
            return responses.get_base_response("Invalid token", 401)

        except ExpiredSignatureError:
            return responses.get_base_response("Session expired", 401)

    return handle_auth_required
