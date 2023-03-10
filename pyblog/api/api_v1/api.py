from fastapi import APIRouter
from pyblog.api.api_v1.routers import users, posts

api_router = APIRouter()
api_router.include_router(users.router, prefix="/users")
api_router.include_router(posts.router, prefix="/posts")
