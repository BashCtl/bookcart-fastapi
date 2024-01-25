from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from . import Base


class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String(100), nullable=False)
    author_id = Column(Integer, ForeignKey("authors.id", ondelete="CASCADE"), nullable=False)
    category_id = Column(Integer, ForeignKey("categories.id", ondelete="CASCADE"), nullable=False)
    author = relationship("Author")
    category = relationship('Category')

    def __repr__(self):
        return f"Book(title={self.title})"
