from django.db import models

# Create your models here.

# class User

# class UserRole


# class Role
class Role(models.Model):
    name = models.CharField(max_length=80, unique=True)
    description = models.TextField(blank=True, null=False, default="")

    def __str__(self):
        """
        Required method to see the name field when a form is created with this model
        """
        return self.name


# class Person
# TODO Sort out how to link donations to a person, and sum them
class Person(models.Model):
    TYPE_CHOICES = [
        ("ADOPTER", "Adopter"),
        ("DONOR", "Donor"),
        ("VOLUNTEER", "Volunteer"),
        ("UNKNOWN", "Unknown"),
    ]

    first_name = models.CharField(max_length=80, null=False, default="")
    last_name = models.CharField(max_length=80, null=False, default="")
    email = models.EmailField(null=False, default="donotemail@example.com")
    phone_number = models.CharField(max_length=20, default="555-5555")
    type = models.CharField(max_length=80, choices=TYPE_CHOICES, default="UNKNOWN")
    roles = models.ManyToManyField(Role)
    address = models.CharField(max_length=250, default="")
    zip_code = models.IntegerField(default=44121)
    notes = models.TextField(blank=True, null=False, default="")

    def __str__(self):
        """
        Required method to see the name field when a form is created with this model
        """
        return self.first_name + " " + self.last_name
