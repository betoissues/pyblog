import os
from dotenv import load_dotenv

load_dotenv()


class Config():
    SECRET_KEY = os.getenv("SECRET_KEY")
    DATABASE_URL = os.getenv("DATABASE_URL")
    HASH_ALGO = os.getenv("HASH_ALGO")
    TOKEN_EXPIRE = os.getenv("TOKEN_EXPIRE")
