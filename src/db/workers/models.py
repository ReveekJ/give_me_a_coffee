from typing import Optional

from sqlalchemy import BigInteger, ForeignKey
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.db_connect import Base



class WorkerModel(AsyncAttrs, Base):
    __tablename__ = "workers"

    id: Mapped[BigInteger] = mapped_column(BigInteger, primary_key=True)
    name: Mapped[Optional[str]]
    username: Mapped[Optional[str]]
    organization_id: Mapped[BigInteger] = mapped_column(BigInteger, ForeignKey("organizations.id"))

    organization: Mapped["OrganizationModel"] = relationship(
        back_populates='workers',
        cascade='delete'
    )
    tasks: Mapped[Optional[list["TaskModel"]]] = relationship(
        back_populates='worker',
        cascade='delete',
    )


from src.db.tasks.models import TaskModel
from src.db.organizations.models import OrganizationModel
