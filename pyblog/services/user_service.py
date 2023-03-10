from sqlalchemy.orm import Session

from pyblog.security import get_password_hash, verify_password_hash
from pyblog.models import User
from pyblog.schemas import UserCreate


class UserService():

    def get(self, db: Session, user_id: int):
        return db.query(User).filter(User.id == user_id).first()

    def get_by_username(self, db: Session, username: str):
        return db.query(User).filter(User.username == username).first()

    def create(self, db: Session, user: UserCreate):
        db_user = User(
            username=user.username,
            display_name=user.display_name,
            password=get_password_hash(user.password)
        )
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user

    def authenticate(self, db: Session, username: str, password: str):
        user = self.get_by_username(db, username)
        if not user:
            return None
        if not verify_password_hash(password, user.password):
            return None

        return user


user_service = UserService()
