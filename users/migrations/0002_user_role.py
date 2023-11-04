# Generated by Django 4.2.6 on 2023-11-04 15:25

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="role",
            field=models.CharField(
                choices=[("member", "member"), ("moderator", "moderator")],
                default="member",
                max_length=9,
            ),
        ),
    ]
