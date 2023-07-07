from uuid import UUID

from fastapi import APIRouter

from core.model.profile import Profile
from core.registry import profile_storage

router = APIRouter()


@router.get("/id")
async def profile_by_id(profile_id: UUID) -> Profile:
    return await profile_storage.get_by_id(profile_id)
