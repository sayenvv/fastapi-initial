from pydantic import BaseModel,EmailStr
from typing import Union

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Union[str, None] = None


class User(BaseModel):
    username: str
    email: EmailStr
    full_name: Union[str, None] = None
    disabled: Union[bool, None] = None
    password: str


class UserInDB(User):
    hashed_password: str


class OurBaseModel(BaseModel):
    class Config:
        orm_mode = True


class UserResponseSchema(OurBaseModel):
    id :int
    username: str
    email: Union[str, None] = None
    full_name: Union[str, None] = None
    disabled: Union[bool, None] = None
    password: str