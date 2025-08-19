import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "emailscheduler.settings")

app = Celery("emailscheduler")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()

# Periodic Task Schedule
app.conf.beat_schedule = {
    "send-scheduled-emails-every-minute": {
        "task": "mailer.tasks.send_scheduled_emails",
        "schedule": crontab(minute="*"),  # every minute
    },
}
