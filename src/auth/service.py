import stat

from annotated_types import T
from sqlmodel import select
from src.auth.models import User
from src.auth.userSchema import userCreateSchema
from src.db.main import SessionDep
from src.auth.utill import verify_password, get_password_hash


class UserService:
    def get_user_by_email(self, email: str, session: SessionDep):
        statement = select(User).where(User.email == email)
        result = session.exec(statement)
        user = result.first()
        if user:
            return user
        return None

    def user_exists(self, email: str, session: SessionDep):
        user = self.get_user_by_email(email, session)
        print("User_____________________________________", user)
        return True if user else False

    def create_user(self, user: userCreateSchema, session: SessionDep):
        user_data = user.model_dump()
        new_user = User(**user_data)
        hashed_password = get_password_hash(user.password)
        new_user.password_hash = hashed_password
        session.add(new_user)
        session.commit()
        session.refresh(new_user)
        return new_user
