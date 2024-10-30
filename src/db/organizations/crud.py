from sqlalchemy import select, delete

from src.db.organizations.models import OrganizationModel
from src.db.organizations.schemas import OrganizationSchema
from src.db_connect import get_session


class OrganizationDB:
    @staticmethod
    def get_organization_by_id(_id: int) -> OrganizationSchema:
        with get_session() as session:
            query = (select(OrganizationModel)
                     .where(OrganizationModel.id == _id)
                     )
            res: OrganizationModel = (session.execute(query)).scalars().first()

            return OrganizationSchema.model_validate(res, from_attributes=True)

    @staticmethod
    def get_organization_by_owner_id(owner_id: int) -> list[OrganizationSchema]:
        with get_session() as session:
            query = (select(OrganizationModel).where(OrganizationModel.owner_id == owner_id))
            res: list[OrganizationModel] = (session.execute(query)).scalars().all()

            return [OrganizationSchema.model_validate(i, from_attributes=True) for i in res]

    @staticmethod
    def create_organization(organization: OrganizationSchema) -> int:
        with get_session() as session:
            m = OrganizationModel(**organization.model_dump(exclude={'id'}))
            session.add(m)
            return int(m.__dict__['id'])
            # session.commit()

    # @staticmethod
    # def update_organization(id_old: int, new_organization: OrganizationSchema) -> None:
    #     with get_session() as session:
    #         stmt = update(OrganizationModel).where(OrganizationModel.id == id_old).values(**new_organization.model_dump(exclude={'id'}))
    #         session.execute(stmt)
    #         session.commit()

    @staticmethod
    def delete_organization(organization_id: int) -> None:
        with get_session() as session:
            stmt = delete(OrganizationModel).where(OrganizationModel.id == organization_id)
            session.execute(stmt)
            session.commit()
