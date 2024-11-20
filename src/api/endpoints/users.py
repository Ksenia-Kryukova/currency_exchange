from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from api.models.user import User, UserInDB
from api.models.token import Token
from db.db import collection, save_user
from core.security import (
    get_password_hash,
    get_user_from_db,
    authenticate_user,
    authorization_user
)


router_auth = APIRouter(prefix="/auth", tags=["auth"])


@router_auth.post("/register", response_model=Token)
async def register_user(user: User):
    '''
    Конечная точка для регистрации и авторизации пользователя
    '''
    if get_user_from_db(collection, user.username) is None:
        hashed_password = get_password_hash(user.password)
        user_in_db = UserInDB(
            **user.model_dump(exclude={"password"}),
            hashed_password=hashed_password
            )
        save_user(user_in_db)
        token = authorization_user(user_in_db)
        return token
    else:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="A user with this name already exists"
        )


@router_auth.post("/login")
async def login_user(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()]
) -> Token:
    '''
    Конечная точка для входа пользователя.
    '''
    user = authenticate_user(
        collection,
        form_data.username,
        form_data.password
        )
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return authorization_user(user)
