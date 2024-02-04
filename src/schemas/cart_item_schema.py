from pydantic import BaseModel, Field


class CartItemSchema(BaseModel):
    book_id: int
    quantity: int
