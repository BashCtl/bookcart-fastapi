from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from src.models.category_model import Category
from src.schemas.category_schema import NewCategory


class CategoryService:

    @classmethod
    def add_category(cls, body: NewCategory, db: Session):
        new_category = Category(**body.model_dump())
        db_category = db.query(Category).filter(Category.name == new_category.name).first()

        if db_category:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Category already exist.")

        db.add(new_category)
        db.commit()
        db.refresh(new_category)

        return new_category

    @classmethod
    def get_single_category(cls, id: int, db: Session):
        category = db.query(Category).filter(Category.id == id)
        if not category.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Category not found.")

        return category.first()
