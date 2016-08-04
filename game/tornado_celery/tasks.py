import os

import requests
import time
from celery import Celery


celery = Celery("tasks", broker="amqp://")
celery.conf.CELERY_RESULT_BACKEND = os.environ.get(
    'CELERY_RESULT_BACKEND', 'amqp')


@celery.task
def require_douban(url):
    time.sleep(3.0)
    r = requests.get(url)
    return r.text


@celery.task
def add(x, y):
    time.sleep(1.0)
    return x + y


if __name__ == "__main__":
    celery.start()
