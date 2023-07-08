from datetime import datetime
from uuid import UUID
from pydantic import BaseModel, EmailStr


class Profile(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr


class ProfileDB(Profile):
    id: UUID
    created: datetime
    updated: datetime
