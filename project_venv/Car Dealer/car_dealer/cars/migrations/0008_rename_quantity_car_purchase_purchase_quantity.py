# Generated by Django 5.0.7 on 2024-09-21 18:24

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("cars", "0007_car_purchase"),
    ]

    operations = [
        migrations.RenameField(
            model_name="car_purchase",
            old_name="quantity",
            new_name="purchase_quantity",
        ),
    ]
