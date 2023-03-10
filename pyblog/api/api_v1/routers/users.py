from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from pyblog.deps import get_db
from pyblog.schemas import UserSchema, UserCreate
from pyblog.services import user_service


router = APIRouter()


@router.get("/{user_id}", response_model=UserSchema)
def get_user(user_id: int, db: Session = Depends(get_db)):
    db_user = user_service.get(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found.")
    return db_user


@router.get("/profile/{username}", response_model=UserSchema)
def get_user_by_username(username: str, db: Session = Depends(get_db)):
    db_user = user_service.get_by_username(db, username=username)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found.")
    return db_user


@router.post("/", response_model=UserSchema)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    return user_service.create(db, user)
