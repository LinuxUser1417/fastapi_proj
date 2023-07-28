from pydantic import BaseModel, Field
from typing import Optional, List

class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True


class TokenData(BaseModel):
    email: Optional[str] = Field(None)

class Token(BaseModel):
    access_token: str
    token_type: str


class PostBase(BaseModel):
    content: str

class PostCreate(PostBase):
    pass

class Post(PostBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True
