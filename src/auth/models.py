from turtle import update
from typing import Optional
from click import Option
from sqlmodel import SQLModel, Field
from datetime import date, datetime
import uuid


class User(SQLModel, table=True):
    __tablename__ = "users"

    uid: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    username: str
    first_name: str
    last_name: str
    is_verfiied: str
    email: str
    password_hash: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
