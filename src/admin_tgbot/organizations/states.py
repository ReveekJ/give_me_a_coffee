from aiogram.fsm.state import StatesGroup, State


class OrganizationSG(StatesGroup):
    ask_name = State()