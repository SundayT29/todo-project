from fastapi import APIRouter, status
from schemas import UserCreate
from models import Users
from passlib.context import CryptContext


router = APIRouter(
    prefix='/auth',
    tags=['Autentication']
)

bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

@router.post('/create_user', status_code=status.HTTP_200_OK)
async def signup(request: UserCreate):
    user = UserCreate(
        first_name=request.first_name,
        last_name= request.last_name,
        username=request.username,
        password=bcrypt_context.hash(request.password)
    )
    return user