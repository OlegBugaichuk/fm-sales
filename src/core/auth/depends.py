from fastapi import Header, HTTPException, status
from pydantic import ValidationError

from .schemas import Token

async def token_depend(Authorization: str = Header(...)) -> Token:
    exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    if not Authorization:
        raise exception

    token_info = Authorization.split(' ')

    try:
        token = Token(access_token= token_info[1], token_type=token_info[0])
    except ValidationError:
        raise exception
    return token