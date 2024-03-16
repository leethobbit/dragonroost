from django.db import models

from apps.business.models import Location
from apps.medical.models import MedicalRecord

# Create your models here.

# Field Types
# CharField, IntegerField, DecimalField, BooleanField, DateField, DateTimeField, ForeignKey, ManyToManyField


class Species(models.Model):
    CLASS_CHOICES = [
        ("MAMMAL", "Mammal"),
        ("REPTILE", "Reptile"),
        ("BIRD", "Bird"),
        ("AMPHIBIAN", "Amphibian"),
        ("INSECT", "Insect"),
    ]
    name = models.CharField(max_length=80, unique=True)
    class_name = models.CharField(
        max_length=20, choices=CLASS_CHOICES, default="REPTILE"
    )  # Choices should be Mammal, Reptile, Bird, Insect, and Amphibian
    description = models.TextField()
    is_ohio_native = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Animal(models.Model):
    # TODO Decide if Creator of an animal should be tracked via ForeignKey

    SEX_CHOICES = [("MALE", "Male"), ("FEMALE", "Female"), ("UNKNOWN", "Unknown")]
    DIET_CHOICES = [("VEGGIE", "Veggie"), ("MIXED", "Mixed"), ("INSECT", "Insect")]
    STATUS_CHOICES = [
        ("PENDING", "Pending"),
        ("ADOPTABLE", "Adoptable"),
        ("QUARANTINED", "Quarantined"),
        ("FOSTERED", "Fostered"),
        ("MEDICAL_HOLD", "Medical Hold"),
        ("ADOPTED", "Adopted"),
    ]

    name = models.CharField(max_length=80, null=False, unique=True)
    description = models.TextField(blank=True, null=False, default="")
    donation_fee = models.DecimalField(max_digits=10, decimal_places=2, default=5.00)
    intake_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    animal_photo = models.ImageField(upload_to="images/", null=True, blank=True)
    color = models.CharField(max_length=80, null=False, default="None")
    sex = models.CharField(max_length=20, choices=SEX_CHOICES, default="UNKNOWN")
    age = models.IntegerField(default=0)
    diet = models.CharField(max_length=80, choices=DIET_CHOICES, default="MIXED")
    species = models.ForeignKey(Species, on_delete=models.SET_NULL, null=True)
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True)
    status = models.CharField(
        max_length=80, choices=STATUS_CHOICES, default="ADOPTABLE"
    )
    medical_record = models.OneToOneField(MedicalRecord, related_name="medical_record", on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table_comment = "Holds information about animals"

    @property
    def animal_tag(self):
        return "A-{0:05d}".format(self.pk)

    @property
    def is_available(self):
        if self.status == "ADOPTED":
            return False
        else:
            return True

    @property
    def days_since_intake(self):
        # TODO Math the days from now() to intake date, return int of days
        # Might be able to use Django timesince, like intake_date|timesince
        pass

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if self.pk is None:
            self.medical_record = MedicalRecord.objects.create(name = f"Medical_{self.name}")
        super().save(*args, **kwargs)

# class AnimalComment(models.Model):
#     TYPE_CHOICES = [
#         ("MEDICAL", "Medical"),
#         ("BEHAVIORAL", "Behavioral"),
#         ("COMMENT", "Comment"),
#         ("WARNING", "Warning"),
#     ]

#     animal = models.ForeignKey(Animal, related_name="comments",on_delete=models.CASCADE, null=False)
#     type = models.CharField(max_length=20, choices=TYPE_CHOICES, default="COMMENT")
#     comment = models.TextField(max_length=255, null=False, blank=True, default="")
#     initials = models.CharField(max_length=20, default="zz", null=False)
#     created = models.DateTimeField(auto_now_add=True)