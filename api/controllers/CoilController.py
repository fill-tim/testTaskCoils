from fastapi import APIRouter

from domain.schemas.Coil import CoilResponse
from services.repositories.CoilService import CoilService

coil_router = APIRouter()


@coil_router.get("/coil")
async def get_all(from_date, to_date):
    all_coils = await CoilService().get_all(from_date, to_date)
    return all_coils


@coil_router.delete("/coil/{coil_id}")
async def delete(coil_id: int):
    delete_coil = await CoilService().delete(coil_id)
    return delete_coil


@coil_router.post("/coil")
async def create(request: CoilResponse):
    created_coil = await CoilService().create(request.parameter)
    return created_coil


@coil_router.get("/coil/stats")
async def get_stats(from_date, to_date):
    stats = await CoilService().get_stats(from_date, to_date)
    return stats
