from datetime import date

from fastapi import FastAPI, Query
from typing import Optional

from pydantic import BaseModel

app = FastAPI()


@app.get('/hotels')
async def get_hotels(
        location: str,
        date_from: date,
        date_to: date,
        has_spa: Optional[bool] = None,
        stars: Optional[int] = Query(None, ge=1, le=5),
):
    return location, date_from, date_to, stars, has_spa


class SBooking(BaseModel):
    room_id: int
    date_from: date
    date_to: date


@app.post('/bookings')
async def add_booking(booking: SBooking):
    pass
