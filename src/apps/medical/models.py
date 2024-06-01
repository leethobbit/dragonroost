from django.db import models

from apps.people.models import Person

EVENT_CHOICES = [
    ("WELLNESS / VACCINE", "Wellness / Vaccine"),
    ("SURGERY", "Surgery"),
    ("DIAGNOSIS", "Diagnosis"),
    ("MEDICATION / TREATMENT", "Medication / Treatment"),
]


# Create your models here.


class Treatment(models.Model):
    """
    Treatments model - Not in use currently but could be implemented at a later time.
    """

    name = models.CharField(max_length=80, null=False)
    description = models.TextField(blank=True, null=False, default="")

    def __str__(self):
        return self.name


# Create a class for Q room updates
class QRoomUpdate(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True, null=False, default="")
    q_volunteer = models.ForeignKey(Person, on_delete=models.SET_DEFAULT, default=1)

    def __str__(self):
        return self.description
