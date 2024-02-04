from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session

from src.core.database import get_db
from src.models.user_model import User
from src.schemas.cart_item_schema import CartItemSchema
from src.services.auth_service import AuthService
from src.services.cart_service import CartService

carts_router = APIRouter()


@carts_router.post("/", status_code=status.HTTP_201_CREATED)
def add_book_to_cart(body: CartItemSchema, user: User = Depends(AuthService.get_current_user),
                     db: Session = Depends(get_db)):
    return CartService.add_item(body, user, db)