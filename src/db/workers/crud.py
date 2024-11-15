from sqlalchemy import select, delete

from src.db.workers.models import WorkerModel
from src.db.workers.schemas import WorkerSchema
from src.db_connect import get_session


class WorkersDB:
    @staticmethod
    def get_worker_by_id(_id: int) -> WorkerSchema:
        with get_session() as session:
            query = (select(WorkerModel)
                     .where(WorkerModel.id == _id)
                     )
            res: WorkerModel = (session.execute(query)).scalars().first()

            return WorkerSchema.model_validate(res, from_attributes=True)

    @staticmethod
    def create_worker(worker: WorkerSchema) -> None:
        with get_session() as session:
            m = WorkerModel(**worker.model_dump())
            session.add(m)
            session.commit()

    @staticmethod
    def delete_worker(worker_id: int) -> None:
        with get_session() as session:
            stmt = delete(WorkerModel).where(WorkerModel.id == worker_id)
            session.execute(stmt)
            session.commit()
