from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session

from src.core.database import get_db
from src.models.user_model import User
from src.schemas.category_schema import NewCategory, CategoryRes
from src.services.auth_service import AuthService
from src.services.category_service import CategoryService

categories_router = APIRouter()


@categories_router.post("/", response_model=CategoryRes, status_code=status.HTTP_201_CREATED)
def add_category(body: NewCategory, db: Session = Depends(get_db), admin: User = Depends(AuthService.get_admin_user)):
    return CategoryService.add_category(body, db)


@categories_router.get("/{id}", response_model=CategoryRes, status_code=status.HTTP_200_OK)
def get_category_by_id(id: int, db: Session = Depends(get_db)):
    return CategoryService.get_single_category(id, db)
