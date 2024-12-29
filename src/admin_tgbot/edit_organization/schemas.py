from typing import Optional

from pydantic import BaseModel

from src.db.organizations.schemas import OrganizationSchema


class MainMenuData(BaseModel):
    organization_id: int
    selected_worker_id: Optional[int] = None
    selected_location_for_qr: Optional[int] = None


class EditMenuData(BaseModel):
    organization_id: int
    selected_food_id: Optional[int] = None
    # selected_ingredients_ids: Optional[list[int]] = None


class LocationsData(BaseModel):
    organization_id: int
    selected_location: Optional[int] = None


class IngredientsData(BaseModel):
    organization_id: int
    selected_ingredient: Optional[int] = None
