from typing import Optional

from pydantic import BaseModel


class OrganizationSchema(BaseModel):
    id: Optional[int] = None
    name: str
    owner_id: int
    # owner: Optional["OwnerSchema"] = None  # Вложенная модель
    workers: Optional[list["WorkerSchema"]] = []  # Вложенные модели
    tasks: Optional[list["TaskSchema"]] = []  # Вложенные модели
    menu: Optional[list["FoodGroupSchema"]] = []  # Вложенные модели

    class Config:
        from_attributes = True


from src.db.tasks.schemas import TaskSchema
from src.db.workers.schemas import WorkerSchema
from src.db.menu.schemas import FoodGroupSchema
