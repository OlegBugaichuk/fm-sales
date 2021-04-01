from fastapi import APIRouter, HTTPException, status
from api.users.crud import get_user_by_login
from .schemas import Login, Token
from .helpers import check_user_password, create_access_token

router = APIRouter()


@router.post('/login', response_model=Token)
async def login(login_info: Login):
    user = get_user_by_login(login_info.login)
    if user and check_user_password(user, login_info.password):
        return {
            'access_token': create_access_token({'user_id': user.id}), 
            'token_type': 'Bearer'
        }
    else:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail='Invalid login or password'
        )