from typing import Optional

from sqlalchemy import BigInteger
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.db_connect import Base


class OwnerModel(AsyncAttrs, Base):
    __tablename__ = "owners"

    id: Mapped[BigInteger] = mapped_column(BigInteger, primary_key=True)

    organizations: Mapped[Optional[list['OrganizationModel']]] = relationship(
        back_populates='owner',
        cascade='delete',
        lazy='selectin'
    )


from src.db.organizations.models import OrganizationModel
