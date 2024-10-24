from typing import List, Optional
from pydantic import BaseModel


class FoodSchema(BaseModel):
    id: int
    name: str
    food_group_id: int

    class Config:
        from_attributes = True


class FoodGroupSchema(BaseModel):
    id: int
    name: str
    organization_id: int
    food: Optional[List[FoodSchema]] = None  # Вложенные модели

    class Config:
        from_attributes = True
