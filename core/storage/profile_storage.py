from typing import Optional
from uuid import UUID

from core.model.profile import ProfileDB
from core.storage.db.postgres import DB
from core.utils import throw_not_found


class ProfileStorage:
    def __init__(self, db: DB) -> None:
        self.db = db

    async def get_by_id(
        self, profile_id: UUID, throw_error: bool = False
    ) -> Optional[ProfileDB]:
        sql = "SELECT * FROM profile WHERE (id = $1)"
        row = await self.db.fetch_row(sql, profile_id)
        if not row and throw_error:
            throw_not_found("No user with this id!")
        profile = ProfileDB.model_validate(row)
        return profile

    async def get_by_email(
        self, username: str, throw_error: bool = False
    ) -> Optional[ProfileDB]:
        sql = "SELECT * FROM profile WHERE (email = $1)"
        row = await self.db.fetch_row(sql, username)
        if not row and throw_error:
            throw_not_found("No user with this id!")
        profile = ProfileDB.model_validate(row)
        return profile
