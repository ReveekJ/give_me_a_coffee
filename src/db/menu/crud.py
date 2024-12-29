from sqlalchemy import select, delete, Sequence, update, values
from sqlalchemy.orm.base import state_str

from src.db.menu.models import FoodModel, IngredientModel
from src.db.menu.schemas import FoodSchema, IngredientSchema
from src.db_connect import get_session


class FoodDB:
    @staticmethod
    def get_food_by_id(_id: int) -> FoodSchema:
        with get_session() as session:
            query = (select(FoodModel)
                     .where(FoodModel.id == _id)
                     )
            res: FoodModel = (session.execute(query)).scalars().first()

            return FoodSchema.model_validate(res, from_attributes=True)

    @staticmethod
    def get_foods_by_organization_id(organization_id: int) -> list[FoodSchema]:
        with get_session() as session:
            query = (select(FoodModel).where(FoodModel.organization_id == organization_id))
            res: Sequence[FoodModel] = session.execute(query).scalars().all()

            return [FoodSchema.model_validate(i, from_attributes=True) for i in res]  # IDE хоть и ругается, но все работает

    @staticmethod
    def create_food(food_group: FoodSchema) -> int:
        with get_session() as session:
            m = FoodModel(**food_group.model_dump(exclude={'id'}))
            session.add(m)
            session.commit()

            return int(str(m.id))

    @staticmethod
    def delete_food(food_group_id: int) -> None:
        with get_session() as session:
            stmt = delete(FoodModel).where(FoodModel.id == food_group_id)
            session.execute(stmt)
            session.commit()


class IngredientsDB:
    @staticmethod
    def get_ingredient_by_id(_id: int) -> IngredientSchema:
        with get_session() as session:
            query = (select(IngredientModel)
                     .where(IngredientModel.id == _id)
                     )
            res: IngredientModel = (session.execute(query)).scalars().first()

            return IngredientSchema.model_validate(res, from_attributes=True)

    @staticmethod
    def get_ingredients_by_organization_id(organization_id: int) -> list[IngredientSchema]:
        with get_session() as session:
            query = (select(IngredientModel).where(IngredientModel.organization_id == organization_id))
            res: Sequence[IngredientModel] = session.execute(query).scalars().all()

            return [IngredientSchema.model_validate(i, from_attributes=True) for i in res]  # IDE хоть и ругается, но все работает

    @staticmethod
    def update_name(ingredient_id: int, name: str) -> None:
        with get_session() as session:
            stmt = update(IngredientModel).where(IngredientModel.id == ingredient_id).values(name=name)
            session.execute(stmt)
            session.commit()

    @staticmethod
    def create_ingredient(ingredient: IngredientSchema) -> int:
        with get_session() as session:
            m = IngredientModel(**ingredient.model_dump(exclude={'id'}))
            session.add(m)
            session.commit()

            return int(str(m.id))

    @staticmethod
    def delete_ingredient(ingredient_id: int) -> None:
        with get_session() as session:
            stmt = delete(IngredientModel).where(IngredientModel.id == ingredient_id)
            session.execute(stmt)
            session.commit()
