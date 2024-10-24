from typing import Optional, List

from pydantic import BaseModel


class WorkerSchema(BaseModel):
    id: int
    organization_id: int
    tasks: Optional[List["TaskSchema"]] = None  # Вложенные модели

    class Config:
        from_attributes = True


from src.db.tasks.schemas import TaskSchema
