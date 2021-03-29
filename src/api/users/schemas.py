from pydantic import BaseModel, Field
from typing import List

class UserBase(BaseModel):
    id: int
    login: str
    name: str
    surname: str


class UserInDb(UserBase):
    password: str = Field(alias='pass')


class User(UserBase):
    pass


class UserPlan(BaseModel):
    level: int
    value: int


class UserStat(BaseModel):
    total_sales: int = 0
    bonus: int = 0
    premium: int = 0
    premium_percent: float = 0.0
    salary: int = 0
    total_salary: int = 0
    plans: List[UserPlan] = []