from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import LessonReminder
from .serializer import LectureSerializer

@api_view(['GET'])
def list_lectures(request):
    lectures = LessonReminder.objects.all()
    serializer = LectureSerializer(lectures, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def create_lecture(request):
    serializer = LectureSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def update_lecture(request, pk):
    try:
        lecture = LessonReminder.objects.get(pk=pk)
    except LessonReminder.DoesNotExist:
        return Response({'error': 'Lecture not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = LectureSerializer(lecture, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_lecture(request, pk):
    try:
        lecture = LessonReminder.objects.get(pk=pk)
    except LessonReminder.DoesNotExist:
        return Response({'error': 'Lecture not found'}, status=status.HTTP_404_NOT_FOUND)

    lecture.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
