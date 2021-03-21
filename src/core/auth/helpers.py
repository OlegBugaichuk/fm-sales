import hashlib
from jose import jwt
from core.settings import SECRET_KEY
from .schemas import User

def get_password_hash(password: str) -> str:
    return hashlib.md5(('4y8N' + password + 'hW6R').encode('utf-8')).hexdigest()


def check_user_password(user: User, password: str) -> bool:
    hashed_password = get_password_hash(password)
    if hashed_password == user.password:
        return True
    return False


def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm='HS256')
    return encoded_jwt

# def get_current_user()