from fastapi import APIRouter, HTTPException, Depends, status
from core.auth.depends import token_depend
from core.auth.schemas import Token
from .schemas import User
from .crud import get_current_user


router = APIRouter()


@router.get('/me', response_model=User)
async def me(token:Token = Depends(token_depend)) -> User:
    try:
        user = get_current_user(token)
    except Exception:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Check Token')
    return user