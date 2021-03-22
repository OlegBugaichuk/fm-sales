from fastapi import FastAPI
from src.core.db.base import engine
from src.core.auth.routers import router as auth_routers
from api.users.routers import router as users_router

from sqlalchemy import text


app = FastAPI()

app.include_router(auth_routers, prefix='/auth', tags=['auth'])
app.include_router(users_router, prefix='/users', tags=['users'])