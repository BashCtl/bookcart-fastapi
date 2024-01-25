from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime

from . import Base


class Category(Base):
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(50), nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"Category(name={self.name})"
