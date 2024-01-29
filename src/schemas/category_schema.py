from pydantic import BaseModel, Field
from datetime import datetime


class NewCategory(BaseModel):
    name: str = Field(..., max_length=30)


class CategoryRes(NewCategory):
    id:int
    created_at: datetime
