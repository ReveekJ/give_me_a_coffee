from typing import Optional

from pydantic import BaseModel


class OrderFoodData(BaseModel):
    organization_id: int
    food_id: Optional[int] = None
    ingredients_ids: Optional[list[int]] = None
