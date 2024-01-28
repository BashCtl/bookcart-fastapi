from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, Boolean

from . import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, nullable=False)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    username = Column(String(50), nullable=False, unique=True)
    is_admin = Column(Boolean, default=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    password = Column(String(100), nullable=False)

    def __repr__(self):
        return f"User(first_name{self.first_name}, last_name={self.last_name})"
