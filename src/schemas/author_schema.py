from pydantic import BaseModel, Field


class NewAuthor(BaseModel):
    first_name: str = Field(..., max_length=50)
    last_name: str = Field(..., max_length=50)


class AuthorRes(NewAuthor):
    id: int
