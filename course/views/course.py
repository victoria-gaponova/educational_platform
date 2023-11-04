from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.viewsets import ModelViewSet

from course.models import Course
from course.permissions import IsOwner, IsModerator
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

    def get_permissions(self):
        """Права доступа"""
        if self.action == "retrieve":
            permission_classes = [IsOwner | IsAdminUser | IsModerator]
        elif self.action == "create":
            permission_classes = [IsAdminUser]
        elif self.action == "destroy":
            permission_classes = [IsOwner | IsAdminUser]
        elif self.action == "update":
            permission_classes = [IsOwner | IsAdminUser| IsModerator]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

