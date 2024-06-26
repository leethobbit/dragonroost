# Generated by Django 5.0.6 on 2024-06-01 20:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("animals", "0020_alter_animal_outcome_date"),
        ("people", "0003_person_roles"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="medicalrecord",
            name="initials",
        ),
        migrations.RemoveField(
            model_name="medicalrecord",
            name="is_vet_cleared",
        ),
        migrations.AddField(
            model_name="animal",
            name="starting_weight",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="medicalrecord",
            name="bowel_movement",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="medicalrecord",
            name="current_weight",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="medicalrecord",
            name="q_volunteer",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.SET_DEFAULT,
                to="people.person",
            ),
        ),
        migrations.AddField(
            model_name="medicalrecord",
            name="treatments",
            field=models.TextField(blank=True, default="", max_length=500),
        ),
    ]
