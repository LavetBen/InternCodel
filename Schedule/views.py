from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import LessonReminder
from .serializer import LectureSerializer
from datetime import timedelta
from django.utils import timezone
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


@swagger_auto_schema(method='get', responses={200: LectureSerializer(many=True)})
@api_view(['GET'])
def list_lectures(request):
    """List all lecture reminders"""
    lectures = LessonReminder.objects.all()
    serializer = LectureSerializer(lectures, many=True)
    return Response(serializer.data)


@swagger_auto_schema(method='post', request_body=LectureSerializer, responses={201: LectureSerializer})
@api_view(['POST'])
def create_lecture(request):
    """Create a new lecture reminder"""
    serializer = LectureSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(method='put', request_body=LectureSerializer, responses={200: LectureSerializer})
@api_view(['PUT'])
def update_lecture(request, pk):
    """Update a lecture reminder by ID"""
    try:
        lecture = LessonReminder.objects.get(pk=pk)
    except LessonReminder.DoesNotExist:
        return Response({'error': 'Lecture not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = LectureSerializer(lecture, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(method='delete', responses={204: 'Lecture deleted'})
@api_view(['DELETE'])
def delete_lecture(request, pk):
    """Delete a lecture reminder by ID"""
    try:
        lecture = LessonReminder.objects.get(pk=pk)
    except LessonReminder.DoesNotExist:
        return Response({'error': 'Lecture not found'}, status=status.HTTP_404_NOT_FOUND)

    lecture.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


@swagger_auto_schema(method='get', responses={200: LectureSerializer(many=True)})
@api_view(['GET'])
def upcoming_reminders(request):
    """Get reminders 10 and 30 minutes before lectures"""
    now = timezone.localtime() + timedelta(hours=2)
    now = now.replace(second=0, microsecond=0)

    target_times = [now + timedelta(minutes=30), now + timedelta(minutes=10)]

    reminders = LessonReminder.objects.filter(time__in=target_times)
    serializer = LectureSerializer(reminders, many=True)

    return Response({
        "time": now,
        "reminders": serializer.data
    })
