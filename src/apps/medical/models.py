from django.db import models

EVENT_CHOICES = [
    ("WELLNESS / VACCINE", "Wellness / Vaccine"),
    ("SURGERY", "Surgery"),
    ("DIAGNOSIS", "Diagnosis"),
    ("MEDICATION / TREATMENT", "Medication / Treatment"),
]


# Create your models here.
class Treatment(models.Model):
    name = models.CharField(max_length=80, null=False)
    description = models.TextField(blank=True, null=False, default="")

    def __str__(self):
        return self.name


