# Model definition
from sqlalchemy.orm import relationship

from db.database import Base
from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import Integer, String, Boolean
from sqlalchemy.sql.schema import ForeignKey


class DbUser(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    email = Column(String, unique=True)
    password = Column(String)
    items = relationship("DbArticle", back_populates="user") # this will create a relationship with the articles table

class DbArticle(Base):
    __tablename__ = "articles"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    content = Column(String)
    published = Column(Boolean)
    user_id = Column(Integer, ForeignKey("users.id")) # this will create a foreign key relationship with the users table
    user = relationship("DbUser", back_populates="items") # this will create a relationship with the users table