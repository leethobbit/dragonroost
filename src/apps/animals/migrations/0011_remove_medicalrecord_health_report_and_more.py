# Generated by Django 5.0.3 on 2024-03-25 03:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("animals", "0010_medicalrecord"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="medicalrecord",
            name="health_report",
        ),
        migrations.RemoveField(
            model_name="medicalrecord",
            name="name",
        ),
        migrations.RemoveField(
            model_name="medicalrecord",
            name="treatment_history",
        ),
    ]
