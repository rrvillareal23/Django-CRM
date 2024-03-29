# Generated by Django 4.2.9 on 2024-01-30 01:27

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("website", "0017_alter_record_customer_permit_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="record",
            name="previous_project_status",
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
    ]
