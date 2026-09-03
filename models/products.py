from .db import db, Base
from sqlalchemy import Float, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .order_products import OrderProduct


class Product(Base, db.Model):
    __tablename__ = "products"

    price: Mapped[float] = mapped_column(Float, nullable=False, default=0.00)
    quantity: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    description: Mapped[str | None] = mapped_column(String, nullable=True)
    thumbnail_url: Mapped[str | None] = mapped_column(String, nullable=True)

    order_products: Mapped[list["OrderProduct"]] = relationship(
        back_populates="product"
    )

    def __repr__(self) -> str:
        return f"<Product> ID: {self.id}"

    def __init__(
        self,
        name: str,
        price: float,
        quantity: int,
        description: str | None = None,
        thumbnail_url: str | None = None,
    ):
        super().__init__(name)
        self.price = price
        self.quantity = quantity
        self.description = description
        self.thumbnail_url = thumbnail_url

    def to_dict(self):
        return super().to_dict()
