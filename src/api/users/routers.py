import datetime
from typing import List
from fastapi import APIRouter, HTTPException, Depends, status
from core.auth.depends import token_depend
from core.auth.schemas import Token
from .schemas import User, UserStat
from .crud import get_current_user, get_users_list, get_user_by_id, get_current_user_stat


router = APIRouter()


@router.get('/me', response_model=User)
async def me(token:Token = Depends(token_depend)):
    try:
        user = get_current_user(token)
    except Exception:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Check Token')
    return user


@router.get('/', response_model=List[User])
async def get_users(token: Token = Depends(token_depend)):
    users = get_users_list()
    return users


@router.get('/{user_id}', response_model=User)
async def get_users(user_id: int, token: Token = Depends(token_depend)):
    user = get_user_by_id(user_id)
    if user:
        return user
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User not found')


@router.get('/me/stats', response_model=UserStat)
async def get_current_user_stats(token: Token = Depends(token_depend), 
                  year: int = datetime.datetime.now().year, 
                  month: int = datetime.datetime.now().month):

    return get_current_user_stat(token, year, month)