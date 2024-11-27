from django.db import models


# Create your models here.
class Feedback(models.Model):
    FEEDBACK_CHOICES = [
        ("SUGGESTION", "Suggestion"),
        ("COMPLIMENT", "Compliment"),
        ("COMPLAINT", "Complaint"),
    ]

    name = models.CharField(max_length=80, null=False, blank=True, default="")
    date = models.DateTimeField(auto_now_add=True)
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


class TransactionCategory(models.Model):
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Transaction(models.Model):
    TRANSACTION_TYPE_CHOICES = [
        ("INCOME", "Income"),
        ("EXPENSE", "Expense"),
    ]

    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    category = models.ForeignKey(TransactionCategory, on_delete=models.CASCADE)
    type = models.CharField(max_length=10, choices=TRANSACTION_TYPE_CHOICES)
    description = models.TextField(blank=True, null=False, default="")
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.type} of {self.amount} on {self.date}"
