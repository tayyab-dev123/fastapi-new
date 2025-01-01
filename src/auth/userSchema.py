from typing import Optional
from click import Option
from pydantic import BaseModel
from sqlmodel import Field
from datetime import date, datetime
import uuid


class userCreateSchema(BaseModel):
    first_name: str
    last_name: str
    username: str
    is_verfiied: Optional[bool] = False
    password: str = Field(min_length=6, max_length=50)
    email: str


class UserResponse(BaseModel):
    uid: uuid.UUID
    username: str
    first_name: str
    last_name: str
    email: str
    is_verfiied: bool
    created_at: datetime
    updated_at: datetime
