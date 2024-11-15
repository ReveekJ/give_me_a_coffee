from typing import Optional

from sqlalchemy import BigInteger, ForeignKey
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.db_connect import Base


class TaskModel(AsyncAttrs, Base):
    __tablename__ = "tasks"

    id: Mapped[BigInteger] = mapped_column(BigInteger, primary_key=True, autoincrement=True)

    organization_id: Mapped[BigInteger] = mapped_column(BigInteger, ForeignKey("organizations.id"))
    worker_id: Mapped[Optional[BigInteger]] = mapped_column(BigInteger, ForeignKey("workers.id"))
    food_id: Mapped[BigInteger] = mapped_column(BigInteger, ForeignKey("foods.id"))

    organization: Mapped["OrganizationModel"] = relationship(
        back_populates='tasks',
        cascade='delete'
    )
    worker: Mapped[Optional["WorkerModel"]] = relationship(
        back_populates='tasks',
        cascade='delete'
    )

    food: Mapped["FoodModel"] = relationship(
        back_populates='tasks',
    )
    ingredients: Mapped[Optional[list["IngredientModel"]]] = relationship(
        back_populates='tasks',
        secondary='task_ingredients'
    )


from src.db.organizations.models import OrganizationModel
from src.db.workers.models import WorkerModel
from src.db.menu.models import IngredientModel
from src.db.menu.models import FoodModel
