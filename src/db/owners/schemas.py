from typing import Optional, List

from pydantic import BaseModel


class OwnerSchema(BaseModel):
    id: int
    organizations: Optional[List["OrganizationSchema"]] = None  # Вложенные модели

    class Config:
        from_attributes = True


from src.db.organizations.schemas import OrganizationSchema
