from aiogram.fsm.state import StatesGroup, State


class OrganizationSG(StatesGroup):
    select_organization = State()
    ask_name = State()