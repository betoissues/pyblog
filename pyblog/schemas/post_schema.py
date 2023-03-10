from pydantic import BaseModel


class PostBase(BaseModel):
    content: str


class PostCreate(PostBase):
    user_id: int


class PostSchema(PostBase):
    id: int

    class Config:
        orm_mode = True
