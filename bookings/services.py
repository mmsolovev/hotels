from datetime import date

from sqlalchemy import and_, or_, select, func

import bookings
from bookings.models import Bookings
from database import engine, async_session_maker
from rooms.models import Rooms
from services.base import BaseService


class BookingService(BaseService):
    model = Bookings

    @classmethod
    async def add(cls,
                  user_id: int,
                  room_id: int,
                  date_from: date,
                  date_to: date,
    ):

        async with async_session_maker() as session:
            booked_rooms = select(Bookings).where(
                and_(
                    Bookings.room_id == 1,
                    or_(
                        and_(
                            Bookings.date_from >= date_from,
                            Bookings.date_from <= date_to,
                        ),
                        and_(
                            Bookings.date_from <= date_from,
                            Bookings.date_to > date_from,
                        ),
                    )
                )
            ).cte("booked_rooms")

            rooms_left = select(
                Rooms.quantity - func.count(booked_rooms.c.room_id).label("rooms_left")
                ).select_from(Rooms).join(
                booked_rooms, booked_rooms.c.room_id == Rooms.id
                ).where(Rooms.id == 1).group_by(
                Rooms.quantity, booked_rooms.c.room_id
            )

            print(rooms_left.compile(engine, compile_kwargs={"literal_binds": True}))\

            rooms_left = await session.execute(rooms_left)
            print(rooms_left.scalar())

