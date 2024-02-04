from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import and_

from src.models.cart_model import Cart
from src.models.cart_item import CartItem
from src.models.user_model import User
from src.schemas.cart_item_schema import CartItemSchema


class CartService:

    @classmethod
    def add_item(cls, body: CartItemSchema, user: User, db: Session):
        cart = db.query(Cart).filter(and_(Cart.user_id == user.id,
                                          Cart.completed == False)).first()
        if not cart:
            cart = Cart(user_id=user.id, completed=False)
            db.add(cart)
            db.commit()

        cart_item = db.query(CartItem).filter(and_(CartItem.cart_id == cart.id,
                                                   CartItem.book_id == body.book_id)).first()

        if cart_item is None:
            cart_item = CartItem(cart_id=cart.id, book_id=body.book_id, quantity=body.quantity)
            db.add(cart_item)
            db.commit()
        else:
            cart_item.quantity = body.quantity
            db.commit()
        db.refresh(cart_item)
        print(cart.cart_items)
        return cart
