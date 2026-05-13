from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Path
from sqlalchemy.orm import Session
from starlette import status

from database import session_local
from models.book import Book, BookRequest, BookResponse

router = APIRouter()


def get_db():
    sqlite_db = session_local()
    try:
        yield sqlite_db
    finally:
        sqlite_db.close()


sqlite_db_dependency = Annotated[Session, Depends(get_db)]


@router.get(
    "/books", response_model=list[BookResponse], status_code=status.HTTP_200_OK
)
async def read_all_books(db: sqlite_db_dependency):
    books = db.query(Book).all()
    return books


@router.post(
    "/books", response_model=BookResponse, status_code=status.HTTP_201_CREATED
)
async def create_book(db: sqlite_db_dependency, book_request: BookRequest):
    book_model = Book(**book_request.model_dump())

    db.add(book_model)
    db.commit()
    db.refresh(book_model)

    return book_model


@router.get(
    "/books/{book_id}",
    response_model=BookResponse,
    status_code=status.HTTP_200_OK,
)
async def read_book(db: sqlite_db_dependency, book_id: int = Path(gt=0)):
    book = db.query(Book).filter(Book.id == book_id).first()

    if book is None:
        raise HTTPException(404, "This book doesn't exists!")
    return book


@router.put("/books/{book_id}", status_code=status.HTTP_200_OK)
async def update_book(
    db: sqlite_db_dependency,
    book_request: BookRequest,
    book_id: int = Path(gt=0),
):
    book = db.query(Book).filter(Book.id == book_id).first()
    if book is None:
        raise HTTPException(404, "This book doesn't exists!")

    book.title = book_request.title
    book.author = book_request.author
    book.description = book_request.description
    book.rating = book_request.rating
    book.published_date = book_request.published_date

    db.commit()
    db.refresh(book)

    return book


@router.delete("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(db: sqlite_db_dependency, book_id: int = Path(gt=0)):
    result = db.query(Book).filter(Book.id == book_id).delete()

    if result == 0:
        raise HTTPException(404, "This book doesn't exists!")

    db.commit()
    return None
