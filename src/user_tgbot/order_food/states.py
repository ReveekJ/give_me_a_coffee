from aiogram.fsm.state import StatesGroup, State


class OrderFoodSG(StatesGroup):
    select_food = State()
    select_ingredients = State()
    approve_food = State()
    wait_please = State()