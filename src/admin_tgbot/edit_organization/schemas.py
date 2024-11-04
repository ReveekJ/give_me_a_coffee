from typing import Optional

from pydantic import BaseModel

from src.db.organizations.schemas import OrganizationSchema


class MainMenuData(BaseModel):
    organization_id: int
    selected_worker_id: Optional[int] = None
