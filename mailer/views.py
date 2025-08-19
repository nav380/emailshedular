# views.py
from django.shortcuts import render, redirect
from .models import ScheduledEmail, hourlyEmail, dailyEmail, weeklyEmail, monthlyEmail
import datetime

def schedule_email(request):
    if request.method == "POST":
        subject = request.POST.get("subject")
        body = request.POST.get("body")
        recipient = request.POST.get("recipient")
        frequency = request.POST.get("frequency")

        # Save base email first
        scheduled_email = ScheduledEmail.objects.create(
            subject=subject,
            body=body,
            recipient_email=recipient
        )

        # Handle frequency-specific models
        if frequency == "hourly":
            time = request.POST.get("time")
            hourlyEmail.objects.create(
                scheduled_time=time,
                scheduled_email=scheduled_email
            )

        elif frequency == "daily":
            time = request.POST.get("time")
            dailyEmail.objects.create(
                scheduled_time=time,
                scheduled_email=scheduled_email
            )

        elif frequency == "weekly":
            day = request.POST.get("weekday")
            time = request.POST.get("time")
            weeklyEmail.objects.create(
                scheduled_day=day,
                scheduled_time=time,
                scheduled_email=scheduled_email
            )

        elif frequency == "monthly":
            day = request.POST.get("monthday")
            time = request.POST.get("time")
            monthlyEmail.objects.create(
                scheduled_day=day,
                scheduled_time=time,
                scheduled_email=scheduled_email
            )

        return redirect("email")  # reload after save

    return render(request, "email.html")
