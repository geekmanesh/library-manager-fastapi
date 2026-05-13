from typing import Optional

from pydantic import BaseModel, Field
from sqlalchemy import Column, Integer, String

from database import Base


class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    author = Column(String)
    description = Column(String)
    rating = Column(Integer)
    published_date = Column(Integer)


class BookRequest(BaseModel):
    id: Optional[int] = Field(
        description="For creating book doesn't need to add id field",
        default=None,
    )
    title: str = Field(min_length=3)
    author: str = Field(min_length=1)
    description: str = Field(min_length=1, max_length=100)
    rating: int = Field(gt=0, lt=6)
    published_date: int = Field(gt=1999, lt=2031)

    class Config:
        schema_extra = {
            "example": {
                "title": "A new book",
                "author": "New Book Writer",
                "description": "Some information about book",
                "rating": 3,
                "published_date": 2026,
            }
        }


class BookResponse(BaseModel):
    id: int
    title: str
    author: str
    description: str
    rating: int
    published_date: int

    class Config:
        from_attributes = True
