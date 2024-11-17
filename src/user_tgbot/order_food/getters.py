from cgi import dolog

from aiogram.types import User
from aiogram_dialog import DialogManager, ShowMode

from src.db.menu.crud import FoodDB
from src.user_tgbot.order_food.schemas import OrderFoodData
from src.utils.aiogram_dialogs_utils import get_dialog_data_dto
from src.utils.order_food_utils import get_text_of_order


async def food_getter(event_from_user: User, dialog_manager: DialogManager, **kwargs):
    dialog_data: OrderFoodData = get_dialog_data_dto(dialog_manager)

    foods = FoodDB.get_foods_by_organization_id(dialog_data.organization_id)

    return {'food_list': [(i.id, i.name) for i in foods]}


async def ingredients_getter(event_from_user: User, dialog_manager: DialogManager, **kwargs):
    dialog_data: OrderFoodData = get_dialog_data_dto(dialog_manager)
    food = FoodDB.get_food_by_id(dialog_data.food_id)

    return {'ingredients': [(i.id, i.name) for i in food.possible_ingredients]}



async def order_description_getter(event_from_user: User, dialog_manager: DialogManager, **kwargs):
    dialog_data: OrderFoodData = get_dialog_data_dto(dialog_manager)
    return {'order_description': get_text_of_order(dialog_data)}
