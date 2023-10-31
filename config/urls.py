from django.contrib import admin
from django.urls import path, include

urlpatterns = [path("admin/", admin.site.urls),
               path("", include("course.urls")),
               path("", include("payments.urls", namespace='paymentsusers')),
               path("users/", include("users.urls", namespace='users')),
               ]
