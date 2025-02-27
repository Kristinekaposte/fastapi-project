#ORM functionality
from fastapi import HTTPException, status
from sqlalchemy.orm.session import Session

from db.hash import Hash
from db.models import DbUser
from schemas import UserBase


def create_user(db: Session, request: UserBase):
    new_user = DbUser(
        username = request.username,
        email = request.email,
        password = Hash.bcrypt(request.password)
    )
    db.add(new_user)
    db.commit() # sends operation to the database
    db.refresh(new_user) # will give id to our new user
    return new_user

def get_all_users(db: Session):
    return db.query(DbUser).all()

def get_user(db: Session, id: int):
    user = db.query(DbUser).filter(DbUser.id == id).first() # filters output based on id
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id {id} not found")
    return user

def get_user_by_username(db: Session, username: str):
    user = db.query(DbUser).filter(DbUser.username == username).first() # filters output based on username
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with username {username} not found")
    return user

def update_user(db: Session, id: int, request: UserBase):
    user = db.query(DbUser).filter(DbUser.id == id)
    if not user.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id {id} not found")
    user.update({
        DbUser.username: request.username,
        DbUser.email: request.email,
        DbUser.password: Hash.bcrypt(request.password)
    })
    db.commit()
    return "updated"

def delete_user(db: Session, id: int):
    user = db.query(DbUser).filter(DbUser.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id {id} not found")
    db.delete(user)
    db.commit()
    return "deleted"
