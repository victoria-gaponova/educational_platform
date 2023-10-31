from rest_framework import generics
from rest_framework.generics import UpdateAPIView
from rest_framework.permissions import IsAuthenticated

from course.models import Lesson
from course.serializers.lesson import LessonSerializer


class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated]

class LessonListAPIView(generics.ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated]

class LessonRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated]

class LessonUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated]

class LessonDestroyAPIView(generics.DestroyAPIView):
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated]