from src.db.menu.crud import IngredientsDB, FoodDB
from src.user_tgbot.order_food.schemas import OrderFoodData


class PrettyList(list):
    def __str__(self):
        res = ''
        for i in self:
            res += f'{i}\n'

        return res

    __repr__ = __str__



def get_text_of_order(data: OrderFoodData) -> str:
    food = FoodDB.get_food_by_id(data.food_id)
    ingredients = [IngredientsDB.get_ingredient_by_id(i) for i in data.ingredients_ids]

    return f'{food.name}\nДополнительные ингредиенты:\n{PrettyList(f"- {i.name}" for i in ingredients)}'

