from .db import db, Base
from pydantic import BaseModel
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column


class Order(Base, db.Model):
    __tablename__ = "orders"

    user_id: Mapped[int] = mapped_column(Integer, nullable=False)
    thumbnail_url: Mapped[str | None] = mapped_column(String)

    def __init__(self, name: str, thumbnail_url: str | None = None):
        super().__init__(name)
        self.thumbnail_url = thumbnail_url
        self.user_id = 1

    def to_dict(self):
        return {
            **super().to_dict(),
            "thumbnail_url": self.thumbnail_url,
        }


class AddOrderPayload(BaseModel):
    name: str
    thumbnail_url: str = ""
