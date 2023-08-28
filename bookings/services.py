from sqlalchemy import select

from bookings.models import Bookings
from database import async_session_maker
from services.base import BaseService


class BookingService(BaseService):
    model = Bookings

