from aiogram.fsm.state import StatesGroup, State


class MainMenuSG(StatesGroup):
    main_menu = State()
    list_of_workers = State()
    actions_with_worker = State()
    add_workers = State()
    generate_qr = State()


class EditMenuSG(StatesGroup):
    select_food = State()
    enter_name_of_food = State()
    choose_action_with_food = State()
    select_ingredient = State()
    enter_name_of_ingredient = State()
    delete_food = State()
