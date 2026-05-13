from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from models.user import User, UserRequest
from routers.book import sqlite_db_dependency
from security import authenticate_user, bcrypt_context

router = APIRouter()

def authenticate_user(username: str, password: str, db: sqlite_db_dependency) -> bool:
    user = db.query(User).


@router.post("/auth")
async def create_user(db: sqlite_db_dependency, request: UserRequest):
    user_model = User(
        email=request.email,
        username=request.username,
        first_name=request.first_name,
        last_name=request.last_name,
        hashed_password=bcrypt_context.hash(request.password),
        is_active=True,
    )

    db.add(user_model)
    db.commit()


@router.post("/token")
async def login_to_get_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    db: sqlite_db_dependency,
):
    user = authenticate_user(form_data.username, form_data.password, db)

    if not user:
        return "Failed authenticated"
    return "Successful authenticated"
