from abc import ABC, abstractmethod

from domain.schemas.Coil import CoilSchema


class AbstractCoilService(ABC):

    @abstractmethod
    async def create(self, coil: CoilSchema):
        raise NotImplementedError

    @abstractmethod
    async def get_all(self, from_date, to_date):
        raise NotImplementedError

    @abstractmethod
    async def delete(self, coil_id):
        raise NotImplementedError

    @abstractmethod
    async def get_stats(self, from_date, to_date):
        raise NotImplementedError
