from aiogram.enums import ContentType
from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.kbd import Button, SwitchTo, Select, Group, Back, Multiselect, Cancel
from aiogram_dialog.widgets.media import DynamicMedia
from aiogram_dialog.widgets.text import Format, Multi

from src.admin_tgbot.edit_organization.getters import workers_getter, add_workers_getter, actions_with_worker_getter, \
    foods_getter, ingredients_getter, qr_code_getter, locations_getter, all_ingrediens_getter, ingredient_name_getter
from src.admin_tgbot.edit_organization.handlers import on_start_main_dialog, select_worker_handler, \
    delete_selected_worker, back_to_organizations, on_start_edit_menu_dialog, select_food, \
    back_to_main_menu_of_edit_organization, go_to_edit_menu, save_name_of_food, save_name_of_ingredient, \
    process_ingredient_select, delete_food_handler, select_location, on_start_location_dialog, delete_location, \
    save_name_of_new_location, select_location_from_generate_qr, go_to_edit_locations, on_start_ingredient_dialog, \
    select_ingredient, go_to_edit_ingredient, new_ingredient_name_input_handler, delete_ingredient_handler, \
    save_name_of_new_ingredient_in_ingredient_dialog
from src.admin_tgbot.edit_organization.states import MainMenuSG, EditMenuSG, LocationSG, IngredientSG


edit_organization_dialog = Dialog(
    Window(
        # TODO: добавить название организации
        Format('Основное меню'),
        SwitchTo(
            Format('Изменить работников'),
            id='change_workers',
            state=MainMenuSG.list_of_workers
        ),
        Button(
            text=Format('Изменить меню'),
            id='go_to_edit_menu',
            on_click=go_to_edit_menu
        ),
        Button(
            text=Format('Изменить ингредиенты'),
            id='go_to_edit_ingredient',
            on_click=go_to_edit_ingredient,
        ),
        Button(
            text=Format('Изменить локации'),
            id='edit_locations',
            on_click=go_to_edit_locations
        ),
        SwitchTo(
            text=Format('Сгенерировать QR'),
            id='generate_qr',
            state=MainMenuSG.select_location_for_generate_qr
        ),
        Button(
            text=Format('Назад'),
            id='back_to_organizations',
            on_click=back_to_organizations
        ),
        state=MainMenuSG.main_menu
    ),
    Window(
        Format('Здесь вы можете изменить работников организации'),
        Group(
            Select(
                Format('{item[1]}'),
                id='workers_list',
                item_id_getter=lambda item: item[0],
                items='workers',
                on_click=select_worker_handler,
            ),
            width=1
        ),
        SwitchTo(
            text=Format('Добавить работников'),
            id='switch_to_add_workers',
            state=MainMenuSG.add_workers
        ),
        Back(
            text=Format('Назад')
        ),
        getter=workers_getter,
        state=MainMenuSG.list_of_workers
    ),
    Window(
        Multi(
            Format('Отправьте эту ссылку вашим работникам и они присоединятся к вашей организации\n\n'),
            Format('{link}'),
        ),
        Back(
            text=Format('Назад')
        ),
        getter=add_workers_getter,
        state=MainMenuSG.add_workers
    ),
    Window(
        Multi(
            Format('Ты изменяешь работника:\n\n'),
            Format('{worker_name}')
        ),
        Button(
            text=Format('Удалить из организации'),
            id='delete_from_organization',
            on_click=delete_selected_worker,
        ),
        SwitchTo(
            text=Format('Назад'),
            id='switch_to_list_of_workers',
            state=MainMenuSG.list_of_workers
        ),
        getter=actions_with_worker_getter,
        state=MainMenuSG.actions_with_worker
    ),
    Window(
        Multi(
            Format('Выбери локацию')
        ),
        Group(
            Select(
                Format('{item[1]}'),
                id='locations_list',
                item_id_getter=lambda item: item[0],
                items='locations',
                on_click=select_location_from_generate_qr,
            ),
            width=2
        ),
        SwitchTo(
            text=Format('Назад'),
            id='back_from_locations',
            state=MainMenuSG.main_menu
        ),
        getter=locations_getter,
        state=MainMenuSG.select_location_for_generate_qr,
    ),
    Window(
        Multi(
            Format('Распечатай этот QR-код и прикрепи его в том месте, где находятся твои клиенты. А если тебе не нравится этот QR, то можешь сделать свой с помощью этой ссылки:\n\n'),
            Format('{link}')
        ),
        DynamicMedia('qr_code'),
        SwitchTo(
            text=Format('Назад'),
            id='back_to_reality',
            state=MainMenuSG.main_menu
        ),
        getter=qr_code_getter,
        state=MainMenuSG.generate_qr
    ),
    on_start=on_start_main_dialog
)


edit_menu_dialog = Dialog(
    Window(
        Multi(
            Format('Здесь ты можешь изменить блюда, которые есть у вас в меню')
            # TODO: добавить название организации
        ),
        Group(
            Select(
                Format('{item[1]}'),
                id='food_groups_list',
                item_id_getter=lambda item: item[0],
                items='food_groups',
                on_click=select_food,
            ),
            width=2
        ),
        SwitchTo(
            text=Format('Добавить блюдо в меню'),
            id='add_group',
            state=EditMenuSG.enter_name_of_food
        ),
        Button(
            text=Format('Назад'),
            id='back_to_edit_organization_dialog',
            on_click=back_to_main_menu_of_edit_organization
        ),
        getter=foods_getter,
        state=EditMenuSG.select_food
    ),
    Window(
        Multi(
            Format('Введи название нового блюда (можешь добавить эмодзи, это сделает интерфейс пользователей более красивым)')
        ),
        MessageInput(
            content_types=ContentType.TEXT,
            func=save_name_of_food
        ),
        SwitchTo(
            text=Format('Назад'),
            id='back',
            state=EditMenuSG.select_food
        ),
        state=EditMenuSG.enter_name_of_food
    ),
    Window(
        Multi(
            Format('Выбери действие, которое ты хочешь совершить')
        ),
        SwitchTo(
            text=Format('Изменить ингредиенты'),
            id='change_ingredients',
            state=EditMenuSG.select_ingredient
        ),
        SwitchTo(
            text=Format('Удалить блюдо'),
            id='delete_food',
            state=EditMenuSG.delete_food
        ),
        SwitchTo(
            text=Format('Назад'),
            id='bacK',
            state=EditMenuSG.select_food
        ),
        state=EditMenuSG.choose_action_with_food
    ),
    Window(
        Multi(
            Format('Выбери ингредиенты, которые может содержать это блюдо:\n\n') # TODO: добавить название блюда
        ),
        Group(
            Multiselect(
                checked_text=Format('[✅] {item[1]}'),
                unchecked_text=Format('[ ] {item[1]}'),
                id='ingredients_multiselect',
                item_id_getter=lambda x: x[0],
                items='ingredients',
                on_click=process_ingredient_select
            ),
            width=2
        ),  # TODO: добавить проверку на максимальное количество ингредиентов
        SwitchTo(
            id='add_ingredient',
            text=Format('Добавить ингредиент'),
            state=EditMenuSG.enter_name_of_ingredient
        ),
        SwitchTo(
            id='done_select_ingredients',
            text=Format('Готово'),
            state=EditMenuSG.select_food
        ),
        SwitchTo(
            text=Format('Назад'),
            id='switch_to_enter_name',
            state=EditMenuSG.choose_action_with_food  # TODO: сделать нормальное возвращение к enter_name
        ),
        getter=ingredients_getter,
        state=EditMenuSG.select_ingredient
    ),
    Window(
        Multi(
            Format('Введи название нового ингредиента')
        ),
        MessageInput(
            content_types=ContentType.TEXT,
            func=save_name_of_ingredient
        ),
        SwitchTo(
            text=Format('Назад'),
            id='back',
            state=EditMenuSG.select_ingredient
        ),
        state=EditMenuSG.enter_name_of_ingredient
    ),
    Window(
        Multi(
            Format('Ты уверен, что хочешь удалить это блюдо? Это действие невозможно отменить и оно применятся мгновенно')
        ),
        Button(
            text=Format('Да'),
            id='delete_pls',
            on_click=delete_food_handler
        ),
        SwitchTo(
            text=Format('Нет'),
            id='not_delete',
            state=EditMenuSG.select_food
        ),
        state=EditMenuSG.delete_food
    ),
    # Window(  # TODO: сделать окно подтверждения добавления еды, ингредиента
    #     state=
    # ),
    on_start=on_start_edit_menu_dialog
)
#  TODO: сделать окно изменения ингредиентов

ingredients_dialog = Dialog(
    Window(
        Multi(Format('Выбери ингредиент')),
        Group(
            Select(
                Format('{item[1]}'),
                id='ingredient_list',
                item_id_getter=lambda item: item[0],
                items='ingredients',
                on_click=select_ingredient,
            ),
            width=2
        ),
        SwitchTo(
            text=Format('Создать новый ингредиент'),
            id='create_new_ingredient',
            state=IngredientSG.enter_name_of_ingredient
        ),
        Button(
            Format('Назад'),
            id='back_from_ingredients',
            on_click=back_to_main_menu_of_edit_organization,
        ),
        getter=all_ingrediens_getter,
        state=IngredientSG.select_ingredient
    ),
    Window(
        Multi(
            Format('{ingredient_name}\n'),
            Format('Выбери действие с ингредиентом')
        ),
        SwitchTo(
            Format('Переименовать ингредиент'),
            id='rename_ingredient',
            state=IngredientSG.rename_ingredient,
        ),
        SwitchTo(
            Format('Удалить ингредиент'),
            id='delete_ingredient',
            state=IngredientSG.approve_delete_ingredient,
        ),
        SwitchTo(
            text=Format('Назад'),
            id='back',
            state=IngredientSG.select_ingredient,
        ),
        getter=ingredient_name_getter,
        state=IngredientSG.ingredient_options
    ),
    Window(
        Multi(
            Format('Введите новое название ингредиента')
        ),
        MessageInput(
            content_types=ContentType.TEXT,
            func=new_ingredient_name_input_handler,
        ),
        SwitchTo(
            text=Format('Назад'),
            id='_back_',
            state=IngredientSG.ingredient_options
        ),
        state=IngredientSG.rename_ingredient
    ),
    Window(
        Multi(
            Format('Вы уверены, что хотите удалить ингредиент {ingredient_name}')
        ),
        Button(
            text=Format('Удалить ингредиент'),
            id='delete_please',
            on_click=delete_ingredient_handler,
        ),
        SwitchTo(
            text=Format('Нет, не удалять'),
            id='no_delete_please',
            state=IngredientSG.ingredient_options
        ),
        getter=ingredient_name_getter,
        state=IngredientSG.approve_delete_ingredient
    ),
    Window(
        Multi(
            Format('Введи название нового ингредиента')
        ),
        MessageInput(
            content_types=ContentType.TEXT,
            func=save_name_of_new_ingredient_in_ingredient_dialog
        ),
        SwitchTo(
            text=Format('Назад'),
            id='back',
            state=IngredientSG.select_ingredient
        ),
        state=IngredientSG.enter_name_of_ingredient
    ),
    on_start=on_start_ingredient_dialog
)

location_dialog = Dialog(
    Window(
        Multi(
            Format('Выбери локацию')
        ),
        Group(
            Select(
                Format('{item[1]}'),
                id='locations_list',
                item_id_getter=lambda item: item[0],
                items='locations',
                on_click=select_location,
            ),
            width=2
        ),
        SwitchTo(
            text=Format('Создать локацию'),
            id='create_location',
            state=LocationSG.enter_name_of_new_location,
        ),
        Cancel(
            text=Format('Назад')
        ),
        getter=locations_getter,
        state=LocationSG.select_location,
    ),
    Window(
        Format('Введи имя новой локации. Оно будет видно только тебе и работникам твоей организации, так что оно должно быть максимально понятным, но не обязано быть красивым))'),
        MessageInput(
            content_types=ContentType.TEXT,
            func=save_name_of_new_location,
        ),
        Back(
            text=Format('Назад')
        ),
        state=LocationSG.enter_name_of_new_location
    ),
    Window(
        Multi(
            Format('Выбери действие с локацией')  # TODO: подписать локацию
        ),
        SwitchTo(
            text=Format('Удалить локацию'),
            id='switch_to_delete_location',
            state=LocationSG.delete_location
        ),
        SwitchTo(
            text=Format('Назад'),
            id='back_to_main_location_menu',
            state=LocationSG.select_location
        ),
        state=LocationSG.actions_with_location
    ),
    Window(
        Multi(
            Format('Ты уверен, что хочешь удалить локацию? Это действие невозможно отменить')  # TODO: подписать локацию
        ),
        Button(
            text=Format('Да, удалить'),
            id='delete_location',
            on_click=delete_location
        ),
        SwitchTo(
            text=Format('Отмена, не удалять'),
            id='no_delete',
            state=LocationSG.actions_with_location
        ),
        state=LocationSG.delete_location
    ),
    on_start=on_start_location_dialog
)
