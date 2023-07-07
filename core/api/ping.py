from fastapi import APIRouter

from core.registry import ping_storage, server_started, VERSION

router = APIRouter()


@router.get("/ping")
async def ping() -> dict[str, str]:
    return {
        "ping": await ping_storage.ping(),
        "server_started": str(server_started),
        "version": VERSION,
    }
