from typing import Annotated

from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from sqlalchemy.orm import Session
from starlette import status

from database import session_local
from settings import ALGORITHM, SECRET_KEY

oauth_bearer = OAuth2PasswordBearer(tokenUrl="auth/token")


def get_db():
    sqlite_db = session_local()
    try:
        yield sqlite_db
    finally:
        sqlite_db.close()


async def get_current_user(token: Annotated[str, Depends(oauth_bearer)]):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
        username: str = payload.get("sub")
        id: int = payload.get("id")

        if username is None or id is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail=f"Token is not valid {id} {username}",
            )
        return {
            "username": username,
            "id": id,
        }
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token is not valid",
        )


db_dependency = Annotated[Session, Depends(get_db)]
user_dependency = Annotated[dict, Depends(get_current_user)]
