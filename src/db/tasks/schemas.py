from typing import Optional

from pydantic import BaseModel

from src.db.menu.schemas import FoodSchema, IngredientSchema


class TaskSchema(BaseModel):
    id: Optional[int]
    organization_id: int
    worker_id: Optional[int] = None
    food_id: int

    food: "FoodSchema"
    ingredients: Optional[list["IngredientSchema"]] = []

    class Config:
        from_attributes = True
