import os


class Config:
    # Database URL
    SQLALCHEMY_DATABASE_URI = os.getenv("DB_URL")

    def __init__(self) -> None:
        pass
