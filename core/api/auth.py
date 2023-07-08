from datetime import timedelta
from typing import Annotated

from fastapi import APIRouter, Depends

from core.auth import Token, authenticate, ACCESS_TOKEN_EXPIRE_DAYS, create_access_token
from core.utils import throw_credential_exception

router = APIRouter()


@router.post("/token", response_model=Token)
async def login_for_access_token(email: str, password: str):
    profile = await authenticate(email, password)
    if not profile:
        throw_credential_exception()
    access_token_expires = timedelta(days=ACCESS_TOKEN_EXPIRE_DAYS)
    access_token = create_access_token(
        data={"sub": profile.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}
