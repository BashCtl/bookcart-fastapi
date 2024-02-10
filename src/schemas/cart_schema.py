from pydantic import BaseModel
from src.schemas.cart_item_schema import CartItemSchema
from typing import List


class CartOut(BaseModel):
    id: int
    user_id: int
    cart_items: List[CartItemSchema]
