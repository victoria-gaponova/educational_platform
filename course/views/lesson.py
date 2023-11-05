from rest_framework import generics

from rest_framework.permissions import IsAuthenticated, IsAdminUser

from course.models import Lesson
from course.paginators.lesson import LessonPaginator
from course.permissions import IsOwner, IsModerator
from course.serializers.lesson import LessonSerializer


class LessonCreateAPIView(generics.CreateAPIView):
    """
        Представление для получения списка всех уроков.
        Attributes:
            serializer_class (LessonSerializer): Сериализатор, используемый для преобразования объектов уроков в JSON.
    """
    serializer_class = LessonSerializer
    permission_classes = [IsAdminUser]


class LessonListAPIView(generics.ListAPIView):
    """
        Представление для получения списка всех уроков.
        Attributes:
            serializer_class (LessonSerializer): Сериализатор, используемый для преобразования объектов уроков в JSON.
            queryset (QuerySet): Набор объектов уроков, используемых для построения списка.
            pagination_class (LessonPaginator): Пагинатор, для отображения уроков на странице.
        """
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = LessonPaginator


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    """
        Представление для получения списка всех уроков.
        Attributes:
            serializer_class (LessonSerializer): Сериализатор, используемый для преобразования объектов уроков в JSON.
            queryset (QuerySet): Набор объектов уроков, используемых для построения списка.
    """
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsOwner | IsAdminUser | IsModerator]


class LessonUpdateAPIView(generics.UpdateAPIView):
    """
        Представление для получения списка всех уроков.
        Attributes:
            serializer_class (LessonSerializer): Сериализатор, используемый для преобразования объектов уроков в JSON.
            queryset (QuerySet): Набор объектов уроков, используемых для построения списка.
    """
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsOwner | IsAdminUser| IsModerator]


class LessonDestroyAPIView(generics.DestroyAPIView):
    """
        Представление для получения списка всех уроков.
        Attributes:
            queryset (QuerySet): Набор объектов уроков, используемых для построения списка.
    """
    queryset = Lesson.objects.all()
    permission_classes = [IsOwner | IsAdminUser]
