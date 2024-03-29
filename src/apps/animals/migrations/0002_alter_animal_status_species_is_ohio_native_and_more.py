# Generated by Django 5.0.3 on 2024-03-12 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("animals", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="animal",
            name="status",
            field=models.CharField(
                choices=[
                    ("PENDING", "Pending"),
                    ("ADOPTABLE", "Adoptable"),
                    ("QUARANTINED", "Quarantined"),
                    ("FOSTERED", "Fostered"),
                    ("NEED VET CHECK", "Need Vet Check"),
                    ("ADOPTED", "Adopted"),
                ],
                default="ADOPTABLE",
                max_length=80,
            ),
        ),
        migrations.AddField(
            model_name="species",
            name="is_ohio_native",
            field=models.BooleanField(default=False),
        ),
        migrations.DeleteModel(
            name="Status",
        ),
    ]
