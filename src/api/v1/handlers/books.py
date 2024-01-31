from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session
from typing import List

from src.core.database import get_db
from src.models.user_model import User
from src.services.auth_service import AuthService
from src.schemas.book_schema import NewBook, BookRes, UpdateBook
from src.services.book_service import BookService

books_router = APIRouter()


@books_router.post("/", response_model=BookRes, status_code=status.HTTP_201_CREATED)
def add_new_book(body: NewBook, db: Session = Depends(get_db), admin: User = Depends(AuthService.get_admin_user)):
    return BookService.add_book(body, db)


@books_router.get("/", response_model=List[BookRes], status_code=status.HTTP_200_OK)
def get_all_books(db: Session = Depends(get_db)):
    return BookService.get_all_books(db)


@books_router.get("/{id}", response_model=BookRes, status_code=status.HTTP_200_OK)
def get_single_book(id: int, db: Session = Depends(get_db)):
    return BookService.get_single_book(id, db)


@books_router.patch("/{id}", response_model=BookRes, status_code=status.HTTP_201_CREATED)
def update_book(id: int, body: UpdateBook, db: Session = Depends(get_db),
                admin: User = Depends(AuthService.get_admin_user)):
    return BookService.update_book(id, body, db)


@books_router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book(id: int, db: Session = Depends(get_db), admin: User = Depends(AuthService.get_admin_user)):
    return BookService.delete_book(id, db)
