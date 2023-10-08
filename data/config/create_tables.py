from fastapi import APIRouter

from data.config.db import engine, Base

create_tables = APIRouter()


@create_tables.on_event("startup")
async def init_tables():
    async with engine.begin() as conn:
        pass
        # await conn.run_sync(Base.metadata.drop_all)
        # await conn.run_sync(Base.metadata.create_all)
