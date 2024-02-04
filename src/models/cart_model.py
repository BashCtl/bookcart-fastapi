from datetime import datetime

from sqlalchemy import Column, Integer, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship

from . import Base


class Cart(Base):
    __tablename__ = "carts"
    id = Column(Integer, primary_key=True, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    completed = Column(Boolean, default=False)
    user = relationship("User")
    cart_items = relationship("CartItem")

    def __repr__(self):
        return f"Cart(id={self.id}, user_id={self.user_id})"
