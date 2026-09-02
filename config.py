import os


class Config:
    # Database URL
    SQLALCHEMY_DATABASE_URI = os.getenv("DB_URL")

    # Disable CSRF
    WTF_CSRF_ENABLED = False

    def __init__(self) -> None:
        pass
