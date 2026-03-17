from workers.celery_worker import celery
from app.services.question_service import generate_questions

@celery.task
def generate_questions_task(role, level):
    return generate_questions(role, level)