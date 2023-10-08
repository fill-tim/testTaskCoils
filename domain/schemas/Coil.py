from pydantic import BaseModel, Field


class CoilSchema(BaseModel):
    weight: float
    length: float


class CoilResponse(BaseModel):
    parameter: CoilSchema = Field(...)

