# Generated by Django 4.2 on 2023-04-24 08:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Ecosystem",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
                ("icon", models.ImageField(upload_to="photos/%Y/%m/%d/")),
                ("description", models.TextField(blank=True)),
                ("website", models.CharField(blank=True, max_length=150)),
                (
                    "date_added",
                    models.DateTimeField(blank=True, default=datetime.datetime.now),
                ),
            ],
        ),
    ]
