from typing import Optional

from pydantic import BaseModel

from src.db.menu.schemas import FoodSchema, IngredientSchema


class TaskSchema(BaseModel):
    id: Optional[int] = None
    organization_id: int
    location_id: int
    worker_id: Optional[int] = None
    food_id: int

    #  эти элементы будут существовать, если их взять из бд
    food: Optional["FoodSchema"] = []
    ingredients: Optional[list["IngredientSchema"]] = []

    class Config:
        from_attributes = True


# проверить работу create_task