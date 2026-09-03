from pydantic import ValidationError
from constants.validators import MIN_PASSWORD_LENGTH


def get_base_response(message: str = "", status: int = 200, **additional_data):
    """
    Base response structure for each request
    """

    default_message = (
        "Could not complete request"
        if status >= 400
        else "Request finished successfully"
    )

    return {
        "message": message or default_message,
        **additional_data,
    }, status


def get_payload_missing_fields_error(error: ValidationError):
    """
    Render a friendly missing fields error 400 based on the payload given in the request
    """

    return get_base_response(
        f"Missing fields: {', '.join([str(err.get('loc')[0]) for err in error.errors()])}.",
        400,
    )


def get_invalid_email_error():
    return get_base_response("Your email is invalid", 400)


def get_min_password_length_error():
    return get_base_response(
        f"Please enter a password with at least {MIN_PASSWORD_LENGTH} characters",
        400,
    )
