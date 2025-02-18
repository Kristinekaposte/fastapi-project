# scema definition for the database
# will get info from api and then store it in the database
from pydantic import BaseModel

class UserBase(BaseModel):
    username: str
    email: str
    password: str

class UserDisplay(BaseModel):
    username: str
    email: str

    class Config:
        from_attributes = True  # this will allow us to get the data from the database and display it in the api