from django.db import models
from django.utils import timezone
import datetime

class ScheduledEmail(models.Model):
    subject = models.CharField(max_length=255)
    body = models.TextField()
    recipient_email = models.EmailField()

    
class hourlyEmail(models.Model):
    scheduled_time = models.TimeField(default=datetime.time(9, 0))
    scheduled_email = models.ForeignKey(ScheduledEmail, on_delete=models.CASCADE, related_name='hourly_email')
    sent_time = models.DateTimeField(auto_now_add=True)    

class dailyEmail(models.Model):
    scheduled_time = models.TimeField(default=datetime.time(9, 0))
    scheduled_email = models.ForeignKey(ScheduledEmail, on_delete=models.CASCADE, related_name='daily_email')
    sent_time = models.DateTimeField(auto_now_add=True)
    
class weeklyEmail(models.Model):
    scheduled_day = models.CharField(max_length=10)  
    scheduled_time = models.TimeField(default=datetime.time(9, 0))
    scheduled_email = models.ForeignKey(ScheduledEmail, on_delete=models.CASCADE, related_name='weekly_email')
    sent_time = models.DateTimeField(auto_now_add=True)   

class monthlyEmail(models.Model):
    scheduled_day = models.IntegerField()  # Day of the month (1-31)
    scheduled_time = models.TimeField(default=datetime.time(9, 0))
    scheduled_email = models.ForeignKey(ScheduledEmail, on_delete=models.CASCADE, related_name='monthly_email')
    sent_time = models.DateTimeField(auto_now_add=True)     
    
class Emailsender(models.Model):
  is_sent= models.BooleanField(default=False)
  scheduled_email = models.ForeignKey(ScheduledEmail, on_delete=models.CASCADE, related_name='emailsender')
  sent_time = models.DateTimeField(auto_now_add=True)

  def __str__(self):
      return f"Email to {self.scheduled_email.recipient_email} at {self.sent_time}"     