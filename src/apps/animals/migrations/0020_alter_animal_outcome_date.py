# Generated by Django 5.0.3 on 2024-05-25 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("animals", "0019_animal_outcome_type"),
    ]

    operations = [
        migrations.AlterField(
            model_name="animal",
            name="outcome_date",
            field=models.DateField(null=True),
        ),
    ]
