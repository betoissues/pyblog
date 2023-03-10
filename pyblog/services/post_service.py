from sqlalchemy.orm import Session
from pyblog.models import Post
from pyblog.schemas import PostCreate


class PostService():

    def get_posts(self, db: Session, skip: int = 0, limit: int = 100):
        return db.query(Post).offset(skip).limit(limit).all()

    def create_post(self, db: Session, post: PostCreate):
        db_post = Post(**post.dict())
        db.add(db_post)
        db.commit()
        db.refresh(db_post)
        return db_post


post_service = PostService()
