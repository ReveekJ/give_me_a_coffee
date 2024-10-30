from typing import Optional, List

from pydantic import BaseModel



class OrganizationSchema(BaseModel):
    id: Optional[int] = None
    name: str
    owner_id: int
    # owner: Optional["OwnerSchema"] = None  # Вложенная модель
    workers: Optional[List["WorkerSchema"]] = None  # Вложенные модели
    tasks: Optional[List["TaskSchema"]] = None  # Вложенные модели
    menu: Optional[List["FoodGroupSchema"]] = None  # Вложенные модели

    class Config:
        from_attributes = True


from src.db.owners.schemas import OwnerSchema
from src.db.tasks.schemas import TaskSchema
from src.db.workers.schemas import WorkerSchema
from src.db.menu.schemas import FoodGroupSchema
