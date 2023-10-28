from rest_framework import serializers

from course.models import Course


class CourseSerializer(serializers.ModelSerializer):
    """
    Сериализатор модели курса для использования в Django REST framework.
    """

    class Meta:
        model = Course
        field = "__all__"
