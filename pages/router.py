from fastapi import APIRouter
from fastapi.templating import Jinja2Templates


router = APIRouter(
    prefix='/pages',
    tags=['Frontend']
)

templates = Jinja2Templates(directory='templates')

@router.get('/hotels')
async def get_hotel_page(request: Request):
    return templates.TemplateResponse(name='hotels.html', context={'request': request})