from django.db import models

from apps.business.models import Location
from apps.people.models import Person

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
    DIET_CHOICES = [
        ("VEGGIE", "Veggie"),
        ("CARNIVORE", "Carnivore"),
        ("MIXED", "Mixed"),
        ("INSECT", "Insect"),
        ("UNKNOWN", "Unknown"),
    ]
    name = models.CharField(max_length=80, unique=True)
    class_name = models.CharField(
        max_length=20, choices=CLASS_CHOICES, default="REPTILE"
    )  # Choices should be Mammal, Reptile, Bird, Insect, and Amphibian
    description = models.TextField()
    diet = models.CharField(max_length=80, choices=DIET_CHOICES, default="UNKNOWN")
    is_ohio_native = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Animal(models.Model):
    # TODO Decide if Creator of an animal should be tracked via ForeignKey

    SEX_CHOICES = [("MALE", "Male"), ("FEMALE", "Female"), ("UNKNOWN", "Unknown")]
    STATUS_CHOICES = [
        ("PENDING", "Pending"),
        ("ADOPTABLE", "Adoptable"),
        ("QUARANTINED", "Quarantined"),
        ("FOSTERED", "Fostered"),
        ("MEDICAL_HOLD", "Medical Hold"),
        ("ADOPTED", "Adopted"),
        ("DECEASED", "Deceased"),
    ]
    INTAKE_CHOICES = [
        ("UNKNOWN", "Unknown"),
        ("OWNER_SURRENDER", "Owner Surrender"),
        ("STRAY", "Stray"),
        ("RETURN_TO_RESCUE", "Return to Rescue"),
        ("BORN_IN_CARE", "Born in Care"),
    ]
    CONDITION_CHOICES = [
        ("UNKNOWN", "Unknown"),
        ("HEALTHY", "Healthy"),
        ("SICK", "Sick"),
        ("INJURED", "Injured"),
    ]
    OUTCOME_CHOICES = [
        ("ADOPTION", "Adoption"),
        ("DIED_IN_CARE", "Died in Care"),
        ("TRANSFER", "Transfer"),
        ("RETURN_TO_OWNER", "Return to Owner"),
    ]

    name = models.CharField(max_length=80, null=False, unique=True)
    description = models.TextField(blank=True, null=False, default="")
    donation_fee = models.DecimalField(max_digits=10, decimal_places=2, default=5.00)
    intake_date = models.DateTimeField(auto_now_add=True)
    outcome_date = models.DateField(null=True)
    outcome_type = models.CharField(
        max_length=80, choices=OUTCOME_CHOICES, default="ADOPTION"
    )
    intake_type = models.CharField(
        max_length=80, choices=INTAKE_CHOICES, default="OWNER_SURRENDER"
    )
    intake_condition = models.CharField(
        max_length=80, choices=CONDITION_CHOICES, default="HEALTHY"
    )
    current_condition = models.CharField(
        max_length=80, choices=CONDITION_CHOICES, default="UNKNOWN"
    )
    updated_at = models.DateTimeField(auto_now=True)
    animal_photo = models.ImageField(upload_to="images/", null=True, blank=True)
    color = models.CharField(max_length=80, null=False, default="None")
    sex = models.CharField(max_length=20, choices=SEX_CHOICES, default="UNKNOWN")
    age = models.IntegerField(default=0)
    starting_weight = models.IntegerField(default=0)
    species = models.ForeignKey(
        Species, on_delete=models.SET_NULL, related_name="animals", null=True
    )
    location = models.ForeignKey(
        Location, on_delete=models.SET_NULL, related_name="animals", null=True
    )
    status = models.CharField(
        max_length=80, choices=STATUS_CHOICES, default="ADOPTABLE"
    )

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

    @property
    def number_of_medical_records(self):
        return MedicalRecord.objects.filter(animal=self).count()

    def __str__(self):
        return self.name


class MedicalRecord(models.Model):
    """
    This model is used to hold medical records for animals. 
    Each animal can have any number of Medical Records attached.
    """
    created = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(max_length=500, blank=True, null=False, default="")
    current_weight = models.IntegerField(default=0)
    bowel_movement = models.BooleanField(default=True)
    treatments = models.TextField(max_length=500, blank=True, null=False, default="")
    q_volunteer = models.ForeignKey(Person, on_delete=models.SET_DEFAULT, default=1)
    animal = models.ForeignKey(
        Animal, related_name="medical_records", on_delete=models.CASCADE, default=1
    )

    class Meta:
        db_table_comment = "Table holds medical record entries."

    def __str__(self):
        return self.notes
