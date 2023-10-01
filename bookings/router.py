from fastapi import APIRouter, Request, Depends
from sqlalchemy import select

from bookings.models import Bookings
from bookings.schemas import SBooking
from bookings.services import BookingService
from database import async_session_maker
from users.dependencies import get_current_user
from users.models import Users

router = APIRouter(
    prefix="/bookings",
    tags=["Бронирования"],
)


# @router.get("")
# async def get_bookings(request: Request):
#     print(request.cookies)
#     print(request.url)
#     print(request.client)


@router.get("")
async def get_bookings(user: Users = Depends(get_current_user)):
    return await BookingService.find_all(user_id=user.id)
