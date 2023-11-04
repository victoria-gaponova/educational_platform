from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class UserRoles(models.TextChoices):
    """
            Класс перечисления для определения ролей пользователя.

            Attributes:
                MEMBER (str): Значение роли 'member'.
                MODERATOR (str): Значение роли 'moderator'.
        """
    MEMBER = 'member', _('member')
    MODERATOR = 'moderator', _('moderator')


class User(AbstractUser):
    """
    Расширенная модель пользователя для проекта Django.

    Заменяет стандартную модель пользователя Django для включения
    дополнительной информации, такой как email, аватар, телефон и страна.

    Attributes:
        email (str): Уникальный адрес электронной почты.
        phone (str): Номер телефона пользователя.
        country (str): Страна,в которой проживает пользователь.
        avatar (ImageField): Изображения профиля пользователя.
        role (str): Роль пользователя (модератор или обычный пользователь).
    """

    username = None
    email = models.EmailField(unique=True, verbose_name="Почта")
    phone = models.CharField(max_length=35, verbose_name="Телефон")
    country = models.CharField(max_length=35, verbose_name="Страна")
    avatar = models.ImageField(upload_to="users/", null=True, blank=True, verbose_name="Аватар")
    role = models.CharField(max_length=9, choices=UserRoles.choices, default=UserRoles.MEMBER)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
