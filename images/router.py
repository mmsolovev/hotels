from fastapi import APIRouter, UploadFile
import shutil

from sqlalchemy.orm import defer

from tasks.tasks import process_pic

router = APIRouter(
    prefix="/images",
    tags=["images"]
)

@router.post("/hotels")
async def add_hotel_image(name: int, file: UploadFile):
    im_path = f"static/images/{name}.webp"
    with open(im_path, "wb+") as file_object:
        shutil.copyfileobj(file.file, file_object)
    process_pic.delay(im_path)
