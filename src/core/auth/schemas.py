from pydantic import BaseModel, Field


class Login(BaseModel):
    login: str
    password: str


class User(BaseModel):
    id: int
    login: str
    password: str = Field(alias='pass')
    name: str
    surname: str


class Token(BaseModel):
    access_token: str
    token_type: str