from sqlalchemy import select, delete

from src.db.owners.models import OwnerModel
from src.db.owners.schemas import OwnerSchema
from src.db_connect import get_session


class OwnerDB:
    @staticmethod
    def get_owner_by_id(_id: int) -> OwnerSchema:
        with get_session() as session:
            query = (select(OwnerModel)
                     .where(OwnerModel.id == _id)
                     )
            res: OwnerModel = (session.execute(query)).scalars().first()

            return OwnerSchema.model_validate(res, from_attributes=True)

    @staticmethod
    def create_owner(owner: OwnerSchema) -> None:
        with get_session() as session:
            m = OwnerModel(**owner.model_dump(exclude={'id'}))
            session.add(m)

    @staticmethod
    def delete_owner(owner_id: int) -> None:
        with get_session() as session:
            stmt = delete(OwnerModel).where(OwnerModel.id == owner_id)
            session.execute(stmt)
            session.commit()
