from celery import Celery

app = Celery(__name__)
app.config_from_object('sanupchae.settings.celery_config')
