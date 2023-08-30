from fastapi import APIRouter
from sqlalchemy import select

from bookings.models import Bookings
from bookings.schemas import SBooking
from bookings.services import BookingService
from database import async_session_maker

router = APIRouter(
    prefix="/bookings",
    tags=["Бронирования"],
)


@router.get("")
async def get_bookings() -> list[SBooking]:
    return await BookingService.find_all()


@router.get("/{booking_id}")
async def get_booking(booking_id):
    pass
