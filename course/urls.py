from django.urls import path
from rest_framework.routers import DefaultRouter

from course.apps import CourseConfig

from course.views.course import CourseViewSet
from course.views.lesson import (
    LessonCreateAPIView,
    LessonListAPIView,
    LessonRetrieveAPIView,
    LessonUpdateAPIView,
    LessonDestroyAPIView,
)
from course.views.subscription import SubscribeCourseCreateAPIView, UnsubscribeCourseDeleteAPIView

app_name = CourseConfig.name

router = DefaultRouter()
router.register(r"course", CourseViewSet, basename="course")

urlpatterns = [
    path("lesson/create/", LessonCreateAPIView.as_view(), name="lesson-create"),
    path("lesson/", LessonListAPIView.as_view(), name="lesson-list"),
    path("lesson/<int:pk>/", LessonRetrieveAPIView.as_view(), name="lesson-get"),
    path("lesson/update/<int:pk>/", LessonUpdateAPIView.as_view(), name="lesson-update"),
    path("lesson/delete/<int:pk>/", LessonDestroyAPIView.as_view(), name="lesson-delete"),
    path("subscribe/<int:course_id>", SubscribeCourseCreateAPIView.as_view(), name="subscribe-course"),
    path("unsubscribe/<int:course_id>", UnsubscribeCourseDeleteAPIView.as_view(), name="unsubscribe-course"),

] + router.urls
