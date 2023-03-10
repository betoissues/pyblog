from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from .db import SessionLocal, Base, engine
from pyblog.schemas import (
    UserCreate,
    PostSchema,
    UserSchema,
)
from pyblog.services import post_service, user_service

Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/posts/", response_model=list[PostSchema])
def get_posts(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    posts = post_service.get_posts(db, skip=skip, limit=limit)
    return posts


@app.get("/users/{user_id}", response_model=UserSchema)
def get_user(user_id: int, db: Session = Depends(get_db)):
    db_user = user_service.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found.")
    return db_user


@app.post("/users/", response_model=UserSchema)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    return user_service.create_user(db, user)
