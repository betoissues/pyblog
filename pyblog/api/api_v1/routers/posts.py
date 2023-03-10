from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from pyblog.deps import get_db
from pyblog.schemas import PostSchema, PostCreate
from pyblog.services import post_service

router = APIRouter()


@router.get("/", response_model=list[PostSchema])
def get_posts(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    posts = post_service.get_posts(db, skip=skip, limit=limit)
    return posts


@router.post("/", response_model=PostSchema)
def create_post(post: PostCreate, db: Session = Depends(get_db)):
    return post_service.create_post(db, post)
