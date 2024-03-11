import factory
from django.contrib.auth import get_user_model

from apps.animals.models import Animal, Species, Status
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

class StatusFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Status
    
    name = factory.Faker("word")
    description = factory.Faker("sentence")

class AnimalFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Animal
    
    name = factory.Sequence(lambda n: "BD %03d" % n)
    description = factory.Faker("sentence")
    donation_fee = 10.50
    color = factory.Faker("color_name")
    sex = "FEMALE"
    age = 69
    diet = "VEGGIES"
    species = factory.SubFactory(SpeciesFactory)
    location = factory.SubFactory(LocationFactory)
    status = factory.SubFactory(StatusFactory)

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = get_user_model()
    
    username = factory.Faker("user_name")
    email = factory.Faker("email")