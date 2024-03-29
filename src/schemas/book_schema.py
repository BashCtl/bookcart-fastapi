from pydantic import BaseModel, Field
from typing import Optional
from src.schemas.author_schema import AuthorRes
from src.schemas.category_schema import CategoryRes


class NewBook(BaseModel):
    title: str = Field(..., max_length=100, min_length=1)
    quantity: Optional[int] = None
    author_id: int
    category_id: int


class BookRes(BaseModel):
    id: int
    title: str
    quantity: int
    author: AuthorRes
    category: CategoryRes


class UpdateBook(BaseModel):
    title: Optional[str] = None
    quantity: Optional[int] = None
    author_id: Optional[int] = None
    category_id: Optional[int] = None
