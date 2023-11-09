from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from course.models import Subscription, Course
from course.serializers.subscription import SubscriptionSerializer


class SubscribeCourseCreateAPIView(generics.CreateAPIView):
    """
        Создает подписку пользователя на указанный курс.
        Parameters:
            course_id (int): Идентификатор курса.
        Returns:
            Response: Объект ответа с информацией о результате операции.
                HTTP_201_CREATED: Подписка успешно создана.
                HTTP_400_BAD_REQUEST: Подписка уже существует.
        """
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        course = get_object_or_404(Course, pk=kwargs['course_id'])

        # Проверка подписан ли пользователь уже на этот курс

        if Subscription.objects.filter(user=request.user, course=course).exists():
            return Response({'detail': 'Вы уже подписаны на этот курс.'}, status=status.HTTP_208_ALREADY_REPORTED)

        serializer = self.get_serializer(data={'user': request.user.id, 'course': kwargs['course_id']})
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        return Response({'detail': 'Вы успешно подписались на курс'}, status=status.HTTP_201_CREATED)


class UnsubscribeCourseDeleteAPIView(generics.DestroyAPIView):
    """
        Удаляет подписку пользователя на указанный курс.
        Parameters:
            course_id (int): Идентификатор курса.
        Returns:
            Response: Объект ответа с информацией о результате операции.
                HTTP_200_OK: Подписка успешно удалена.
        """
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        course_id = self.kwargs.get('course_id')
        course = Course.objects.get(pk=course_id)
        return Subscription.objects.get(user=self.request.user, course=course)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({'detail': 'Вы успешно отписаны от курса'}, status=status.HTTP_200_OK)
