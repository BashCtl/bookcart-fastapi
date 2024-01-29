from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session

from src.core.database import get_db
from src.schemas.user_schema import NewUser, UserResp, UpdateUser
from src.models.user_model import User
from src.services.user_service import UserService
from src.services.auth_service import AuthService

users_router = APIRouter()


@users_router.post('/', response_model=UserResp, status_code=status.HTTP_201_CREATED)
def create_user(body: NewUser, db: Session = Depends(get_db)):
    return UserService.create_user(body, db)


@users_router.patch("/{id}", response_model=UserResp, status_code=status.HTTP_200_OK)
def update_user(id: int, body: UpdateUser, db: Session = Depends(get_db),
                current_user: User = Depends(AuthService.get_current_user)):
    return UserService.update_user(id, body, db, current_user)
