from pydantic import BaseModel
from typing_extensions import Optional


class LocationSchema(BaseModel):
    id: Optional[int] = None
    name: str
    organization_id: int
