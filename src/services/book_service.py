from fastapi import HTTPException, status, Response
from sqlalchemy.orm import Session
from sqlalchemy import and_

from src.models.book_model import Book
from src.schemas.book_schema import NewBook, UpdateBook


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

    @classmethod
    def get_single_book(cls, id: int, db: Session):
        book = db.query(Book).filter(Book.id == id).first()
        if not book:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found.")

        return book

    @classmethod
    def update_book(cls, id: int, body: UpdateBook, db: Session):
        book_query = db.query(Book).filter(Book.id == id)
        if not book_query.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found.")

        book_query.update(body.model_dump(exclude_unset=True), synchronize_session=False)
        db.commit()

        return book_query.first()

    @classmethod
    def delete_book(cls, id: int, db: Session):
        book_query = db.query(Book).filter(Book.id == id)
        if not book_query.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found.")

        book_query.delete(synchronize_session=False)
        db.commit()

        return Response(status_code=status.HTTP_204_NO_CONTENT)
