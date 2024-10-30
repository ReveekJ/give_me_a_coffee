from typing import Optional

from sqlalchemy import BigInteger, ForeignKey
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.db_connect import Base


class FoodGroupModel(AsyncAttrs, Base):
    __tablename__ = "food_groups"

    id: Mapped[BigInteger] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    name: Mapped[str]
    organization_id: Mapped[BigInteger] = mapped_column(BigInteger, ForeignKey("organizations.id"))

    organization: Mapped["OrganizationModel"] = relationship(
        back_populates='menu',
        cascade='delete'
    )
    food: Mapped[Optional[list["FoodModel"]]] = relationship(
        back_populates='food_group',
        cascade='delete'
    )


class FoodModel(AsyncAttrs, Base):
    __tablename__ = 'food'

    id: Mapped[BigInteger] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    name: Mapped[str]
    food_group_id: Mapped[BigInteger] = mapped_column(BigInteger, ForeignKey("food_groups.id"))

    food_group: Mapped[FoodGroupModel] = relationship(
        back_populates='food',
        cascade='delete'
    )

    tasks: Mapped[Optional[list["TaskModel"]]] = relationship(
        back_populates='description',
        secondary='food_orders_description'
    )

from src.db.organizations.models import OrganizationModel
from src.db.tasks.models import TaskModel
