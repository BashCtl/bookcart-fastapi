from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session

from src.core.database import get_db
from src.models.user_model import User
from src.services.auth_service import AuthService
from src.schemas.book_schema import NewBook, BookRes
from src.services.book_service import BookService

books_router = APIRouter()


@books_router.post("/", response_model=BookRes, status_code=status.HTTP_201_CREATED)
def add_new_book(body: NewBook, db: Session = Depends(get_db), admin: User = Depends(AuthService.get_admin_user)):
    return BookService.add_book(body, db)
