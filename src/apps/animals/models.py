from django.db import models

from apps.business.models import Location

# Create your models here.

# Field Types
# CharField, IntegerField, DecimalField, BooleanField, DateField, DateTimeField, ForeignKey, ManyToManyField

class Species(models.Model):
    CLASS_CHOICES = [('MAMMAL', 'Mammal'), ('REPTILE', 'Reptile'), ('BIRD','Bird'), ('AMPHIBIAN', 'Amphibian'),('INSECT', 'Insect')]
    name = models.CharField(max_length=80, unique=True)
    class_name = models.CharField(max_length=20, choices=CLASS_CHOICES, default="REPTILE") # Choices should be Mammal, Reptile, Bird, Insect, and Amphibian
    description = models.TextField()

    def __str__(self):
        return self.name

class Status(models.Model):
    name = models.CharField(max_length=80, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.name

class Animal(models.Model):
    #TODO Decide if Creator of an animal should be tracked via ForeignKey

    SEX_CHOICES = [('MALE', 'Male'), ('FEMALE', 'Female'), ('UNKNOWN', 'Unknown')]
    DIET_CHOICES = [('VEGGIE', 'Veggie'), ('MIXED', 'Mixed'), ('INSECT', 'Insect')]

    name = models.CharField(max_length=80,null=False, unique=True)
    description = models.TextField(blank=True, null=False, default='')
    donation_fee = models.DecimalField(max_digits=10, decimal_places=2, default=5.00)
    intake_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    animal_photo = models.ImageField(upload_to="images/", null=True, blank=True)
    color = models.CharField(max_length=80,null=False,default="None")
    sex = models.CharField(max_length=20, choices=SEX_CHOICES, default="UNKNOWN")
    age = models.IntegerField(default=0)
    diet = models.CharField(max_length=80, choices=DIET_CHOICES, default="MIXED")
    species = models.ForeignKey(Species, on_delete=models.SET_NULL, null=True)
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True)
    status = models.ForeignKey(Status, on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table_comment = "Holds information about animals"
    
    @property
    def animal_tag(self):
        return 'A-{0:05d}'.format(self.pk)
    
    @property
    def days_since_intake(self):
        #TODO Math the days from now() to intake date, return int of days
        pass

    def __str__(self):
        return self.name

