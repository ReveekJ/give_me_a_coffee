import json

import redis.asyncio as redis
from pydantic import BaseModel


class TaskMessageSchema(BaseModel):
    chat_id: int
    message_id: int


class TaskMessagesRedis:
    def __init__(self):
        self.r = redis.Redis(host='redis', port=6379, db=0)

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.r.aclose()

    async def __aenter__(self):
        return await self.__connect()

    async def __connect(self):
        return self

    async def create_task_messages(self, task_id: int, messages_ids: list[TaskMessageSchema]):
        await self.r.set(str(task_id), json.dumps([i.model_dump() for i in messages_ids]))

    async def get_task_messages(self, task_id: int) -> list[TaskMessageSchema]:
        return [TaskMessageSchema.model_validate(i) for i in json.loads(await self.r.get(str(task_id)))]

    async def delete_task_messages(self, task_id: int) -> None:
        await self.r.delete(str(task_id))
