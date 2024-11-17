from src.db.task_ingredients.models import FoodOrderDescription
from src.db_connect import get_session


class TaskIngredientsDB:
    @staticmethod
    def create_link_task_ingredients(task_id: int, ingredient_ids: list[int]):
        with get_session() as session:
            for ingredient_id in ingredient_ids:
                m = FoodOrderDescription(
                    task_id=task_id,
                    ingredient_id=ingredient_id,
                )
                session.add(m)
                session.commit()

