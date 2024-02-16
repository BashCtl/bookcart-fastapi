from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session

from src.core.database import get_db
from src.models.user_model import User
from src.schemas.cart_item_schema import CartItemSchema
from src.schemas.cart_schema import CartOut
from src.services.auth_service import AuthService
from src.services.cart_service import CartService

carts_router = APIRouter()


@carts_router.post("/", response_model=CartOut, status_code=status.HTTP_201_CREATED)
def add_book_to_cart(body: CartItemSchema, current_user: User = Depends(AuthService.get_current_user),
                     db: Session = Depends(get_db)):
    return CartService.add_item(body, current_user, db)


@carts_router.delete("/item/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_single_cart_item(id: int, current_user: User = Depends(AuthService.get_current_user),
                            db: Session = Depends(get_db)):
    return CartService.delete_cart_item(id, current_user, db)


@carts_router.get("/", response_model=CartOut, status_code=status.HTTP_200_OK)
def get_current_cart(current_user: User = Depends(AuthService.get_current_user),
                     db: Session = Depends(get_db)):
    return CartService.get_current_cart(current_user, db)


@carts_router.delete("/", status_code=status.HTTP_204_NO_CONTENT)
def delete_current_cart(current_user: User = Depends(AuthService.get_current_user),
                       db: Session = Depends(get_db)):
    return CartService.delete_current_cart(current_user, db)
