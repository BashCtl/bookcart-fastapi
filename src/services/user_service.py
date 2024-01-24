from sqlalchemy.orm import Session

from src.schemas.user_schema import NewUser
from src.models.user_model import User
from src.utils.hashing import hashing_password


class UserService:

    @classmethod
    def create_user(cls, body: NewUser, db: Session):
        body.password = hashing_password(body.password)
        new_user = User(**body.model_dump())
        db.add(new_user)
        db.commit()
        db.refresh(new_user)

        return new_user
