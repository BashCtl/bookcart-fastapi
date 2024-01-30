from pydantic import BaseModel, Field
from datetime import datetime
from src.schemas.author_schema import AuthorRes
from src.schemas.category_schema import CategoryRes


class NewBook(BaseModel):
    title: str = Field(..., max_length=100, min_length=1)
    author_id: int
    category_id: int


class BookRes(BaseModel):
    id: int
    title: str
    author: AuthorRes
    category: CategoryRes
