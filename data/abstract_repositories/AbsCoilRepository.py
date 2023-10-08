from abc import ABC, abstractmethod


class AbstractCoilRepository(ABC):
    @abstractmethod
    async def try_create(self, coil):
        raise NotImplementedError

    @abstractmethod
    async def try_get_all(self, from_date, to_date):
        raise NotImplementedError

    @abstractmethod
    async def try_delete(self, coil_id):
        raise NotImplementedError

    @abstractmethod
    async def try_get_stats(self, from_date, to_date):
        raise NotImplementedError


