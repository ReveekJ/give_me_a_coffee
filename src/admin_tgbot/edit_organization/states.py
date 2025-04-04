from aiogram.fsm.state import StatesGroup, State


class MainMenuSG(StatesGroup):
    main_menu = State()
    list_of_workers = State()
    actions_with_worker = State()
    add_workers = State()
    select_location_for_generate_qr = State()
    generate_qr = State()


class EditMenuSG(StatesGroup):
    select_food = State()
    enter_name_of_food = State()
    choose_action_with_food = State()
    select_ingredient = State()
    enter_name_of_ingredient = State()
    delete_food = State()


class LocationSG(StatesGroup):
    select_location = State()
    enter_name_of_new_location = State()
    actions_with_location = State()
    delete_location = State()


class IngredientSG(StatesGroup):
    select_ingredient = State()
    # enter_name_of_new_ingredient = State()
    ingredient_options = State()
    rename_ingredient = State()
    approve_delete_ingredient = State()
    enter_name_of_ingredient = State()

