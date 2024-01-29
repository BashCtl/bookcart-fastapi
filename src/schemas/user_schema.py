from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional


class NewUser(BaseModel):
    first_name: str = Field(..., min_length=2, max_length=50)
    last_name: str = Field(..., min_length=2, max_length=50)
    username: str = Field(..., min_length=2, max_length=50)
    password: str = Field(..., min_length=6, max_length=50)


class UpdateUser(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    username: Optional[str] = None
    password: Optional[str] = None


class UserResp(BaseModel):
    id: int
    username: str
    first_name: str
    last_name: str
    is_admin: bool
    created_at: datetime
