from django.db import models

# Create your models here.


# class Role
class Role(models.Model):
    name = models.CharField(max_length=80, unique=True)
    description = models.TextField(blank=True, null=False, default="")

    def __str__(self):
        """
        Required method to see the name field when a form is created with this model
        """
        return self.name

    def get_absolute_url(self):
        return f"/people/roles/{self.id}/"


# class Person
# TODO Sort out how to link donations to a person, and sum them
class Person(models.Model):
    first_name = models.CharField(max_length=80, null=False, default="")
    last_name = models.CharField(max_length=80, null=False, default="")
    email = models.EmailField(null=False, default="donotemail@example.com")
    phone_number = models.CharField(max_length=20, default="555-5555")
    roles = models.ManyToManyField(Role)
    address = models.CharField(max_length=250, default="")
    zip_code = models.IntegerField(default=44121)
    notes = models.TextField(blank=True, null=False, default="")

    def __str__(self):
        """
        Required method to see the name field when a form is created with this model
        """
        return self.first_name + " " + self.last_name

    def get_absolute_url(self):
        return f"/people/{self.id}/"
