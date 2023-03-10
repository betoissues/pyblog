from sqlalchemy.orm import Session
from pyblog.models import Post
from pyblog.schemas import PostCreate


class PostService():

    def get_posts(db: Session, skip: int = 0, limit: int = 100):
        return db.query(Post).offset(skip).limit(limit).all()

    def create_post(db: Session, post: PostCreate, user_id: int):
        db_post = Post(**post.dict(), user_id=user_id)
        db.add(db_post)
        db.commit()
        db.refresh(db_post)
        return db_post


post_service = PostService()
