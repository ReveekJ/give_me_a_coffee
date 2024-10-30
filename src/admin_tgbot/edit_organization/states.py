from aiogram.fsm.state import StatesGroup, State


class MainMenuSG(StatesGroup):
    main_menu = State()
    list_of_workers = State()
    actions_with_worker = State()
    add_workers = State()
