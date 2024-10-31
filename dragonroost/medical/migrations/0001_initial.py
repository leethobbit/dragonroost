# Generated by Django 5.0.9 on 2024-10-22 18:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('people', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MedicalUpdate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, unique=True)),
                ('date', models.DateField(auto_now_add=True)),
                ('notes', models.TextField(blank=True, default='')),
                ('q_staff', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='medical_notes', to='people.person')),
            ],
        ),
    ]