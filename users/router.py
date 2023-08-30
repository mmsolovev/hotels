from fastapi import APIRouter, HTTPException

from users.auth import get_password_hash
from users.schemas import SUserRegister
from users.services import UsersService

router = APIRouter(
    prefix='/auth',
    tags=['Пользователи'],
)


@router.post('/register')
async def user_register(user_data: SUserRegister):
    existing_user = await UsersService.find_one_or_none(email=user_data.email)
    if existing_user:
        raise HTTPException(status_code=500)
    hashed_password = get_password_hash(user_data.password)
    await UsersService.add(email=user_data.email, hashed_password=hashed_password)
