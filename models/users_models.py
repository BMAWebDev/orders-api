from .db import db, NamelessBase
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column


class User(NamelessBase, db.Model):
    __tablename__ = "users"

    username: Mapped[str] = mapped_column(String(255), nullable=False)
    email: Mapped[str] = mapped_column(String(255), nullable=False)
    first_name: Mapped[str] = mapped_column(String(255))
    last_name: Mapped[str] = mapped_column(String(255))
    password_hash: Mapped[str] = mapped_column(String(255))

    def __init__(self, username: str, email: str):
        self.username = username
        self.email = email

    def to_dict(self):
        return {**super().to_dict(), "username": self.username}
