from typing import Optional, List

from pydantic import BaseModel


class TaskSchema(BaseModel):
    id: int
    organization_id: int
    worker_id: Optional[int] = None
    description: Optional[str] = None  # TODO: Если вы добавили это поле

    class Config:
        from_attributes = True


