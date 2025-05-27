from django.apps import AppConfig
import logging

logger = logging.getLogger(__name__)

class ScheduleConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Schedule'

    def ready(self):
        from .scheduler import scheduler
        scheduler.start()
        logger.info("Scheduler started successfully.")