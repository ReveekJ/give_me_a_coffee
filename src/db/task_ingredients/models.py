from sqlalchemy import BigInteger, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from src.db_connect import Base


class FoodOrderDescription(Base):
    __tablename__ = 'task_ingredients'

    task_id: Mapped[BigInteger] = mapped_column(ForeignKey('tasks.id', ondelete='CASCADE'), type_=BigInteger,
                                                primary_key=True)
    ingredient_id: Mapped[BigInteger] = mapped_column(ForeignKey('ingredients.id', ondelete='CASCADE'), type_=BigInteger,
                                                primary_key=True)
