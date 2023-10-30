from rest_framework import serializers

from course.models import Lesson


class LessonSerializer(serializers.ModelSerializer):
    """
    Сериализатор модели урока для использования в Django REST framework.
    """

    class Meta:
        model = Lesson
        fields = "__all__"
