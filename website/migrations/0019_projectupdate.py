# Generated by Django 4.2.9 on 2024-01-30 04:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("website", "0018_record_previous_project_status"),
    ]

    operations = [
        migrations.CreateModel(
            name="ProjectUpdate",
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
                ("updated_at", models.DateTimeField(auto_now_add=True)),
                ("update_text", models.TextField()),
                (
                    "record",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="website.record"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
