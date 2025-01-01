from fastapi import FastAPI
from src.book.router import book_router
from src.auth.routes import authRouter as auth_router
from contextlib import asynccontextmanager
from src.db.main import create_db_and_tables


@asynccontextmanager
async def life_span(app: FastAPI):
    print("start")
    # create_db_and_tables()
    yield
    print("end")


version = "v1"


app = FastAPI(
    title="Book API",
    description="A simple book API",
    version=version,
    openapi_url=f"/{version}/openapi.json",
    lifespan=life_span,
)


app.include_router(book_router, prefix=f"/api/{version}/books", tags=["Books"])
app.include_router(auth_router, prefix=f"/api/{version}/books", tags=["Auth"])
