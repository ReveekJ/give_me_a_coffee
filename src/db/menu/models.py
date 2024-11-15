from typing import Optional

from sqlalchemy import BigInteger, ForeignKey
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.db_connect import Base


class FoodModel(AsyncAttrs, Base):
    __tablename__ = "foods"

    id: Mapped[BigInteger] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    name: Mapped[str]
    organization_id: Mapped[BigInteger] = mapped_column(BigInteger, ForeignKey("organizations.id"))

    organization: Mapped["OrganizationModel"] = relationship(
        back_populates='foods',
        cascade='delete'
    )
    possible_ingredients: Mapped[Optional[list["IngredientModel"]]] = relationship(
        back_populates='foods',
        secondary='possible_ingredients'
    )
    tasks: Mapped[Optional[list["TaskModel"]]] = relationship(
        back_populates='food',
    )


class IngredientModel(AsyncAttrs, Base):
    __tablename__ = 'ingredients'

    id: Mapped[BigInteger] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    name: Mapped[str]
    organization_id: Mapped[BigInteger] = mapped_column(BigInteger, ForeignKey("organizations.id"))

    organization: Mapped["OrganizationModel"] = relationship(
        back_populates='ingredients',
        cascade='delete'
    )

    foods: Mapped[Optional[list["FoodModel"]]] = relationship(
        back_populates='possible_ingredients',
        secondary='possible_ingredients'
    )

    tasks: Mapped[Optional[list["TaskModel"]]] = relationship(
        back_populates='ingredients',
        secondary='task_ingredients'
    )


from src.db.organizations.models import OrganizationModel
from src.db.tasks.models import TaskModel
