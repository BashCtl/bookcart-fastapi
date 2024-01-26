from sqlalchemy.orm import Session

from src.schemas.author_schema import NewAuthor
from src.models.author_model import Author


class AuthorService:

    @classmethod
    def add_author(cls, body: NewAuthor, db: Session):
        new_author = Author(**body.model_dump())
        db.add(new_author)
        db.commit()
        db.refresh(new_author)

        return new_author
