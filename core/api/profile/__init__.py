from fastapi import APIRouter
from core.api.profile.curremt import router as id_router

router = APIRouter(prefix="/profile")
router.include_router(id_router)
