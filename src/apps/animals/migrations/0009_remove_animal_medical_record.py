# Generated by Django 5.0.3 on 2024-03-22 21:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("animals", "0008_alter_animal_medical_record"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="animal",
            name="medical_record",
        ),
    ]
