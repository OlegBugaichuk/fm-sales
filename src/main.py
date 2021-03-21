from fastapi import FastAPI
from src.core.db.base import engine
from src.core.auth.routers import router

from sqlalchemy import text


app = FastAPI()

app.include_router(router, prefix='/auth', tags=['auth'])