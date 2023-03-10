# PYBlog

**NOTE**: This is a constant work in progress, in an effort to stay up to date with Python and FastAPI changes.

This project is to test repository structure for FastAPI projects from scratch as a demo microblog, following the [FastAPI Tutorial](https://fastapi.tiangolo.com/tutorial/)

## Setup Instructions

1. Populate `.env`

```
DATABASE_URL=
SECRET_KEY=
HASH_ALGO=
TOKEN_EXPIRE=
```
2. Install dependencies `pip install -r requirements.txt`
3. Run DB migrations (pending)
4. Execute with uvicorn: `uvicorn pyblog.main:app --reload`

- - -

## Pending

- [  ] Add Alembic migrations
- [  ] Add return types
- [  ] Load configuration with Pydantic
