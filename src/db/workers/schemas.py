from typing import Optional

from pydantic import BaseModel


class WorkerSchema(BaseModel):
    id: int
    name: Optional[str] = ''
    username: Optional[str] = ''
    organization_id: int
    tasks: Optional[list["TaskSchema"]] = []  # Вложенные модели

    class Config:
        from_attributes = True


from src.db.tasks.schemas import TaskSchema
