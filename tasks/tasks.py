from tasks.celery import celery
from PIL import Image
from pathlib import Path

@celery.task
def process_pic(
        path: str,
):
    im_path = Path(path)
    im = Image.open(path)
    im_resized_1000 = im.resize((1000,1000))
    im_resized_100 = im.resize((100, 100))
    im_resized_1000.save(f"static/images/resized_1000_{im_path.name}")
    im_resized_100.save(f"static/images/resized_100_{im_path.name}")