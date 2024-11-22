import os
import jwt
from jwt.exceptions import InvalidTokenError
from typing import Annotated
from datetime import datetime, timedelta, timezone
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status
from dotenv import load_dotenv


from api.models.user import UserInDB
from api.models.token import Token, TokenData
from db.db import collection, get_user_from_db


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")


def get_password_hash(password: str):
    '''
    Функция для хэширования пароля.
    '''
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str):
    '''
    Функция для верификации пароля.
    '''
    return pwd_context.verify(plain_password, hashed_password)


def authenticate_user(collection, username: str, password: str):
    '''
    ФУнкция для аутентификации пользователя.
    '''
    user = get_user_from_db(collection, username)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user


def create_jwt_token(data: dict, expires_delta: timedelta | None = None):
    '''
    Создание jwt токена.
    '''
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def authorization_user(user: UserInDB):
    '''
    Авторизация пользователя.
    '''
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_jwt_token(
        data={"sub": user.username},
        expires_delta=access_token_expires
    )
    return Token(access_token=access_token, token_type="bearer")


async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    '''
    Проверка доступа у пользователя.
    '''
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except InvalidTokenError:
        raise credentials_exception
    user = get_user_from_db(collection, username=token_data.username)
    if user is None:
        raise credentials_exception
    return user
