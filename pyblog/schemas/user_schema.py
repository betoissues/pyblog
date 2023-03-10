from pydantic import BaseModel
from pyblog.schemas.post_schema import PostSchema


class UserBase(BaseModel):
    username: str
    display_name: str


class UserCreate(UserBase):
    pass


class UserSchema(UserBase):
    id: int
    posts: list[PostSchema] = []

    class Config:
        orm_mode = True
