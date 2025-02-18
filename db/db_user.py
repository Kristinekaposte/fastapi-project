#ORM functionality
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
    # Handle any exceptions here
    return db.query(DbUser).filter(DbUser.id == id).first() # filters output based on id

def update_user(db: Session, id: int, request: UserBase):
    user = db.query(DbUser).filter(DbUser.id == id)
    # Handle any exceptions here
    user.update({
        DbUser.username: request.username,
        DbUser.email: request.email,
        DbUser.password: Hash.bcrypt(request.password)
    })
    db.commit()
    return "updated"

def delete_user(db: Session, id: int):
    user = db.query(DbUser).filter(DbUser.id == id).first()
    # Handle any exceptions here
    db.delete(user)
    db.commit()
    return "deleted"
