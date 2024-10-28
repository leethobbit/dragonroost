from django.db import models

from dragonroost_ng.people.models import Person

# Create your models here.


class MedicalUpdate(models.Model):
    """
    Model for medical staff updates
    """

    title = models.CharField(max_length=120, unique=True)
    q_staff = models.ForeignKey(
        Person,
        on_delete=models.SET_NULL,
        related_name="medical_notes",
        null=True,
    )
    date = models.DateField(auto_now_add=True)
    notes = models.TextField(blank=True, null=False, default="")

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return f"/medical/updates/{self}/"
