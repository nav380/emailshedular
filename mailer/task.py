import datetime
import logging
from celery import shared_task
from django.core.mail import send_mail
from .models import ScheduledEmail, hourlyEmail, dailyEmail, weeklyEmail, monthlyEmail

logger = logging.getLogger(__name__)

@shared_task
def send_scheduled_emails():
    """
    Celery task that runs periodically (every minute via celery beat).
    It checks scheduled emails in all frequency models and sends them.
    """
    now = datetime.datetime.now()
    current_time = now.time().replace(second=0, microsecond=0)
    current_day = now.strftime("%A")
    current_day_of_month = now.day

    logger.info("Checking scheduled emails at %s", now)

    # -------- Hourly Emails --------
    hourly = hourlyEmail.objects.filter(scheduled_time__hour=now.hour, scheduled_time__minute=now.minute)
    for h in hourly:
        _send_email(h.scheduled_email)

    # -------- Daily Emails --------
    daily = dailyEmail.objects.filter(scheduled_time__hour=now.hour, scheduled_time__minute=now.minute)
    for d in daily:
        _send_email(d.scheduled_email)

    # -------- Weekly Emails --------
    weekly = weeklyEmail.objects.filter(
        scheduled_day=current_day,
        scheduled_time__hour=now.hour,
        scheduled_time__minute=now.minute
    )
    for w in weekly:
        _send_email(w.scheduled_email)

    # -------- Monthly Emails --------
    monthly = monthlyEmail.objects.filter(
        scheduled_day=current_day_of_month,
        scheduled_time__hour=now.hour,
        scheduled_time__minute=now.minute
    )
    for m in monthly:
        _send_email(m.scheduled_email)


def _send_email(scheduled_email: ScheduledEmail):
    """Helper to send email + log result"""
    try:
        send_mail(
            subject=scheduled_email.subject,
            message=scheduled_email.body,
            from_email="noreply@example.com",
            recipient_list=[scheduled_email.recipient_email],
            fail_silently=False,
        )
        logger.info("✅ Email sent to %s (Subject: %s)", scheduled_email.recipient_email, scheduled_email.subject)
    except Exception as e:
        logger.error("❌ Failed to send email to %s. Error: %s", scheduled_email.recipient_email, str(e))
