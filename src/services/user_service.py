from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from src.models.user_model import User
from src.schemas.user_schema import NewUser, UpdateUser
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

    @classmethod
    def update_user(cls, id: int, body: UpdateUser, db: Session, current_user: User):
        user_query = db.query(User).filter(User.id == id)

        if not user_query.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

        if user_query.first().id != current_user.id or not current_user.is_admin:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                                detail="Not authorized to perform requested action.")

        if body.username and db.query(User).filter(User.username == body.username).first():
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Username already exists.")

        user_query.update(body.model_dump(exclude_unset=True), synchronize_session=False)
        db.commit()

        return user_query.first()

    @classmethod
    def get_all_users(cls, db: Session):
        all_users = db.query(User).all()

        return all_users

    @classmethod
    def get_single_user(cls, id: int, db : Session):
        user = db.query(User).filter(User.id==id).first()
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found.")

        return user
