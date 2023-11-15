import os

from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail

from course.models import Subscription, Course

@shared_task
def sending_emails_about_updates(course_pk):
    subscriptions = Subscription.objects.filter(course=course_pk)
    course = Course.objects.get(pk=course_pk)
    for subscription in subscriptions:
        send_mail(
            subject=f'Обновление курса {course}',
            message='В курсе появились новые материалы',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[subscription.user.email],
            fail_silently=False
        )

