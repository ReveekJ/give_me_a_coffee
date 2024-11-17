from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.kbd import Select, Group, Multiselect, SwitchTo, Button
from aiogram_dialog.widgets.text import Multi, Format

from src.user_tgbot.order_food.getters import food_getter, ingredients_getter, order_description_getter
from src.user_tgbot.order_food.handlers import on_start_order_food_dialog, select_food_handler, \
    select_ingredients_handler, make_order_handler
from src.user_tgbot.order_food.states import OrderFoodSG

order_food_dialog = Dialog(
    Window(
        Multi(
            Format('Выбери блюдо/напиток')
        ),
        Group(
            Select(
                text=Format('{item[1]}'),
                id='food_selector',
                item_id_getter=lambda item: item[0],
                items='food_list',
                on_click=select_food_handler
            ),
            width=2
        ),
        getter=food_getter,
        state=OrderFoodSG.select_food
    ),
    Window(
        Multi(
            Format('Выбери ингредиенты, которые будут добавлены к этому блюду')
        ),
        Group(
            Multiselect(
                checked_text=Format('[✅] {item[1]}'),
                unchecked_text=Format('[ ] {item[1]}'),
                id='ingredients_multiselect',
                item_id_getter=lambda x: x[0],
                items='ingredients',
            ),
            width=2
        ),
        SwitchTo(
            text=Format('Готово'),
            id='done',
            on_click=select_ingredients_handler,
            state=OrderFoodSG.approve_food
        ),
        SwitchTo(
            text=Format('Назад'),
            id='back',
            state=OrderFoodSG.select_food
        ),
        getter=ingredients_getter,
        state=OrderFoodSG.select_ingredients
    ),
    Window(
        Multi(
            Format('Ваш заказ:\n'),
            Format('{order_description}')
        ),
        Button(
            text=Format('Заказать'),
            id='make_order',
            on_click=make_order_handler
        ),
        SwitchTo(
            text=Format('Вернуться к заказу'),
            id='nonono',
            state=OrderFoodSG.select_ingredients
        ),
        getter=order_description_getter,
        state=OrderFoodSG.approve_food
    ),
    # Window(
    #     Multi(
    #         Format('Заказ оформлен. Скоро к вам подойдет сотрудник и принесет {food_name}\n\n'),
    #         Format('Чтобы сделать еще один заказ, отсканируйте QR снова')
    #     ),
    #     getter=food_name_getter,
    #     state=OrderFoodSG.wait_please
    # ),
    on_start=on_start_order_food_dialog
)