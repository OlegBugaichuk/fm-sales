from sqlalchemy import text

from core.auth.schemas import Token
from core.auth.helpers import decode_access_token
from core.db.base import engine
from core.db.tables import tables
from .schemas import UserInDb, User

def get_user_by_login(login: str) -> UserInDb:
    
    with engine.connect() as connection:
        result = connection.execute(text(f'select * from {tables["users"]} where login="{login}"'))
        try:
            user = UserInDb(**result.first())
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


def get_current_user(token: Token) -> User:
    payload = decode_access_token(token)
    if payload:
        return get_user_by_id(payload.get('user_id', None))