# Generated by Django 4.2.9 on 2024-01-29 02:31

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("website", "0007_recordnote_user"),
    ]

    operations = [
        migrations.AddField(
            model_name="record",
            name="customer_permit_price",
            field=models.IntegerField(default="-", null=True),
        ),
        migrations.AddField(
            model_name="record",
            name="installer_permit_price",
            field=models.IntegerField(default="-", null=True),
        ),
    ]
