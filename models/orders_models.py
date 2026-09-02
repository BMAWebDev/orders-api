from .db import db
from datetime import datetime
from sqlalchemy import Integer, String, DateTime
from sqlalchemy.orm import Mapped, mapped_column


class Order(db.Model):
    __tablename__ = "orders"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    created_at: Mapped[str] = mapped_column(
        String, default=datetime.now().isoformat(), nullable=False
    )

    def to_dict(self):
        return {"id": self.id, "name": self.name, "created_at": self.created_at}
