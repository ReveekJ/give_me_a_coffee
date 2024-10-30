from sqlalchemy import BigInteger, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from src.db_connect import Base


class FoodOrderDescription(Base):
    __tablename__ = 'food_orders_description'

    task_id: Mapped[BigInteger] = mapped_column(ForeignKey('tasks.id', ondelete='CASCADE'), type_=BigInteger,
                                                primary_key=True)
    food_id: Mapped[BigInteger] = mapped_column(ForeignKey('food.id', ondelete='CASCADE'), type_=BigInteger,
                                                primary_key=True)
