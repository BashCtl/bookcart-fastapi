from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import and_

from src.models.book_model import Book
from src.schemas.book_schema import NewBook


class BookService:

    @classmethod
    def add_book(cls, body: NewBook, db: Session):
        new_book = Book(**body.model_dump())
        db_book = db.query(Book).filter(and_(Book.title == body.title,
                                             Book.author_id == body.author_id,
                                             Book.category_id == body.category_id)).first()
        if db_book:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Book already exists.")
        db.add(new_book)
        db.commit()
        db.refresh(new_book)

        return new_book

    @classmethod
    def get_all_books(cls, db: Session):
        all_books = db.query(Book).all()

        return all_books
