import factory

from dragonroost.animals.models import Species
from dragonroost.business.tests.factories import LocationFactory


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


class AnimalFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "animals.Animal"
        django_get_or_create = ("name", "breed", "species")

    name = factory.Faker("first_name")
    species = factory.SubFactory(SpeciesFactory)
    location = factory.SubFactory(LocationFactory)
