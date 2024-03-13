from django.db import models

from apps.animals.models import Animal

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

class MedicalRecord(models.Model):
    name = models.CharField(max_length=80, null=False, unique=True)
    animal = models.ForeignKey(Animal, on_delete=models.PROTECT, null=False)
    event_type = models.CharField(max_length=80, choices=EVENT_CHOICES)
    description = models.TextField(blank=True, null=False, default="")
    needs_treatment = models.BooleanField(default=False)

    class Meta:
        db_table_comment = "Table holds medical record entries."

    def __str__(self):
        return self.name
