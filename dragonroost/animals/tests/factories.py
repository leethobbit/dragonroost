import factory
from measurement.measures import Weight

from dragonroost.animals.models import Breed
from dragonroost.animals.models import Species
from dragonroost.business.tests.factories import LocationFactory
from dragonroost.people.tests.factories import PersonFactory


class SpeciesFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "animals.Species"
        django_get_or_create = ("name", "class_name", "diet", "is_ohio_native")

    name = factory.Sequence(lambda n: f"Species {n}")
    class_name = factory.Faker(
        "random_element",
        elements=[x[0] for x in Species.CLASS_CHOICES],
    )
    diet = factory.Faker(
        "random_element",
        elements=[x[0] for x in Species.DIET_CHOICES],
    )
    is_ohio_native = factory.Iterator([True, False])


class BreedFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "animals.Breed"
        django_get_or_create = ("name", "origin", "temperament")

    name = factory.Sequence(lambda n: f"Breed {n}")
    origin = factory.Faker("country")
    temperament = factory.Faker(
        "random_element",
        elements=[x[0] for x in Breed.TEMPERAMENT_CHOICES],
    )


class AnimalFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "animals.Animal"
        django_get_or_create = ("name", "breed", "species")

    name = factory.Faker("first_name")
    species = factory.SubFactory(SpeciesFactory)
    location = factory.SubFactory(LocationFactory)
    breed = None
    starting_weight = Weight(lb=10)
    status = factory.Iterator(["AVAILABLE", "QUARANTINE"])


class MedicalRecordFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "animals.MedicalRecord"
        django_get_or_create = ("animal", "notes")

    notes = factory.Faker("text")
    current_weight = Weight(lb=15)
    animal = factory.SubFactory(AnimalFactory)
    q_volunteer = factory.SubFactory(PersonFactory)
