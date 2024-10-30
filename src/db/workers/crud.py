from sqlalchemy import select, delete

from src.db.workers.models import WorkerModel
from src.db.workers.schemas import WorkerSchema
from src.db_connect import get_session


class OwnerDB:
    @staticmethod
    def get_owner_by_id(_id: int) -> WorkerSchema:
        with get_session() as session:
            query = (select(WorkerModel)
                     .where(WorkerModel.id == _id)
                     )
            res: WorkerModel = (session.execute(query)).scalars().first()

            return WorkerSchema.model_validate(res, from_attributes=True)

    @staticmethod
    def create_owner(worker: WorkerSchema) -> None:
        with get_session() as session:
            m = WorkerModel(**worker.model_dump(exclude={'id'}))
            session.add(m)

    @staticmethod
    def delete_owner(worker_id: int) -> None:
        with get_session() as session:
            stmt = delete(WorkerModel).where(WorkerModel.id == worker_id)
            session.execute(stmt)
            session.commit()
