# https://www.youtube.com/watch?v=THxCy-6EnQM

# This script defines a async task for celery to submit to rabbitmq
# make sure you have rabbitmq running on localhost first
# To test it, run "celery -A testCelery worker --loglevel=info" in this folder 
# then run python scripts that exes "my_background_task" function

###### For example #######

# (flask) seanwu@Seans-MacBook-Pro celery-test % python3
# Python 3.9.1 (default, Feb  3 2021, 07:38:02) 
# [Clang 12.0.0 (clang-1200.0.32.29)] on darwin
# Type "help", "copyright", "credits" or "license" for more information.
# >>> from testCelery import my_background_task
# >>> my_background_task.delay("Should")
# <AsyncResult: b62e8617-46f7-4a39-a179-3712e7b95b74>
# >>> 

# Then go to the console that runs celery: 

# [2021-04-04 02:18:31,005: INFO/ForkPoolWorker-2] Task 
# testCelery.my_background_task[b62e8617-46f7-4a39-a179-3712e7b95b74] 
# succeeded in 5.0012224660000015s: 'dluohS'

from celery import Celery
import time



celery = Celery('tasks', broker='amqp://localhost', backend='db+sqlite:///db.sqlite3')

@celery.task
def my_background_task(text):
    # some long running task here
    time.sleep(5)
    return text[::-1]





