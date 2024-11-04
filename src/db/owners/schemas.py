from typing import Optional

from pydantic import BaseModel


class OwnerSchema(BaseModel):
    id: int
    organizations: Optional[list["OrganizationSchema"]] = []  # Вложенные модели

    class Config:
        from_attributes = True


from src.db.organizations.schemas import OrganizationSchema
