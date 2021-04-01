from fastapi import APIRouter, HTTPException, Depends, status
from core.auth.depends import token_depend
from core.auth.schemas import Token
from typing import List
from .schemas import User
from .crud import get_current_user, get_users_list


router = APIRouter()


@router.get('/', response_model=List[User])
async def users_list(token:Token = Depends(token_depend)):
    try:
        users = get_users_list()
    except Exception:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Check Token')
    return users


@router.get('/me', response_model=User)
async def me(token:Token = Depends(token_depend)):
    try:
        user = get_current_user(token)
    except Exception:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Check Token')
    return user


