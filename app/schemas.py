from typing import Optional
from pydantic import BaseModel, EmailStr
from pydantic.types import conint
from datetime import datetime


class CreateUser(BaseModel):
    email: EmailStr
    password: str

class ResponseUser(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        orm_mode = True

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True

class CreatePost(PostBase):
    pass

class ResponsePost(PostBase):
    id: int
    created_at: datetime
    owner_id: int
    owner: ResponseUser

    class Config:
        orm_mode = True

class Post(BaseModel):
    content: str
    title: str
    owner_id: int
    id: int
    published: bool = True
    created_at: datetime

    class Config:
        orm_mode = True

class PostOut(BaseModel):
    Post: Post
    votes: int

    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[str] = None

class Vote(BaseModel):
    post_id: int
    dir: conint(le=1)
