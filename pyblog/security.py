from datetime import datetime, timedelta
from jose import jwt, JWTError
from passlib.context import CryptContext

from pyblog.config import Config

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_password_hash(password: str):
    return pwd_context.hash(password)


def verify_password_hash(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)


# @TODO: Investigate more about the subject in the dict
# @TODO: Add OAuth2 Bearer authentication
def create_access_token(sub: str, expires_delta: datetime | None = None):
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=Config.TOKEN_EXPIRE)

    to_encode = {"exp": expire, "sub": sub}
    encoded_jwt = jwt.encode(to_encode, Config.SECRET_KEY, algorithm=Config.HASH_ALGO)
    return encoded_jwt
