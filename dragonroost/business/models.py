from django.db import models

from dragonroost.people.models import Person


# Create your models here.
class Feedback(models.Model):
    FEEDBACK_CHOICES = [
        ("SUGGESTION", "Suggestion"),
        ("COMPLIMENT", "Compliment"),
        ("COMPLAINT", "Complaint"),
    ]

    name = models.CharField(max_length=80, null=False, blank=True, default="")
    email_address = models.EmailField(blank=True)
    feedback_type = models.CharField(
        max_length=80,
        choices=FEEDBACK_CHOICES,
        default="SUGGESTION",
    )
    feedback = models.TextField(blank=True, null=False, default="")

    def __str__(self):
        """
        Required method to see the name field when a form is created with this model
        """
        return self.name

    def get_absolute_url(self):
        return f"/business/feedback/{self}/"


class Location(models.Model):
    name = models.CharField(max_length=80, unique=True)
    description = models.TextField(blank=True, null=False, default="")

    def __str__(self):
        """
        Required method to see the name field when a form is created with this model
        """
        return self.name

    def get_absolute_url(self):
        return f"/business/locations/{self.id}/"


# class Meeting
class Meeting(models.Model):
    """
    Model for staff meetings
    """

    title = models.CharField(max_length=120, unique=True)
    date = models.DateField(auto_now_add=True)
    meeting_url = models.URLField(
        max_length=200,
        default="example.com",
        verbose_name="Meeting URL",
    )
    minutes = models.FileField(upload_to="meetings/%Y", blank=True)

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return f"/business/meetings/{self.id}/"


# class Donation
class Donation(models.Model):
    """
    Possible model for donations - not in use currently.
    TODO: Change this to a more generic Transaction model.
    """

    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    donor = models.ForeignKey(Person, on_delete=models.DO_NOTHING)
    is_sponsorship = models.BooleanField(default=False)
    donation_date = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True, null=False, default="")

    def __str__(self) -> str:
        # TODO: Come up with a good string for this return. Maybe donor + amount + date?
        return self.pk
