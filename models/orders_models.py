from .db import db, Base
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column


class Order(Base, db.Model):
    __tablename__ = "orders"

    user_id: Mapped[int] = mapped_column(Integer, nullable=False)
    thumbnail_url: Mapped[str] = mapped_column(String)

    def __init__(self, name: str):
        super().__init__(name)

    def to_dict(self):
        return {
            **super().to_dict(),
            "thumbnail_url": self.thumbnail_url,
        }
