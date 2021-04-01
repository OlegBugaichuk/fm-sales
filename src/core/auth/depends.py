from fastapi import Header, HTTPException, status, Depends
from pydantic import ValidationError
from fastapi.security import HTTPBasicCredentials, HTTPBearer
from .schemas import Token


security = HTTPBearer()

async def token_depend(credentials: HTTPBasicCredentials = Depends(security)) -> Token:
    exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    token = credentials.credentials

    try:
        token = Token(access_token=token, token_type=credentials.scheme)
    except ValidationError:
        raise exception
    return token