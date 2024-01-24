from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session

from src.core.database import get_db
from src.models.user_model import User

users_router = APIRouter()