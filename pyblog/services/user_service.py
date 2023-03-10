from sqlalchemy.orm import Session

from pyblog.models import User
from pyblog.schemas import UserCreate


class UserService():

    def get_user(self, db: Session, user_id: int):
        return db.query(User).filter(User.id == user_id).first()

    def create_user(self, db: Session, user: UserCreate):
        db_user = User(
            username=user.username,
            display_name=user.display_name,
        )
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user


user_service = UserService()
