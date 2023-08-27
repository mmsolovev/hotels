from datetime import date

from fastapi import FastAPI, Query, Depends
from typing import Optional

from pydantic import BaseModel

app = FastAPI()


# class SHotel(BaseModel):
#     address: str
#     name: str
#     stars: int


class HotelsSearchArgs:
    def __init__(
            self,
            location: str,
            date_from: date,
            date_to: date,
            has_spa: Optional[bool] = None,
            stars: Optional[int] = Query(None, ge=1, le=5),
    ):
        self.location = location
        self.date_from = date_from
        self.date_to = date_to
        self.has_spa = has_spa
        self.stars = stars


@app.get('/hotels')
async def get_hotels(
        search_args: HotelsSearchArgs = Depends()
):
    # hotels = [
    #     {"address": "ул. Строителей, д. 22",
    #      "name": "Super Resort",
    #      "stars": 5,
    #      },
    # ]
    return search_args


class SBooking(BaseModel):
    room_id: int
    date_from: date
    date_to: date


@app.post('/bookings')
async def add_booking(booking: SBooking):
    pass
