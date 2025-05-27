# Lesson Reminder

Lesson Reminder is a Django-based web application designed to help users manage and get reminders for their lessons. It leverages **Django REST Framework** for building APIs, **django-apscheduler** for scheduling reminder jobs, and **django-cors-headers** to handle Cross-Origin Resource Sharing (CORS) for API access.

---

## Features

- Create, update, list, and delete lessons via REST API.
- Schedule lesson reminders automatically using APScheduler.
- CORS enabled to allow requests from different origins (e.g., frontend apps).
- Secure and scalable API backend with Django REST Framework.

---

## Tech Stack


- Django==5.2.1
- Django REST Framework
- django-apscheduler
- django-cors-headers
- SQLite (default database)

---

## Installation & Setup

### 1. Clone the repository

```bash
git clone  https://github.com/LavetBen/InternCodel
cd Scheduler
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

## APScheduler Usage
The project uses django-apscheduler to schedule jobs like sending lesson reminders. Scheduler settings can be found and customized in the Django settings file.

##CORS Configuration
Cross-Origin Resource Sharing is enabled using django-cors-headers to allow your frontend applications to consume the API without issues.