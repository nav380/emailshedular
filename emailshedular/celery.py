import os
from celery import Celery
from celery.schedules import crontab

# Make sure project name matches your settings.py folder
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "emailshedular.settings")

app = Celery("emailshedular")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()

# Periodic Task Schedule
app.conf.beat_schedule = {
    "send-scheduled-emails-every-minute": {
        "task": "mailer.tasks.send_scheduled_emails",  # adjust app name here
        "schedule": crontab(minute="*"),  # every minute
    },
}
