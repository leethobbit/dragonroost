# Generated by Django 5.0.3 on 2024-03-10 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Treatment",
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
                ("name", models.CharField(max_length=80, unique=True)),
                ("description", models.TextField(blank=True, default="")),
                (
                    "cost",
                    models.DecimalField(decimal_places=2, default=5.0, max_digits=6),
                ),
            ],
            options={
                "db_table_comment": "Holds information about kinds of treatments.",
            },
        ),
        migrations.CreateModel(
            name="Vaccine",
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
                ("name", models.CharField(max_length=80, unique=True)),
                ("description", models.TextField(blank=True, default="")),
                (
                    "cost",
                    models.DecimalField(decimal_places=2, default=5.0, max_digits=6),
                ),
            ],
            options={
                "db_table_comment": "Holds information about kinds of vaccines.",
            },
        ),
    ]
