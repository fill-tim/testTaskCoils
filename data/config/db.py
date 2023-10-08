from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import OperationalError
from fastapi import HTTPException
import os
from dotenv import load_dotenv

load_dotenv()

SERVER_NAME = os.getenv("SERVER_NAME")
DB_USERNAME = os.getenv("DB_USERNAME")
PASSWORD = os.getenv("PASSWORD")
PORT = os.getenv("PORT")
DB_NAME = os.getenv("DB_NAME")

SQLALCHEMY_DATABASE_URL = f"{SERVER_NAME}://{DB_USERNAME}:{PASSWORD}@localhost:{PORT}/{DB_NAME}"
print(SQLALCHEMY_DATABASE_URL)
engine = create_async_engine(SQLALCHEMY_DATABASE_URL, echo=True)
async_session = sessionmaker(engine, class_=AsyncSession)
Base = declarative_base()


def check_db():
    try:
        db = async_session()
        return db
    except OperationalError as e:
        raise HTTPException(status_code=503, detail=str(e))
    finally:
        db.close()
