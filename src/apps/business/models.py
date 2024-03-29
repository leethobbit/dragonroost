from django.db import models

from apps.people.models import Person


# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=80, unique=True)
    description = models.TextField(blank=True, null=False, default="")

    def __str__(self):
        """
        Required method to see the name field when a form is created with this model
        """
        return self.name


# class Donation
class Donation(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    donor = models.ForeignKey(Person, on_delete=models.DO_NOTHING)
    is_sponsorship = models.BooleanField(default=False)
    donation_date = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True, null=False, default="")
