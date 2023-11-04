from django.db import models

from config import settings
from course.validators import validator_scam_url

NULLABLE = {'blank': True, 'null': True}


class Course(models.Model):
    """
    Модель представляет курс в онлайн-школе.

    Attributes:
        title (str): Название урока (максимум 150 символов).
        preview (ImageField): Превью курса, изображение.
        description (str): Описание курса.

    Relationships:
        owner (ForeignKey): Внешний ключ, связывающий объект с моделью пользователя.

    Methods:
        __str__(): Возвращает строковое представление объекта, используется для отображения
        названия курса при выводе в админимстивной панеле Django.
    """

    title = models.CharField(max_length=50, verbose_name="название")
    preview = models.ImageField(upload_to="course/", verbose_name="превью", null=True)
    description = models.TextField(verbose_name="описание")
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, **NULLABLE)

    def __str__(self):
        return self.title


class Lesson(models.Model):
    """
    Модель представляет урок в онлайн-школе.

    Attributes:
        title (str): Название урока (максимум 150 символов).
        description (str): Описание курса.
        preview (ImageField): Превью курса, изображение.
        url (URLFIELD): Ссылка на видеоурок.

    Relationships:
        course (ForeignKey): Внешний ключ,связывающий урок с курсом.
        Урок привязан к одному курсу, курс может содеожать много уроков.

        owner (ForeignKey): Внешний ключ, связывающий объект с моделью пользователя.

    Methods:
        __str__(): Возвращает строковое представление объекта, используется для отображения
        названия курса при выводе в админимстtitle (str): Название курса (максимум 50 символов).ративной панеле Django.
    """

    title = models.CharField(max_length=150, verbose_name="название")
    description = models.TextField(verbose_name="описание")
    preview = models.ImageField(upload_to="course/", verbose_name="превью", null=True)
    url = models.URLField(validators=[validator_scam_url], verbose_name="ссылка на видео")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="курс")
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, **NULLABLE)

    def __str__(self):
        return self.title


class Subscription(models.Model):
    """
           Модель подписки на курс.
           Attributes:
               user (ForeignKey): Ссылка на модель пользователя, который подписан на курс.
               course (ForeignKey): Ссылка на модель курса, на который подписан пользователь.
           Methods:
               __str__(): Возвращает строковое представление объекта подписки.
       """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='пользователь')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='курс')

    def __str__(self):
        return f'{self.user.email} подписан на {self.course.title}'