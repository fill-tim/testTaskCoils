import json
from datetime import datetime

from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from data.repositories.CoilRepository import CoilRepository
from domain.schemas.Coil import CoilSchema
from services.abstract_repositories.AbsCoilService import AbstractCoilService
from services.helpers.date_convert import Date


class CoilService(AbstractCoilService, CoilRepository):

    async def create(self, coil: CoilSchema):
        try:
            created_coil_id = await self.try_create(coil)
            if created_coil_id:
                return {
                    "status": "success",
                    "data": {
                        "item": created_coil_id
                    }
                }
            else:
                return JSONResponse(content={
                    "status": "error",
                    "data": {
                        "items": "Не смогли создать катушку"
                    },
                }, status_code=400)

        except Exception as error:
            return JSONResponse(content={
                "status": "error",
                "data": {
                    "items": str(error)
                },
            }, status_code=400)

    async def get_all(self, from_date, to_date):
        try:
            from_date_int = await Date().convert_to_timestamp(from_date)
            to_date_int = await Date().convert_to_timestamp(to_date)

            coils = await self.try_get_all(from_date_int, to_date_int)
            if coils:
                response = [coil for coil in coils]
                return JSONResponse(content={
                    "status": "success",
                    "data": {
                        "items": jsonable_encoder(response)
                    },
                }, status_code=200)
            else:
                return JSONResponse(content={
                    "status": "error",
                    "data": {
                        "items": "Не удалось найти катушки"
                    },
                }, status_code=404)

        except Exception as error:
            return JSONResponse(content={
                "status": "error",
                "data": {
                    "items": str(error)
                },
            }, status_code=400)

    async def delete(self, coil_id):
        try:
            delete_coil = await self.try_delete(coil_id)
            if delete_coil == 'success':
                return JSONResponse(content={
                    "status": "success",
                    "data": {
                        "items": "Удаление прошло успешно"
                    },
                }, status_code=200)
            else:
                return JSONResponse(content={
                    "status": "error",
                    "data": {
                        "items": f"Катушка с id - {coil_id} не найдена!"
                    },
                }, status_code=404)
        except Exception as error:
            return JSONResponse(content={
                "status": "error",
                "data": {
                    "items": str(error)
                },
            }, status_code=400)

    async def get_stats(self, from_date, to_date):
        try:
            from_date_int = await Date().convert_to_timestamp(from_date)
            to_date_int = await Date().convert_to_timestamp(to_date)

            coils_stats = await self.try_get_stats(from_date_int, to_date_int)

            if coils_stats:
                return JSONResponse(content={
                    "status": "success",
                    "data": {
                        "items": jsonable_encoder(coils_stats)
                    },
                }, status_code=200)
            else:
                return JSONResponse(content={
                    "status": "error",
                    "data": {
                        "items": "Не удалось найти катушки"
                    },
                }, status_code=404)
        except Exception as error:

            return JSONResponse(content={
                "status": "error",
                "data": {
                    "items": str(error)
                },
            }, status_code=400)
