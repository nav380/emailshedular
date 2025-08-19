from django.contrib import admin
from .models import ScheduledEmail, hourlyEmail, dailyEmail, weeklyEmail, monthlyEmail, Emailsender


@admin.register(ScheduledEmail)
class ScheduledEmailAdmin(admin.ModelAdmin):
    list_display = ('subject', 'recipient_email')
    search_fields = ('subject', 'recipient_email')


@admin.register(hourlyEmail)
class HourlyEmailAdmin(admin.ModelAdmin):
    list_display = ('scheduled_email', 'scheduled_time', 'sent_time')
    search_fields = ('scheduled_email__subject', 'scheduled_email__recipient_email')
    list_filter = ('scheduled_time',)


@admin.register(dailyEmail)
class DailyEmailAdmin(admin.ModelAdmin):
    list_display = ('scheduled_email', 'scheduled_time', 'sent_time')
    search_fields = ('scheduled_email__subject', 'scheduled_email__recipient_email')
    list_filter = ('scheduled_time',)


@admin.register(weeklyEmail)
class WeeklyEmailAdmin(admin.ModelAdmin):
    list_display = ('scheduled_email', 'scheduled_day', 'scheduled_time', 'sent_time')
    search_fields = ('scheduled_email__subject', 'scheduled_email__recipient_email')
    list_filter = ('scheduled_day', 'scheduled_time')


@admin.register(monthlyEmail)
class MonthlyEmailAdmin(admin.ModelAdmin):
    list_display = ('scheduled_email', 'scheduled_day', 'scheduled_time', 'sent_time')
    search_fields = ('scheduled_email__subject', 'scheduled_email__recipient_email')
    list_filter = ('scheduled_day', 'scheduled_time')


@admin.register(Emailsender)
class EmailSenderAdmin(admin.ModelAdmin):
    list_display = ('scheduled_email', 'is_sent', 'sent_time')
    search_fields = ('scheduled_email__subject', 'scheduled_email__recipient_email')
    list_filter = ('is_sent', 'sent_time')
