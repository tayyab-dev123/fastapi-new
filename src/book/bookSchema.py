from pydantic import BaseModel
from typing import Optional
from datetime import date, datetime
import uuid


class Book(BaseModel):
    title: str
    author: str
    publisher: str
    published_date: date
    page_count: int
    language: str
    created_at: datetime
    updated_at: datetime


class BookAll(Book):
    uid: uuid.UUID


class BookCreate(BaseModel):
    title: str
    author: str
    publisher: str
    published_date: date  # Changed from date to str
    page_count: int
    language: str


class BookAllResponse(BookCreate):
    uid: uuid.UUID


class BookUpdate(BaseModel):
    title: str
    author: str
    publisher: str
    page_count: int
    language: str
