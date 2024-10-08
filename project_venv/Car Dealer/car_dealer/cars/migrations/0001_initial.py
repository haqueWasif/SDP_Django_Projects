# Generated by Django 5.0.7 on 2024-09-21 08:01

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("brands", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="car_model",
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
                ("description", models.TextField()),
                ("price", models.TextField()),
                ("brand", models.ManyToManyField(to="brands.brand_model")),
            ],
        ),
    ]
