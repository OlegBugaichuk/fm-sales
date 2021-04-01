from sqlalchemy import text
from pydantic import parse_obj_as
from typing import List
from core.auth.schemas import Token
from core.auth.helpers import decode_access_token
from core.db.base import engine
from core.db.tables import tables
from .schemas import UserInDb, User, UserStat as UserStatSchema


def get_users_list() -> List[User] or None:
    with engine.connect() as connection:
        result = connection.execute(
            text(f'select * from {tables["users"]} where active=1')
        )
        try:
            users = parse_obj_as(List[User], result.fetchall())
            return users
        except Exception as e:
            print(e)
            return None


def get_user_by_login(login: str) -> UserInDb or None:
    
    with engine.connect() as connection:
        result = connection.execute(
            text(f'select * from {tables["users"]} where active=1 and login="{login}"')
        )
        try:
            user = UserInDb(**result.first())
            return user
        except Exception as e:
            return None
            

def get_user_by_id(user_id: int) -> User or None:
    with engine.connect() as connection:
        result = connection.execute(
            text(f'select * from {tables["users"]} where active=1 and id="{user_id}"')
        )
        try:
            user = User(**result.first())
            return user
        except Exception as e:
            return None


def get_current_user(token: Token) -> User:
    payload = decode_access_token(token)
    if payload:
        return get_user_by_id(payload.get('user_id', None))


def get_current_user_stat(token: Token, year, month) -> UserStatSchema:
    payload = decode_access_token(token)
    user_id = payload.get('user_id')
    stat = UserStat(user_id=user_id, year=year, month=month)
    return stat.get_stats()


class UserStat:
    
    def __init__(self, user_id, year, month):
        self.user_id = user_id
        self.year = year
        self.month = month

    def get_stats(self) -> UserStatSchema:
        stat = UserStatSchema(**{
            'plans': [
                {'level':1, 'value': 250000},
                {'level':2, 'value': 275000},
                {'level':3, 'value': 300000},
                {'level':4, 'value': 320000}
            ]
        })
        return stat
