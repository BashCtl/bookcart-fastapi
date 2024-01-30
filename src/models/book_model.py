from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import UniqueConstraint

from . import Base


class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String(100), nullable=False)
    author_id = Column(Integer, ForeignKey("authors.id", ondelete="CASCADE"), nullable=False)
    category_id = Column(Integer, ForeignKey("categories.id", ondelete="CASCADE"), nullable=False)
    author = relationship("Author")
    category = relationship('Category')
    __table_args__ = (UniqueConstraint("title", "author_id", "category_id", name="_book_title_uc"),)

    def __repr__(self):
        return f"Book(title={self.title})"
