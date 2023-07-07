from uuid import UUID

from fastapi import APIRouter

from core.model.profile import ProfileDB
from core.registry import profile_storage

router = APIRouter()


@router.get("/id")
async def profile_by_id(profile_id: UUID) -> ProfileDB:
    return await profile_storage.get_by_id(profile_id)
