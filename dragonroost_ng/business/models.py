from django.db import models

from dragonroost_ng.people.models import Person


# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=80, unique=True)
    description = models.TextField(blank=True, null=False, default="")

    def __str__(self):
        """
        Required method to see the name field when a form is created with this model
        """
        return self.name


# class Meeting
class Meeting(models.Model):
    """
    Model for staff meetings
    """

    title = models.CharField(max_length=120, unique=True)
    date = models.DateField(auto_now_add=True)
    minutes = models.FileField(upload_to="meetings/%Y")

    def __str__(self) -> str:
        return self.title


# class Donation
class Donation(models.Model):
    """
    Possible model for donations - not in use currently
    """

    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    donor = models.ForeignKey(Person, on_delete=models.DO_NOTHING)
    is_sponsorship = models.BooleanField(default=False)
    donation_date = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True, null=False, default="")

    def __str__(self) -> str:
        # TODO: Come up with a good string for this return. Maybe donor + amount + date?
        return self.pk
