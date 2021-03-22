from pydantic import BaseModel, validator


class Login(BaseModel):
    login: str
    password: str


class Token(BaseModel):
    token_type: str
    access_token: str

    @validator('token_type')
    def validate_token_type(cls, value):
        if value != 'Bearer':
            raise ValueError('Token type must be "Bearer"!')
        return value