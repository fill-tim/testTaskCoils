from datetime import datetime
from sqlalchemy import Integer, Column, Numeric, Boolean
from data.config.db import Base


class Coil(Base):
    __tablename__ = 'coils'
    id = Column(Integer, primary_key=True, autoincrement=True)
    length = Column(Numeric, nullable=False)
    weight = Column(Numeric, nullable=False)
    created_at = Column(Integer, default=int((datetime.utcnow()).timestamp()))
    delete_at = Column(Integer, default=None)
    is_active = Column(Boolean, default=True)

    def dir(self):
        return {"id": self.id, "length": self.length, "weight": self.weight, "created_at": self.created_at,
                "deleted_at": self.delete_at}
