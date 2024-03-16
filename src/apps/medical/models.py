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


class MedicalRecord(models.Model):
    name = models.CharField(max_length=80, null=False)
    health_report = models.TextField(max_length=500, null=False, blank=True, default="")
    treatment_history = models.TextField(max_length=500, null=False, blank=True, default="")
    notes = models.TextField(max_length=500, blank=True, null=False, default="")
    is_vet_cleared = models.BooleanField(default=False)

    class Meta:
        db_table_comment = "Table holds medical record entries."

    def __str__(self):
        return self.name
