from sqlalchemy import select, delete

from src.db.tasks.models import TaskModel
from src.db.tasks.schemas import TaskSchema
from src.db_connect import get_session


class OwnerDB:
    @staticmethod
    def get_task_by_id(_id: int) -> TaskSchema:
        with get_session() as session:
            query = (select(TaskModel)
                     .where(TaskModel.id == _id)
                     )
            res: TaskModel = (session.execute(query)).scalars().first()

            return TaskSchema.model_validate(res, from_attributes=True)

    @staticmethod
    def get_tasks_by_organization(organization_id: int) -> list[TaskSchema]:
        with get_session() as session:
            query = (select(TaskModel).where(TaskModel.organization_id == organization_id))
            res = session.execute(query).scalars().all()

            return [TaskSchema.model_validate(i, from_attributes=True) for i in res]

    @staticmethod
    def get_tasks_by_worker(worker_id: int) -> list[TaskSchema]:
        with get_session() as session:
            query = (select(TaskModel).where(TaskModel.worker_id == worker_id))
            res = session.execute(query).scalars().all()

            return [TaskSchema.model_validate(i, from_attributes=True) for i in res]

    @staticmethod
    def create_task(task: TaskSchema) -> None:
        with get_session() as session:
            m = TaskModel(**task.model_dump(exclude={'id'}))
            session.add(m)

    @staticmethod
    def delete_task(worker_id: int) -> None:
        with get_session() as session:
            stmt = delete(TaskModel).where(TaskModel.id == worker_id)
            session.execute(stmt)
            session.commit()
