import factory
from django.contrib.auth import get_user_model

from apps.animals.models import Animal, Species
from apps.business.models import Location


class SpeciesFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Species

    name = factory.Faker("word")
    description = factory.Faker("sentence")


class LocationFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Location

    name = factory.Faker("word")
    description = factory.Faker("sentence")

    name = factory.Faker("word")
    description = factory.Faker("sentence")


class AnimalFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Animal

    name = factory.Faker("word")
    description = factory.Faker("sentence")
    donation_fee = 10.50
    color = factory.Faker("color_name")
    sex = "FEMALE"
    age = 69
    species = factory.SubFactory(SpeciesFactory)
    location = factory.SubFactory(LocationFactory)
    status = "ADOPTABLE"


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = get_user_model()

    username = factory.Faker("user_name")
    email = factory.Faker("email")
