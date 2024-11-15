from typing import Optional

from sqlalchemy import BigInteger, ForeignKey
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.db_connect import Base


class OrganizationModel(AsyncAttrs, Base):
    __tablename__ = "organizations"

    id: Mapped[BigInteger] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    name: Mapped[str]
    owner_id: Mapped[BigInteger] = mapped_column(BigInteger, ForeignKey("owners.id"))

    owner: Mapped["OwnerModel"] = relationship(
        back_populates='organizations',
        cascade='delete',
    )
    workers: Mapped[Optional[list["WorkerModel"]]] = relationship(
        back_populates='organization',
        cascade='delete'
    )
    tasks: Mapped[Optional[list["TaskModel"]]] = relationship(
        back_populates='organization',
        cascade='delete'
    )
    foods: Mapped[Optional[list["FoodModel"]]] = relationship(
        back_populates='organization',
        cascade='delete'
    )
    ingredients: Mapped[Optional[list["IngredientModel"]]] = relationship(
        back_populates='organization',
        cascade='delete'
    )


from src.db.workers.models import WorkerModel
from src.db.menu.models import FoodModel
from src.db.owners.models import OwnerModel
from src.db.tasks.models import TaskModel
from src.db.menu.models import IngredientModel
