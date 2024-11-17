from sqlalchemy import select, delete

from src.db.locations.models import LocationModel
from src.db.locations.schemas import LocationSchema
from src.db_connect import get_session


class LocationsDB:
    @staticmethod
    def get_location_by_id(_id: int) -> LocationSchema:
        with get_session() as session:
            query = (select(LocationModel)
                     .where(LocationModel.id == _id)
                     )
            res: LocationModel = (session.execute(query)).scalars().first()

            return LocationSchema.model_validate(res, from_attributes=True)

    @staticmethod
    def get_locations_by_organization_id(organization_id: int) -> list[LocationSchema]:
        with get_session() as session:
            query = (select(LocationModel).where(LocationModel.organization_id == organization_id))
            res = session.execute(query).scalars().all()

            return [LocationSchema.model_validate(i, from_attributes=True) for i in res]

    @staticmethod
    def create_location(location: LocationSchema) -> None:
        with get_session() as session:
            m = LocationModel(**location.model_dump(exclude={'id'}))
            session.add(m)
            session.commit()

    @staticmethod
    def delete_location(location_id: int) -> None:
        with get_session() as session:
            stmt = delete(LocationModel).where(LocationModel.id == location_id)
            session.execute(stmt)
            session.commit()
