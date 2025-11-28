from celery import Celery

celery = Celery(
    'tasks',
    broker='redis://localhost',
    include=["tasks.tasks"]
)