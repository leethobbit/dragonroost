# Generated by Django 5.0.3 on 2024-05-25 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("animals", "0016_animal_current_condition_alter_species_diet"),
    ]

    operations = [
        migrations.AddField(
            model_name="animal",
            name="adopted_date",
            field=models.DateTimeField(null=True),
        ),
    ]
