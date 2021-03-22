import hashlib
from core.auth.schemas import Token
from jose import jwt
from core.settings import SECRET_KEY
from api.users.schemas import UserInDb

def get_password_hash(password: str) -> str:
    return hashlib.md5(('4y8N' + password + 'hW6R').encode('utf-8')).hexdigest()


def check_user_password(user: UserInDb, password: str) -> bool:
    hashed_password = get_password_hash(password)
    if hashed_password == user.password:
        return True
    return False


def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm='HS256')
    return encoded_jwt


def decode_access_token(token: Token) -> dict:
    payload = jwt.decode(token.access_token, SECRET_KEY, algorithms=['HS256'])
    return payload