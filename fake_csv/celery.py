import os
from celery import Celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fake_csv.settings')

app = Celery('fake_csv')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()
