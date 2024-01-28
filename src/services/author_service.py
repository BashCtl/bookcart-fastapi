from fastapi import HTTPException, status, Response
from sqlalchemy.orm import Session

from src.models.author_model import Author
from src.schemas.author_schema import NewAuthor


class AuthorService:

    @classmethod
    def add_author(cls, body: NewAuthor, db: Session):
        new_author = Author(**body.model_dump())
        db.add(new_author)
        db.commit()
        db.refresh(new_author)

        return new_author

    @classmethod
    def update_author(cls, id: int, body: NewAuthor, db: Session):
        author_query = db.query(Author).filter(Author.id == id)
        if not author_query.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Author with {id} id not found.")
        author_query.update(body.model_dump(), synchronize_session=False)
        db.commit()

        return author_query.first()

    @classmethod
    def delete_author(cls, id: int, db: Session):
        author_query = db.query(Author).filter(Author.id == id)
        if not author_query.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Author with id {id} not found.")
        author_query.delete(synchronize_session=False)
        db.commit()
        return Response(status_code=status.HTTP_204_NO_CONTENT)

    @classmethod
    def get_author_by_id(cls, id: int, db: Session):
        author_query = db.query(Author).filter(Author.id == id)
        if not author_query.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Author not found.")
        return author_query.first()

    @classmethod
    def get_all_author(cls, db: Session):
        all_authors = db.query(Author).all()

        return all_authors
