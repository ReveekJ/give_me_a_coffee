from typing import Optional

from pydantic import BaseModel




class OrganizationSchema(BaseModel):
    id: Optional[int] = None
    name: str
    owner_id: int
    # owner: Optional["OwnerSchema"] = None
    workers: Optional[list["WorkerSchema"]] = []
    tasks: Optional[list["TaskSchema"]] = []
    foods: Optional[list["FoodSchema"]] = []
    ingredients: Optional[list["IngredientSchema"]] = []

    class Config:
        from_attributes = True


from src.db.tasks.schemas import TaskSchema
from src.db.workers.schemas import WorkerSchema
from src.db.menu.schemas import FoodSchema
from src.db.menu.schemas import IngredientSchema
