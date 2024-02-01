from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from . import Base


class CartItem(Base):
    __tablename__ = "cart_items"
    id = Column(Integer, primary_key=True, nullable=False)
    cart_id = Column(Integer, ForeignKey("carts.id", ondelete="CASCADE"), nullable=False)
    book_id = Column(Integer, ForeignKey("books.id", ondelete="CASCADE"), nullable=False)
    quantity = Column(Integer, default=1)
    cart = relationship("Cart")
    book = relationship("Book")
