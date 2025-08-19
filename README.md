📧 Mail Scheduler

A Django-based automated email scheduling system with support for hourly, daily, weekly, and monthly email jobs.
Built with Celery and Redis/RabbitMQ as the task queue, and integrated with Django’s email backend for reliable email delivery.

🚀 Features

✅ Schedule emails on hourly, daily, weekly, and monthly basis

✅ Background task management using Celery

✅ Flexible scheduling with cron-like syntax

✅ Easy email content management via Django Admin

✅ Supports multiple recipients & rich text content

✅ Error tracking & retries for failed email jobs

🛠️ Tech Stack

Backend: Django

Task Queue: Celery + Redis/RabbitMQ

Scheduler: django-cron / Celery Beat

Database: PostgreSQL / SQLite

Email: Django Email Backend (SMTP / Gmail / Custom)

📂 Project Structure
mailscheduler/
│── mailscheduler/       # Django project settings
│── mailer/           # App for managing scheduled emails
│   │── models.py        # Email models (Hourly, Daily, Weekly, Monthly)
│   │── tasks.py         # Celery tasks for email sending
│   │── cron.py          # Cron job setup
│   │── views.py         # (Optional) API for managing schedules
│── requirements.txt     # Dependencies
│── celery.py            # Celery configuration
│── Dockerfile           # Container setup (optional)

⚡ Setup & Run

Clone the repo

git clone https://github.com/nav380/mailscheduler.git
cd mailscheduler


Create virtual environment & install requirements

pip install -r requirement.txt


Run migrations & start Django

python manage.py migrate
python manage.py runserver


Start Celery worker & beat

celery -A mailscheduler worker -l info
celery -A mailscheduler beat -l info


Configure SMTP settings in settings.py

Now, emails will be sent automatically as per the defined schedule 🚀