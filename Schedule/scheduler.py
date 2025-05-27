from apscheduler.schedulers.background import BackgroundScheduler
from django.core.mail import send_mail
from django.utils import timezone
from django.conf import settings
from .models import LessonReminder
from datetime import timedelta
import logging

logger = logging.getLogger(__name__)
scheduler = BackgroundScheduler()

def send_reminder_emails():
    # Adjust for 2-hour offset (server is 2 hours behind your local time)
    now = (timezone.localtime() + timedelta(hours=2)).replace(second=0, microsecond=0)

    targets = [
        now + timedelta(minutes=30),
        now + timedelta(minutes=10),
    ]

    for target_time in targets:
        reminders = LessonReminder.objects.filter(time=target_time)
        logger.info(f"Checking reminders for {target_time} — found: {reminders.values('lesson_name', 'teacher_name', 'email')}")

        for reminder in reminders:
            try:
                minutes_left = int((reminder.time - now).total_seconds() // 60)
                send_mail(
                    subject=f"Lesson Reminder: {reminder.lesson_name}",
                    message=f"Hi {reminder.teacher_name}, your lesson '{reminder.lesson_name}' starts in {minutes_left} minutes.",
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[reminder.email],
                    fail_silently=False,
                )
                logger.info(f"Sent {minutes_left}-minute reminder to {reminder.teacher_name} for {reminder.lesson_name}.")
            except Exception as e:
                logger.error(f"Failed to send email to {reminder.teacher_name}: {e}")

scheduler.add_job(send_reminder_emails, 'cron', minute='*')
