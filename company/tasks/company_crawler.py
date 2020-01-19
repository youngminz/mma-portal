from celery import shared_task


@shared_task
def task_company_crawl():
    print("42")
