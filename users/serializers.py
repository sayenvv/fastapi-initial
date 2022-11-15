from pydantic import BaseModel,EmailStr

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None


class User(BaseModel):
    username: str
    email: EmailStr
    full_name: str | None = None
    disabled: bool | None = None
    password: str


class UserInDB(User):
    hashed_password: str


class OurBaseModel(BaseModel):
    class Config:
        orm_mode = True


class UserResponseSchema(OurBaseModel):
    id :int
    username: str
    email: str | None = None
    full_name: str | None = None
    disabled: bool | None = None
    password: str