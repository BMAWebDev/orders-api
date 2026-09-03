from .db import db, NamelessBase
from typing import TYPE_CHECKING
from pydantic import BaseModel
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from .orders import Order


class User(NamelessBase, db.Model):
    __tablename__ = "users"

    username: Mapped[str] = mapped_column(String(255), nullable=False)
    email: Mapped[str] = mapped_column(String(255), nullable=False)
    first_name: Mapped[str | None] = mapped_column(String(255), nullable=True)
    last_name: Mapped[str | None] = mapped_column(String(255), nullable=True)
    password_hash: Mapped[str] = mapped_column(String(255), nullable=False)

    order: Mapped["Order"] = relationship(back_populates="user")

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
