from bookings.models import Bookings
from services.base import BaseService


class BookingService(BaseService):
    model = Bookings

