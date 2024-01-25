from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime
from . import Base


class Author(Base):
    __tablename__ = "authors"
    id = Column(Integer, primary_key=True, nullable=False)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)

    def __repr__(self):
        return f"Author(first_name={self.first_name}, last_name={self.last_name})"
