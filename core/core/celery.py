from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# broker='amqp://matin:12345678@music:8000/music/'

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

app = Celery('core')

app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()
