from database import TaskOrm, new_session
from sqlalchemy import select

async def add_task(data: dict) -> int:
    async with new_session() as session:
        new_task = TaskOrm(**data)
        session.add(new_task)
        await session.flush()
        await session.commit()
        return new_task.id

async def get_tasks():

    async with new_session() as session:
        query = select(TaskOrm)
        result = await session.execute(query)
        tasks_models = result.scalars().all()
        return tasks_models