from datetime import datetime

from sqlalchemy import select, update, func

from data.abstract_repositories.AbsCoilRepository import AbstractCoilRepository
from data.config.db import check_db
from domain.models.CoilModel import Coil


class CoilRepository(AbstractCoilRepository):

    async def try_create(self, coil):
        async with check_db() as session:
            coil_obj = Coil(length=coil.length, weight=coil.weight)
            session.add(coil_obj)
            await session.commit()
            await session.refresh(coil_obj)
            return coil_obj.id

    async def try_get_all(self, from_date_int, to_date_int):
        async with check_db() as session:
            stmt = select(Coil).where(Coil.created_at >= from_date_int, Coil.created_at <= to_date_int)
            response = await session.execute(stmt)
            res = [row[0] for row in response.all()]

            return res

    async def try_delete(self, coil_id):
        async with check_db() as session:
            coil = await session.get(Coil, coil_id)
            if coil is not None:
                stmt = update(Coil).where(Coil.id == coil_id).values(delete_at=int((datetime.utcnow()).timestamp()),
                                                                     is_active=False)
                await session.execute(stmt)
                await session.commit()
                return "success"
            else:
                return "error"

    async def try_get_stats(self, from_date_int, to_date_int):
        async with check_db() as session:
            async with session.begin():

                count = await session.execute(
                    select((func.count(Coil.id)), (func.avg(Coil.length)), (func.max(Coil.length)),
                           (func.min(Coil.length)), (func.max(Coil.weight)),
                           (func.sum(Coil.weight)))
                    .where(Coil.created_at >= from_date_int, Coil.created_at <= to_date_int))

                count_is_active = await session.execute(
                    select(func.count(Coil.id)).where((Coil.is_active == False), Coil.created_at >= from_date_int,
                                                      Coil.created_at <= to_date_int))

                count = count.all()

                response = {
                    "total_count": count[0][0],
                    "count_is_active": count_is_active.scalar(),
                    "count_avg_length": count[0][1],
                    "max_length": count[0][2],
                    "min_length": count[0][3],
                    "max_weight": count[0][4],
                    "sum_weight": count[0][5]
                }

            return response
