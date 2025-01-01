from sqlmodel.ext.asyncio.session import AsyncSession
from .bookSchema import BookCreate, BookUpdate
from datetime import date, datetime
from .models import Book
from sqlmodel import select, desc
from uuid import UUID
from src.db.main import SessionDep


class BookService:
    def get_book(self, book_uid: UUID, session: SessionDep):
        statement = select(Book).where(Book.uid == book_uid)
        result = session.exec(statement)
        book = result.first()
        print("Book_________________________________________________________--", book)
        if book:
            book.published_date = book.published_date
        return book

    def get_all_books(self, session: SessionDep):
        statement = select(Book)
        books = session.exec(statement)
        books = books.all()
        for book in books:
            book.published_date = book.published_date
        return books

    def create_book(self, bookCreateData: BookCreate, session: SessionDep):
        book_data = bookCreateData.model_dump()
        new_book = Book(**book_data)
        session.add(new_book)
        session.commit()
        return new_book

    def update_book(
        self, book_uid: UUID, bookUpdateData: BookUpdate, session: SessionDep
    ):
        book_to_update = self.get_book(book_uid, session)
        if book_to_update is not None:
            update_data_dict = bookUpdateData.model_dump()

            for k, v in update_data_dict.items():
                setattr(book_to_update, k, v)

            session.commit()

            return book_to_update
        else:
            return {"message": "Book not found"}

    def delete_book(self, book_uid: UUID, session: SessionDep):
        book_to_delete = self.get_book(book_uid, session)
        if book_to_delete is not None:
            print("Book to delete", book_to_delete)
            session.delete(book_to_delete)
            session.commit()
            return {"message": "Book deleted successfully"}
        else:
            return {"message": "Book not found"}
