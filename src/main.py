from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from src.core.auth.routers import router as auth_routers
from api.users.routers import router as users_router


# app object.
app = FastAPI()

# include routers
app.include_router(auth_routers, prefix='/auth', tags=['auth'])
app.include_router(users_router, prefix='/users', tags=['users'])

# mount
app.mount('/static', StaticFiles(directory='static'), name='static')