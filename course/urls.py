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
    path("<int:pk>/lesson/", LessonRetrieveAPIView.as_view(), name="lesson-get"),
    path("<int:pk>/lesson/update/", LessonUpdateAPIView.as_view(), name="lesson-update"),
    path("<int:pk>/lesson/delete/", LessonDestroyAPIView.as_view(), name="lesson-delete"),
    path("<int:course_id>/subscribe/", SubscribeCourseCreateAPIView.as_view(), name="subscribe-course"),
    path("<int:course_id>/unsubscribe//", UnsubscribeCourseDeleteAPIView.as_view(), name="unsubscribe-course"),

] + router.urls
