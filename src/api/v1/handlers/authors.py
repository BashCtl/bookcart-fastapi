from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session

from src.core.database import get_db
from src.models.user_model import User
from src.schemas.author_schema import NewAuthor, AuthorRes
from src.services.author_service import AuthorService
from src.services.auth_service import AuthService

authors_router = APIRouter()


@authors_router.post("/", response_model=AuthorRes, status_code=status.HTTP_201_CREATED)
def add_author(body: NewAuthor, db: Session = Depends(get_db),
               current_account: User = Depends(AuthService.get_current_user)):
    return AuthorService.add_author(body, db)


@authors_router.put("/", response_model=AuthorRes, status_code=status.HTTP_201_CREATED)
def update_author(id: int, body: NewAuthor, db: Session = Depends(get_db),
                  current_account: User = Depends(AuthService.get_current_user)):
    return AuthorService.update_author(id, body, db)
