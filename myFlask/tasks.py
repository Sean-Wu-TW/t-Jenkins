from app import celery

@celery.task
def my_background_task(text):
    # some long running task here
    time.sleep(5)
    return text[::-1]