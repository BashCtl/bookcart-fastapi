from datetime import datetime, timedelta

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt, JWTError
from sqlalchemy.orm import Session

from src.core.configs import settings
from src.core.database import get_db
from src.models.token_table import TokenTable
from src.models.user_model import User
from src.schemas.token_schema import TokenData
from src.utils.hashing import verify_password


class AuthService:
    SECRET_KEY = settings.SECRET_KEY
    ALGORITHM = settings.ALGORITHM
    ACCESS_TOKEN_EXPIRE_MINUTES = settings.ACCESS_TOKEN_EXPIRE_MINUTES
    REFRESH_TOKEN_EXPIRE_MINUTES = eval(settings.REFRESH_TOKEN_EXPIRE_MINUTES)
    JWT_REFRESH_SECRET = settings.JWT_REFRESH_SECRET

    oauth2_schema = OAuth2PasswordBearer(tokenUrl='/login')

    @classmethod
    def create_access_token(cls, data: dict):
        to_encode = data.copy()
        expire = datetime.utcnow() + timedelta(minutes=AuthService.ACCESS_TOKEN_EXPIRE_MINUTES)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, AuthService.SECRET_KEY, algorithm=AuthService.ALGORITHM)

        return encoded_jwt

    @classmethod
    def create_refresh_token(cls, data: dict, expire_delta: int = None):
        to_encode = data.copy()
        if expire_delta:
            expire_delta = datetime.utcnow() + timedelta(minutes=expire_delta)
        else:
            expire_delta = datetime.utcnow() + timedelta(minutes=AuthService.REFRESH_TOKEN_EXPIRE_MINUTES)
        to_encode.update({"exp": expire_delta})
        encoded_jwt = jwt.encode(to_encode, AuthService.JWT_REFRESH_SECRET, algorithm=AuthService.ALGORITHM)

        return encoded_jwt

    @classmethod
    def verify_access_token(cls, token: str, credential_exception):
        try:
            payload = jwt.decode(token, AuthService.SECRET_KEY, algorithms=[AuthService.ALGORITHM])
            id: int = payload.get("id")
            if id is None:
                raise credential_exception
            token_data = TokenData(id=id)
        except JWTError:
            raise credential_exception

        return token_data

    @classmethod
    def get_current_user(cls, token: str = Depends(oauth2_schema), db: Session = Depends(get_db)):
        credential_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                             detail="Could not validate credentials.",
                                             headers={"WWW-Authenticate": "Bearer"})

        token_data = AuthService.verify_access_token(token, credential_exception)
        user = db.query(User).filter(User.id == token_data.id).first()

        token_from_db = db.query(TokenTable).filter(TokenTable.access_token == token).first()
        if token_from_db.status:
            return user
        else:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token blocked")

    @classmethod
    def get_admin_user(cls, token: str = Depends(oauth2_schema), db: Session = Depends(get_db)):
        user = AuthService.get_current_user(token, db)
        if user.is_admin:
            return user
        else:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Access Forbidden.")

    @classmethod
    def login(cls, request: OAuth2PasswordRequestForm, db: Session):
        user = db.query(User).filter(User.username == request.username).first()
        if user is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials.")
        if not verify_password(request.password, user.password):
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials.")
        access_token = AuthService.create_access_token({"id": user.id})
        refresh_token = AuthService.create_refresh_token({"id": user.id})

        token_db = TokenTable(user_id=user.id, access_token=access_token, refresh_token=refresh_token, status=True)
        db.add(token_db)
        db.commit()
        db.refresh(token_db)

        return {"token_type": "bearer", "access_token": access_token, "refresh_token": refresh_token}
