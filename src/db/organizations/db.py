import asyncio
from datetime import datetime
from pprint import pprint

from sqlalchemy import select
from sqlalchemy.orm import selectinload, joinedload

from src.db.organizations.models import OrganizationModel
from src.db.organizations.schemas import OrganizationSchema
from src.db.owners.models import OwnerModel
from src.db_connect import get_async_session



class OrganizationDB:
    @staticmethod
    async def get_organization_by_id(_id: int) -> OrganizationSchema:
        async with await get_async_session() as session:
            query = (select(OrganizationModel)
                     .options(
                selectinload(OrganizationModel.workers),
                joinedload(OrganizationModel.owner),
                selectinload(OrganizationModel.tasks),
                selectinload(OrganizationModel.menu),

                    )
                     .filter(OrganizationModel.id == _id)
                     )
            res = (await session.execute(query)).scalars().first()
            # pprint(res.owner.__dict__)

            return OrganizationSchema.model_validate(res, from_attributes=True)



async def test():
    res = await OrganizationDB.get_organization_by_id(1)
    print(res)



asyncio.run(test())
