from django.db import models
from django.db import models

class LessonReminder(models.Model):
    teacher_name = models.CharField(max_length=100)
    lesson_name = models.CharField(max_length=100)
    email = models.EmailField()
    time = models.DateTimeField()

