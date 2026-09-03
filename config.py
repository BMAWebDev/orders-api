from os import getenv


class Config:
    # Database URL
    SQLALCHEMY_DATABASE_URI = getenv("DB_URL")

    # Disable CSRF
    WTF_CSRF_ENABLED = False

    # JWT Secret Key
    SECRET_KEY = getenv("JWT_ACCESS_TOKEN_SECRET")

    def __init__(self) -> None:
        pass
