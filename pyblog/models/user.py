from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from pyblog.db import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    display_name = Column(String)
    password = Column(String, nullable=False)

    posts = relationship("Post", back_populates="user")
