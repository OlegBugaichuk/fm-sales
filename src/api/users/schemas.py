from pydantic import BaseModel, Field


class UserBase(BaseModel):
    id: int
    login: str
    name: str
    surname: str


class UserInDb(UserBase):
    password: str = Field(alias='pass')


class User(UserBase):
    pass