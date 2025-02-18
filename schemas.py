# scema definition for the database
# will get info from api and then store it in the database
from typing import List

from pydantic import BaseModel

# Article inside UserDisplay
class Article(BaseModel):
    title: str
    content: str
    published: bool
    class Config:
        from_attributes = True

class UserBase(BaseModel):
    username: str
    email: str
    password: str

# class UserDisplay(BaseModel):
#     username: str
#     email: str
#     items: List[Article] = []
#     class Config:
#         from_attributes = True  # this will allow us to get the data from the database and display it in the api

class UserDisplay(BaseModel):
    username: str
    email: str
    items: List[Article]

    def __init__(self, **data):
        super().__init__(**data)
        if 'items' not in data:
            self.items = []

    class Config:
        from_attributes = True


#User inside ArticleDisplay
class User(BaseModel):
    id: int
    username: str
    class Config:
        from_attributes = True

class ArticleBase(BaseModel):
    title: str
    content: str
    published: bool
    creator_id: int  # user_id

class ArticleDisplay(BaseModel):
    title: str
    content: str
    published: bool
    user: User
    class Config:
        from_attributes = True