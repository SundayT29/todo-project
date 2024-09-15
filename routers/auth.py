from fastapi import APIRouter, Depends, status, HTTPException
from database import get_db
from schemas import UserRequest
from models import Users
from passlib.context import CryptContext
from services import get_user
from fastapi.security import OAuth2PasswordRequestForm


router = APIRouter(
    prefix='/auth',
    tags=['Autentication']
)

bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

@router.post('/create_user', status_code=status.HTTP_201_CREATED)
async def signup(request: UserRequest, db=Depends(get_db)):
    user = Users(
        first_name=request.first_name,
        last_name= request.last_name,
        username=request.username,
        password=bcrypt_context.hash(request.password)
    )

    user_exists = get_user(request=user, db=db)

    if user_exists:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Username Already Exist!")

    db.add(user)
    db.commit()
    db.refresh(user)
    return {'id': user.uuid, 'username': user.username, 'role': user.role}

@router.post('/token', status_code=status.HTTP_200_OK)
async def get_token():
    pass