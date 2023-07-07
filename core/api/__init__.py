from fastapi import APIRouter
from core.api.profile import router as profile_router
from core.api.ping import router as ping_router

router = APIRouter(prefix="/api")
router.include_router(ping_router)

router.include_router(profile_router)
