# from sqlmodel import Session, create_engine, SQLModel
# from sqlmodel.ext.asyncio.session import AsyncSession
# from sqlalchemy.orm import sessionmaker
# from sqlalchemy.ext.asyncio import AsyncEngine
# from src.config import Config

# engine = AsyncEngine(create_engine(Config.DATABASE_URL, echo=True))


# async def initdb():
#     """create a connection to our db"""

#     async with engine.begin() as conn:
#         from src.book.models import Book

#         await conn.run_sync(SQLModel.metadata.create_all)


# async def get_session() -> AsyncSession:
#     async_session = sessionmaker(
#         bind=engine, class_=AsyncSession, expire_on_commit=False
#     )

#     async with async_session() as session:
#         yield session


from typing import Annotated
from fastapi import Depends
from sqlmodel import Field, Session, SQLModel, create_engine, select
from src.config import Config


engine = create_engine(Config.DATABASE_URL, echo=True)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]
