from typing import Annotated
from uuid import UUID

from fastapi import APIRouter, Depends

from core.auth import get_current_profile
from core.model.profile import ProfileDB

router = APIRouter()


@router.get("/current", response_model=ProfileDB)
async def get_current_profile(current_profile: Annotated[ProfileDB, Depends(get_current_profile)]) -> ProfileDB:
    return current_profile
