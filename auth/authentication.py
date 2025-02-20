from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm.session import Session
from db.database import get_db
from db import models
from db.hash import Hash
from auth import oauth2

router = APIRouter(
    tags=["authentication"]
)

@router.post("/token")  # this needs to be same as the tokenUrl="token" in oauth2.py
def get_token(request: OAuth2PasswordRequestForm = Depends(),db: Session = Depends(get_db)):
    user = db.query(models.DbUser).filter(models.DbUser.username == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid Credentials")
    if not Hash.verify(user.password, request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid Password")
    access_token = oauth2.create_access_token(data={"sub": user.username})
    return {
        "access_token": access_token,
        "token_type": "bearer",
        "user_id": user.id,
        "username": user.username
    }