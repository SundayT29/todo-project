from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session
from schemas import UserCreate
from services import user_email_exist, create_user, create_token
from database import get_db


router = APIRouter(
    prefix='/auth',
    tags=['Autentication']
)

@router.post('/signup', status_code=status.HTTP_201_CREATED)
async def create_new_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = await user_email_exist(db=db, email= user.email)
    if db_user:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail='User email already exist!!!')
    
    db_user = await create_user(user=user, db=db)
    access_token = await create_token(id=db_user.id, email=db_user.email, role=db_user.role)
    return access_token
    
