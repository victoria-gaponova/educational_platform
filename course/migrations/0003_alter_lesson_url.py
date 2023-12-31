# Generated by Django 4.2.6 on 2023-11-04 19:57

import course.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("course", "0002_course_owner_lesson_owner"),
    ]

    operations = [
        migrations.AlterField(
            model_name="lesson",
            name="url",
            field=models.URLField(
                validators=[course.validators.validator_scam_url],
                verbose_name="ссылка на видео",
            ),
        ),
    ]
