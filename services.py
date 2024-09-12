from fastapi import Depends
from database import get_db
from schemas import UserRequest
from sqlalchemy.orm import Session
from models import Users

# Autentication
# get User from database
def get_user(request: UserRequest, db: Session):
    user = db.query(Users).filter(Users.username == request.username).first()
    return user
