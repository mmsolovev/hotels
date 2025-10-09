from datetime import date

from fastapi import FastAPI, Query, Depends
from typing import Optional

from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from fastapi_cache.decorator import cache

from redis import asyncio as aioredis

from pydantic import BaseModel
from starlette.middleware.cors import CORSMiddleware

from bookings.router import router as router_bookings
from bookings.schemas import SBooking
from users.router import router as router_users

from pages.router import router as router_pages


@asynccontextmanager
async def lifespan(_: FastAPI) -> AsyncIterator[None]:
    redis = aioredis.from_url("redis://localhost")
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")
    yield


app = FastAPI(lifespan=lifespan)


@cache()
async def get_cache():
    return 1


app.include_router(router_users)
app.include_router(router_bookings)
app.include_router(router_pages)

origins = ['http://localhost:3000']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


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
@cache(expire=20)
async def get_hotels(search_args: HotelsSearchArgs = Depends()):
    return search_args


@app.post('/bookings')
async def add_booking(booking: SBooking):
    pass


@app.get("/")
@cache(expire=60)
async def index():
    return dict(hello="world")
