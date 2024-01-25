from fastapi import APIRouter
from src.api.v1.handlers.users import users_router
from src.api.v1.handlers.login import login_router

router = APIRouter()

router.include_router(users_router, prefix='/users', tags=['users'])
router.include_router(login_router, prefix='', tags=['login'])