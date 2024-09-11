from fastapi import APIRouter

router = APIRouter(
    prefix='/auth',
    tags=['Autentication']
)

@router.post('/create_user')
async def create_user():
    return {'request': 'User Created'}
