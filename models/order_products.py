from .db import db
from sqlalchemy import Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .orders import Order
    from .products import Product


class OrderProduct(db.Model):
    __tablename__ = "order_products"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, nullable=False)
    order_id: Mapped[int] = mapped_column(ForeignKey("orders.id"))
    product_id: Mapped[int] = mapped_column(ForeignKey("products.id"))

    order: Mapped["Order"] = relationship(back_populates="products")
    product: Mapped["Product"] = relationship(back_populates="order_products")

    def __repr__(self) -> str:
        return f"<Product> ID: {self.id}"

    def __init__(self):
        super().__init__()
