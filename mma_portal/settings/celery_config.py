from celery.schedules import crontab
from django.conf import settings
from kombu import Queue

broker_url = settings.BROKER_URL
broker_transport_options = {
    'max_retries': 1,
    'interval_start': 0,
    'visibility_timeout': 86400,
}
imports = (
    'company.tasks',
)
timezone = 'Asia/Seoul'
task_queues = (
    Queue('default', routing_key='default'),
)
task_default_queue = 'default'
task_default_priority = 5


beat_schedule_company = {
    'task_company_crawl': {
        'task': 'company.tasks.company_crawler.task_company_crawl',
        'schedule': crontab(minute=0, hour=0),
    }
}

beat_schedule = dict()
beat_schedule.update(beat_schedule_company)
