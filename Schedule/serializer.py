# serializers.py

from rest_framework import serializers
from .models import LessonReminder  # Replace with your actual model name

class LectureSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonReminder
        fields = ['id', 'teacher_name', 'lesson_name', 'email', 'time']
