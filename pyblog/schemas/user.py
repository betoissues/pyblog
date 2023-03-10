from pydantic import BaseModel
from pyblog.schemas import PostSchema


class UserBase(BaseModel):
    username: str
    display_name: str


class UserCreate(UserBase):
    password: str


class UserSchema(UserBase):
    id: int
    posts: list[PostSchema] = []

    class Config:
        orm_mode = True
