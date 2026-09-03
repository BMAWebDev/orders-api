from .db import db, Base
from sqlalchemy import Float, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .order_products import OrderProduct


class Product(Base, db.Model):
    __tablename__ = "products"

    price: Mapped[float] = mapped_column(Float, nullable=False, default=0.00)
    quantity: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    description: Mapped[str] = mapped_column(String)
    thumbnail_url: Mapped[str] = mapped_column(String)

    order_products: Mapped[list["OrderProduct"]] = relationship(
        back_populates="product"
    )

    def __repr__(self) -> str:
        return f"<Product> ID: {self.id}"

    def __init__(self, name: str):
        super().__init__(name)

    def to_dict(self):
        return super().to_dict()
