from .db import db, Base
from pydantic import BaseModel
from sqlalchemy import Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .order_products import OrderProduct


class Order(Base, db.Model):
    __tablename__ = "orders"

    # user_id: Mapped[int] = mapped_column(
    #     Integer,
    #     nullable=False,
    # )
    # product_id: Mapped[int] = mapped_column(Integer, nullable=False)

    products: Mapped[list["OrderProduct"]] = relationship(back_populates="order")

    def __init__(self, name: str):
        super().__init__(name)
        self.user_id = 1

    def to_dict(self):
        return {
            **super().to_dict(),
        }


class AddOrderPayload(BaseModel):
    name: str
