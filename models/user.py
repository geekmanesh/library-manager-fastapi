from pydantic import BaseModel
from sqlalchemy import Boolean, Column, Integer, String

from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True)
    username = Column(String, unique=True)

    first_name = Column(String)
    last_name = Column(String)

    hashed_password = Column(String)

    is_active = Column(Boolean, default=True)


class UserRequest(BaseModel):
    email: str
    username: str
    first_name: str
    last_name: str
    password: str
