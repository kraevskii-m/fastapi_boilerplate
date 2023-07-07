from datetime import datetime
from uuid import UUID
from pydantic import BaseModel


class Profile(BaseModel):
    first_name: str
    last_name: str
    password: str
    email: str


class ProfileDB(Profile):
    id: UUID
    created: datetime
    updated: datetime
