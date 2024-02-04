from fastapi import APIRouter
from src.api.v1.handlers.users import users_router
from src.api.v1.handlers.login import login_router
from src.api.v1.handlers.authors import authors_router
from src.api.v1.handlers.categories import categories_router
from src.api.v1.handlers.books import books_router
from src.api.v1.handlers.carts import carts_router

router = APIRouter()

router.include_router(users_router, prefix="/users", tags=["users"])
router.include_router(login_router, prefix="", tags=["login"])
router.include_router(authors_router, prefix="/authors", tags=["authors"])
router.include_router(categories_router, prefix="/categories", tags=["categories"])
router.include_router(books_router, prefix="/books", tags=["books"])
router.include_router(carts_router, prefix="/cart", tags=["cart"])
