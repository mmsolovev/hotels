from datetime import date

from fastapi import FastAPI, Query
from typing import Optional

from pydantic import BaseModel

app = FastAPI()


class SHotel(BaseModel):
    address: str
    name: str
    stars: int


@app.get('/hotels')
async def get_hotels(
        location: str,
        date_from: date,
        date_to: date,
        has_spa: Optional[bool] = None,
        stars: Optional[int] = Query(None, ge=1, le=5),
) -> list[SHotel]:
    hotels = [
        {"address": "ул. Строителей, д. 22",
         "name": "Super Resort",
         "stars": 5,
         },
    ]
    return hotels


class SBooking(BaseModel):
    room_id: int
    date_from: date
    date_to: date


@app.post('/bookings')
async def add_booking(booking: SBooking):
    pass
