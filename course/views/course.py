from rest_framework.viewsets import ModelViewSet

from course.models import Course
from course.serializers.course import CourseSerializer


class CourseViewSet(ModelViewSet):
    """
    ViewSet для взаимодействия с моделью курса.

    Attributes:
        queryset (QuerySet): Это набор объектов курсов, предварительно загруженные связанные уроки.
        serializer_class (CourseSerializer): Сериализатор,используемый для преобразования объектов курса в JSON и наоборот.
    """
    serializer_class = CourseSerializer
    queryset = Course.objects.all()