from sqlalchemy import BigInteger, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.db_connect import Base


class LocationModel(Base):
    __tablename__ = 'locations'

    id: Mapped[BigInteger] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    name: Mapped[str]
    organization_id: Mapped[BigInteger] = mapped_column(BigInteger, ForeignKey('organizations.id'), nullable=False)

    organization: Mapped["OrganizationModel"] = relationship(
        back_populates="locations",
    )


from src.db.organizations.models import OrganizationModel
