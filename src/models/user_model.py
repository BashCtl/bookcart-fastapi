from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime
from . import Base


class User(Base):
    id = Column(Integer, primary_key=True, nullable=False)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    username = Column(String(50), nullable=False, unique=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    password = Column(String(100), nullable=False)
