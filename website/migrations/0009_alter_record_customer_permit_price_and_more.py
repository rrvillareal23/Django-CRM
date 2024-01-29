# Generated by Django 4.2.9 on 2024-01-29 02:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("website", "0008_record_customer_permit_price_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="record",
            name="customer_permit_price",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="record",
            name="customer_price",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="record",
            name="installer_permit_price",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="record",
            name="installer_price",
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
