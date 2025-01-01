from fastapi import APIRouter, Depends, HTTPException, status
from src.book.bookSchema import BookUpdate, Book, BookAll, BookAllResponse
from src.book.service import BookService
from sqlmodel.ext.asyncio.session import AsyncSession
from src.db.main import SessionDep


book_router = APIRouter()

book_service = BookService()


@book_router.get("/", response_model=list[BookAll], status_code=status.HTTP_200_OK)
def get_all_books(session: SessionDep):
    return book_service.get_all_books(session)


@book_router.post(
    "/", response_model=BookAllResponse, status_code=status.HTTP_201_CREATED
)
def create_book(book: Book, session: SessionDep):
    new_book = book_service.create_book(book, session)
    return new_book


@book_router.get("/{book_id}", response_model=BookAll, status_code=status.HTTP_200_OK)
def get_book_by_id(book_id: str, session: SessionDep) -> Book:
    book = book_service.get_book(book_id, session)
    if book:
        return book

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Book with id {book_id} not found",
    )


@book_router.patch("/{book_id}")
def update_book(book_id: str, updateBook: BookUpdate, session: SessionDep):
    book = book_service.update_book(book_id, updateBook, session)
    if book:
        return book
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Book with id {book_id} not found",
    )


@book_router.delete("/{book_id}", response_model=dict, status_code=status.HTTP_200_OK)
def delete_book(book_id: str, session: SessionDep):
    book = book_service.delete_book(book_id, session)
    if book:
        return book
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Book with id {book_id} not found",
    )
