from fastapi import FastAPI

from api.controllers.CoilController import coil_router
from data.config.create_tables import create_tables

app = FastAPI()

app.include_router(create_tables)
app.include_router(coil_router)
