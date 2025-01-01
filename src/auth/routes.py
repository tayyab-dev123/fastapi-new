import email
from fastapi import APIRouter, HTTPException, status
from httpx import get
from src.auth.userSchema import UserResponse, userCreateSchema
from src.db.main import SessionDep
from src.auth.service import UserService


authRouter = APIRouter()

userService = UserService()


@authRouter.post(
    "/signup", response_model=UserResponse, status_code=status.HTTP_201_CREATED
)
def create_user(
    user_data: userCreateSchema,
    session: SessionDep,
):
    email = user_data.email

    userExists = userService.user_exists(email, session)
    print("User exists_____________________________________", userExists)
    if userExists:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User already exists",
        )
    user = userService.create_user(user_data, session)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User not created",
        )

    return user
