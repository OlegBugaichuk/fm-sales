from sqlalchemy import text

from src.core.db.base import engine
from src.core.db.tables import tables
from .schemas import User

def get_user_by_login(login: str) -> User:
    
    with engine.connect() as connection:
        result = connection.execute(text(f'select * from {tables["users"]} where login="{login}"'))
        try:
            user = User(**result.first())
            return user
        except Exception as e:
            return None
            

def get_user_by_id(user_id: int) -> User:
    with engine.connect() as connection:
        result = connection.execute(text(f'select * from {tables["users"]} where id="{user_id}"'))
        try:
            user = User(**result.first())
            return user
        except Exception as e:
            return None