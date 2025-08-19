from django.contrib import admin
from django.urls import path,include
from .views import schedule_email
urlpatterns = [
    path('email',schedule_email,name="email"),  # Include the mailer app URLs
    
]