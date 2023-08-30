from fastapi import APIRouter, HTTPException, status
from starlette.responses import Response

from users.auth import get_password_hash, user_auth, create_access_token
from users.schemas import SUserAuth
from users.services import UsersService

router = APIRouter(
    prefix='/auth',
    tags=['Пользователи'],
)


@router.post('/register')
async def user_register(user_data: SUserAuth):
    existing_user = await UsersService.find_one_or_none(email=user_data.email)
    if existing_user:
        raise HTTPException(status_code=500)
    hashed_password = get_password_hash(user_data.password)
    await UsersService.add(email=user_data.email, hashed_password=hashed_password)


@router.post('/login')
async def user_login(response: Response, user_data: SUserAuth):
    user = await user_auth(user_data.email, user_data.password)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    access_token = create_access_token({'sub': user.id})
    response.set_cookie('booking_access_token', access_token, httponly=True)
    return access_token
