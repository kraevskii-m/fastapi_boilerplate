from typing import Optional
from uuid import UUID

from core.model.profile import Profile
from core.storage.db.postgres import DB
from core.utils import throw_not_found


class ProfileStorage:
    def __init__(self, db: DB) -> None:
        self.db = db

    async def get_by_id(
        self, profile_id: UUID, throw_error: bool = False
    ) -> Optional[Profile]:
        sql = "SELECT * FROM profile WHERE (id = $1)"
        row = await self.db.fetch_row(sql, profile_id)
        if not row and throw_error:
            throw_not_found("No user with this id!")
        profile = Profile.parse_obj(row)
        return profile
