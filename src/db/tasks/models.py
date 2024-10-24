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

    organization: Mapped["OrganizationModel"] = relationship(
        back_populates='tasks',
        cascade='delete'
    )
    worker: Mapped[Optional["WorkerModel"]] = relationship(
        back_populates='tasks',
        cascade='delete'
    )

    # TODO: добавить description
    # description: Mapped[list["OrganizationModel.menu"]] = relationship(
    #     back_populates=
    # )


from src.db.organizations.models import OrganizationModel
from src.db.workers.models import WorkerModel
