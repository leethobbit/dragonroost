import logging
from datetime import timezone

from django.db import models
from django.urls import reverse
from django_measurement.models import MeasurementField
from measurement.measures import Weight

from dragonroost.business.models import Location
from dragonroost.people.models import Person

from .managers import AnimalQuerySet

logger = logging.getLogger(__name__)


# Create your models here.
class Species(models.Model):
    CLASS_CHOICES = [
        ("MAMMAL", "Mammal"),
        ("REPTILE", "Reptile"),
        ("BIRD", "Bird"),
        ("AMPHIBIAN", "Amphibian"),
        ("INSECT", "Insect"),
        ("FISH", "Fish"),
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
        max_length=20,
        choices=CLASS_CHOICES,
        default="REPTILE",
    )  # Choices should be Mammal, Reptile, Bird, Insect, and Amphibian
    description = models.TextField()
    diet = models.CharField(max_length=80, choices=DIET_CHOICES, default="UNKNOWN")
    is_ohio_native = models.BooleanField(default=False)
    has_breeds = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("animals:species-detail", args=[str(self.id)])


class Breed(models.Model):
    TEMPERAMENT_CHOICES = [
        ("ACTIVE", "Active"),
        ("ENERGETIC", "Energetic"),
        ("GENTLE", "Gentle"),
        ("INDEPENDENT", "Independent"),
    ]

    name = models.CharField(max_length=80, unique=True)
    origin = models.CharField(max_length=80, blank=True)
    species = models.ForeignKey(
        Species,
        related_name="breeds",
        on_delete=models.CASCADE,
        default=1,
    )
    temperament = models.CharField(
        max_length=80,
        choices=TEMPERAMENT_CHOICES,
        default="ACTIVE",
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("animals:breed-detail", args=[str(self.id)])


class Animal(models.Model):
    # TODO Decide if Creator of an animal should be tracked via ForeignKey

    SEX_CHOICES = [("MALE", "Male"), ("FEMALE", "Female"), ("UNKNOWN", "Unknown")]
    STATUS_CHOICES = [
        ("ADOPTED", "Adopted"),
        ("AMBASSADOR", "Ambassador"),
        ("AVAILABLE", "Available"),
        ("DECEASED", "Deceased"),
        ("FOSTERED", "Fostered"),
        ("MEDICAL_HOLD", "Medical Hold"),
        ("ON_HOLD", "On Hold"),
        ("QUARANTINE", "Quarantine"),
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
        max_length=80,
        choices=OUTCOME_CHOICES,
        default="ADOPTION",
    )
    intake_type = models.CharField(
        max_length=80,
        choices=INTAKE_CHOICES,
        default="OWNER_SURRENDER",
    )
    intake_condition = models.CharField(
        max_length=80,
        choices=CONDITION_CHOICES,
        default="HEALTHY",
    )
    current_condition = models.CharField(
        max_length=80,
        choices=CONDITION_CHOICES,
        default="UNKNOWN",
    )
    updated_at = models.DateTimeField(auto_now=True)
    animal_photo = models.ImageField(
        upload_to="images/",
        null=True,
        blank=True,
    )
    color = models.CharField(max_length=80, null=False, default="None")
    sex = models.CharField(max_length=20, choices=SEX_CHOICES, default="UNKNOWN")
    age = models.IntegerField(default=0)
    starting_weight = MeasurementField(measurement=Weight)
    species = models.ForeignKey(
        Species,
        on_delete=models.SET_NULL,
        related_name="animals",
        null=True,
    )
    location = models.ForeignKey(
        Location,
        on_delete=models.SET_NULL,
        related_name="animals",
        null=True,
    )
    status = models.CharField(
        max_length=80,
        choices=STATUS_CHOICES,
        default="AVAILABLE",
    )
    breed = models.ForeignKey(
        Breed,
        on_delete=models.SET_DEFAULT,
        related_name="animals",
        null=True,
        default=None,
    )

    objects = AnimalQuerySet.as_manager()

    class Meta:
        db_table_comment = "Holds information about animals"
        ordering = ["-intake_date"]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f"/animals/{self.id}/"

    @property
    def animal_tag(self):
        return f"A-{self.pk:05d}"

    @property
    def is_available(self):
        return self.status == "AVAILABLE"

    @property
    def days_since_intake(self):
        # TODO Math the days from now() to intake date, return int of days
        # Might be able to use Django timesince, like intake_date|timesince
        pass

    @property
    def number_of_medical_records(self):
        return MedicalRecord.objects.filter(animal=self).count()

    @property
    def latest_medical_record(self):
        return MedicalRecord.objects.filter(animal=self).latest("created")

    @property
    def is_recently_cleared(self):
        """
        Track all recently vet cleared animals. Recent means in the last 14 days.
        """
        today = timezone.now().replace(hour=0, minute=0, second=0, microsecond=0)
        vet_cleared_date = self.vet_cleared_date.replace(year=today.year)
        plus_thirty_days = today + timezone.timedelta(days=30)
        return today < vet_cleared_date < plus_thirty_days


class MedicalRecord(models.Model):
    """
    This model is used to hold medical records for animals.
    Each animal can have any number of Medical Records attached.
    """

    created = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(max_length=500, blank=True, null=False, default="")
    current_weight = MeasurementField(measurement=Weight)
    bowel_movement = models.BooleanField(default=True)
    problem_list = models.TextField(max_length=500, blank=True, null=False, default="")
    findings = models.TextField(max_length=500, blank=True, null=False, default="")
    treatments = models.TextField(max_length=500, blank=True, null=False, default="")
    q_volunteer = models.ForeignKey(Person, on_delete=models.SET_DEFAULT, default=1)
    animal = models.ForeignKey(
        Animal,
        related_name="medical_records",
        on_delete=models.CASCADE,
        default=1,
    )

    class Meta:
        db_table_comment = "Table holds medical record entries."
        ordering = ["created"]

    def __str__(self):
        return self.notes
