from typing import Optional

from pydantic import BaseModel


class FoodSchema(BaseModel):
    id: Optional[int] = None
    name: str
    organization_id: int

    possible_ingredients: Optional[list["IngredientSchema"]] = []

    class Config:
        from_attributes = True


class IngredientSchema(BaseModel):
    id: Optional[int] = None
    name: str
    organization_id: int
    # foods: Optional[list["FoodSchema"]] = []

    class Config:
        from_attributes = True
