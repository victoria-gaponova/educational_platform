import os
import random

from decimal import Decimal
from django.core.management import BaseCommand
from faker import Faker

from config import settings
from course.models import Lesson, Course
from payments.models import Payment
from users.models import User, UserRoles

fake = Faker()


class Command(BaseCommand):
    """
           Команда для сброса и добавления тестовых данных в модель Payment.

           Метод `handle` выполняет следующие шаги:
           1. Удаляет все записи в моделях Payment, Lesson и Course и User.
           2. Создает суперпользователя.
           3. Создает модератор пользователя.
           4. Создает 5 пользователей и сохраняет их в список.
           5. Создает 5 курсов и для каждого курса создает 3 урока.
           6. Создает 20 случайных платежей, связанных с пользователями, курсами и уроками.

           Attributes:
               help (str): Описание команды для вывода при запуске `python manage.py help`.
       """
    help = 'Reset and add sample payment data to the Payment model'

    def handle(self, *args, **kwargs):
        # Удаление всех записей в моделях
        Payment.objects.all().delete()
        Lesson.objects.all().delete()
        Course.objects.all().delete()
        User.objects.all().delete()

        # Создание суперпользователя
        super_user = User.objects.create(
            email=settings.EMAIL_HOST_USER,
            first_name='Admin',
            last_name='LMS',
            is_staff=True,
            is_superuser=True
        )
        super_user.set_password(os.getenv('ADMIN_PASSWORD'))
        super_user.save()

        # Создание модератор
        moderator_user = User.objects.create(
            email=os.getenv('MODERATOR_EMAIL'),
            first_name='Admin',
            last_name='LMS',
            role=UserRoles.MODERATOR
        )
        moderator_user.set_password(os.getenv('ADMIN_PASSWORD'))
        moderator_user.save()

        # Создание пользователя
        users = []
        for _ in range(5):
            email = fake.email()
            phone = fake.numerify()
            country = fake.country()
            first_name = fake.first_name()
            last_name = fake.last_name()
            user = User.objects.create(email=email, phone=phone, country=country,
                                       first_name=first_name, last_name=last_name)
            user.set_password(os.getenv('ADMIN_PASSWORD'))
            user.save()
            users.append(user)

        # Создание курсов
        courses = []
        for i in range(5):
            course = Course.objects.create(
                title=fake.word(),
                description=fake.text(),
                owner=users[i],
            )
            courses.append(course)

        # Создание уроков
        lessons = []
        for _ in range(3):
            lesson = Lesson.objects.create(
                title=fake.sentence(),
                description=fake.text(),
                course=course,
                url=fake.url(),
                owner=users[i]
            )
            lessons.append(lesson)

        # Создание платежей
        for _ in range(20):
            user = random.choice(users)
            payment_date = fake.date_between(start_date='-30d', end_date='today')
            amount = Decimal(random.uniform(10, 100))
            payment_method = random.choice(['cash', 'transfer'])

            is_course = random.choice([True, False])
            course_or_lesson = random.choice(courses) if is_course else random.choice(lessons)

            Payment.objects.create(
                user=user,
                date=payment_date,
                course=course_or_lesson if is_course else None,
                lesson=course_or_lesson if not is_course else None,
                amount=amount,
                payment_method=payment_method,
            )
