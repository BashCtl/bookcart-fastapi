from fastapi import HTTPException, status, Response
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

        return cart

    @classmethod
    def delete_cart_item(cls, book_id: int, user: User, db: Session):
        cart = db.query(Cart).filter(and_(Cart.user_id == user.id,
                                          Cart.completed == False)).first()
        if not cart:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Cart not found.")

        cart_item = db.query(CartItem).filter(and_(CartItem.cart_id == cart.id,
                                                   CartItem.book_id == book_id))

        if not cart_item.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found.")

        cart_item.delete(synchronize_session=False)
        db.commit()

        return Response(status_code=status.HTTP_204_NO_CONTENT)

    @classmethod
    def delete_current_cart(cls, user: User, db: Session):
        cart_query=db.query(Cart).filter(and_(Cart.user_id == user.id,
                                          Cart.completed == False))
        if not cart_query.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Cart not found.")

        cart_query.delete(synchronize_session=False)
        db.commit()

        return Response(status_code=status.HTTP_204_NO_CONTENT)

    @classmethod
    def get_current_cart(cls, user: User, db: Session):
        cart = db.query(Cart).filter(and_(Cart.user_id == user.id,
                                          Cart.completed == False)).first()
        if not cart:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Cart not found.")

        return cart
