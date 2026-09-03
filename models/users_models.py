from .db import db, NamelessBase
from pydantic import BaseModel
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column


class User(NamelessBase, db.Model):
    __tablename__ = "users"

    username: Mapped[str] = mapped_column(String(255), nullable=False)
    email: Mapped[str] = mapped_column(String(255), nullable=False)
    first_name: Mapped[str] = mapped_column(String(255))
    last_name: Mapped[str] = mapped_column(String(255))
    password_hash: Mapped[str] = mapped_column(String(255), nullable=False)

    def __init__(self, username: str, email: str, password_hash: str):
        self.username = username
        self.email = email
        self.password_hash = password_hash

    def to_dict(self):
        return {**super().to_dict(), "username": self.username}


class RegisterUserPayload(BaseModel):
    username: str
    email: str
    password: str


class LoginUserPayload(BaseModel):
    username: str
    password: str
