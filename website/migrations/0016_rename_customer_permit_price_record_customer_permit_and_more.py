# Generated by Django 4.2.9 on 2024-01-29 03:14

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("website", "0015_alter_record_customer_permit_price_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="record",
            old_name="customer_permit_price",
            new_name="customer_permit",
        ),
        migrations.RenameField(
            model_name="record",
            old_name="installer_permit_price",
            new_name="installer_permit",
        ),
    ]
