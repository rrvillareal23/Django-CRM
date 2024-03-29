# Generated by Django 4.2.9 on 2024-01-27 15:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("website", "0004_record_project_tier"),
    ]

    operations = [
        migrations.AddField(
            model_name="record",
            name="customer_price",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="record",
            name="installer_price",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="record",
            name="project_status",
            field=models.CharField(
                choices=[
                    ("Waiting on Tou", "WAITING ON TOU"),
                    ("Waiting on Survey", "WAITING ON SURVEY"),
                    ("Waiting on Deposit", "WAITING ON DEPOSIT"),
                    ("Waiting on Installer", "WAITING ON INSTALLER"),
                    ("Waiting on Customer", "WAITING ON CUSTOMER"),
                    ("Waiting on Appointment", "WAITING ON APPOINTMENT"),
                    ("Waiting on Permit", "WAITING ON PERMIT"),
                    ("Waiting on Install", "WAITING ON INSTALL"),
                    ("Install Completed", "INSTALL COMPLETED"),
                ],
                default="Waiting on Survey",
                max_length=50,
            ),
        ),
        migrations.CreateModel(
            name="RecordNote",
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
                ("note", models.TextField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "record",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="website.record"
                    ),
                ),
            ],
            options={
                "ordering": ["-created_at"],
            },
        ),
    ]
