from datetime import datetime, timedelta
from fastapi import Depends
from sqlalchemy.orm import Session
from jose import JWTError, jwt
from passlib.context import CryptContext
from models import Users
from schemas import UserCreate, UserUpdate

bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')
SECRET_KEY = 'secret_key'
ALGORITHM = 'HS256'
TOKEN_EXPIRES_MINUTES = 30


async def user_email_exist(db: Session, email: str):
    db_user = db.query(Users).filter(Users.email == email).first()
    return db_user

async def create_user(db: Session, user: UserCreate):
    db_user = Users(
                    first_name = user.first_name,
                    last_name = user.last_name,
                    email = user.email,
                    bio = user.bio,
                    hashed_password = bcrypt_context.hash(user.password)
                )
    
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

async def create_token(id: int, email: str, role: str):
    encode = {'sub': email, 'id': id, 'role': role}
    expires = datetime.utcnow() + timedelta(minutes=TOKEN_EXPIRES_MINUTES)
    encode.update({'exp': expires})
    token = jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)
    return token
