import os
from datetime import timedelta, datetime
from typing import Annotated

from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from passlib.context import CryptContext
from pydantic import BaseModel
from starlette import status

from core.model.profile import ProfileDB
from core.registry import profile_storage

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
SECRET_KEY = os.getenv("SECRET_KEY", "abc")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_DAYS = 365


class Token(BaseModel):
    access_token: str
    token_type: str


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


async def authenticate(email: str, password: str):
    profile = await profile_storage.get_by_email(email)
    if not profile:
        return False
    if not verify_password(password, profile.password):
        return False
    return profile


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


class TokenData(BaseModel):
    email: str | None = None


async def get_current_profile(token: Annotated[str, Depends(oauth2_scheme)]) -> ProfileDB:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    profile = await profile_storage.get_by_email(email=token_data.email)
    if profile is None:
        raise credentials_exception
    return profile
