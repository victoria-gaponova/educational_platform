from rest_framework.routers import DefaultRouter

from course.apps import CourseConfig

from course.views.course import CourseViewSet

app_name = CourseConfig.name

router = DefaultRouter()
router.register(r'course', CourseViewSet, basename='course')

urlpatterns = [

       ] + router.urls
