from sqlalchemy import delete, select

from src.db.possible_ingredients.models import PossibleIngredientsModel
from src.db_connect import get_session


class PossibleIngredientsDB:
    @staticmethod
    def create_link_ingredient_food(ingredient_id: int, food_id: int):
        with get_session() as session:
            m = PossibleIngredientsModel(food_id=food_id, ingredient_id=ingredient_id)
            session.add(m)
            session.commit()

    @staticmethod
    def delete_link_ingredient_food(ingredient_id: int, food_id: int):
        with get_session() as session:
            stmt = delete(PossibleIngredientsModel).where(PossibleIngredientsModel.food_id == food_id, PossibleIngredientsModel.ingredient_id == ingredient_id)
            session.execute(stmt)
            session.commit()

    @staticmethod
    def delete_link_by_food_id(food_id: int):
        with get_session() as session:
            stmt = delete(PossibleIngredientsModel).where(PossibleIngredientsModel.food_id == food_id)
            session.execute(stmt)
            session.commit()

    @staticmethod
    def get_possible_ingredients_by_food_id(food_id: int) -> list[int]:
        with get_session() as session:
            query = select(PossibleIngredientsModel).where(PossibleIngredientsModel.food_id == food_id)
            return [int(str(i.ingredient_id)) for i in session.execute(query).scalars().all()]
