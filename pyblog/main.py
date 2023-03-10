from fastapi import FastAPI

from pyblog.api.api_v1.api import api_router
from pyblog.db import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title="PyBlog")

app.include_router(api_router, prefix="/api/v1")
