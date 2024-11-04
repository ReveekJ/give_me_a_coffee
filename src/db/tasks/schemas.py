from typing import Optional

from pydantic import BaseModel

from src.db.menu.schemas import FoodSchema


class TaskSchema(BaseModel):
    id: int
    organization_id: int
    worker_id: Optional[int] = None
    description: Optional[list[FoodSchema]] = None  # TODO: Если вы добавили это поле

    class Config:
        from_attributes = True
