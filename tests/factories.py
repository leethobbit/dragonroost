import factory
from django.contrib.auth import get_user_model

from apps.animals.models import Animal, Species
from apps.business.models import Location
from apps.people.models import Person, Role


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


class RoleFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Role

    name = "VOLUNTEER"
    description = factory.Faker("sentence")


class PersonFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Person

    first_name = factory.Faker("word")
    last_name = factory.Faker("word")
    email = factory.Faker("email")
    phone_number = factory.Faker("phone_number")
    roles = factory.SubFactory(RoleFactory)

    @factory.post_generation
    def roles(self, create, extracted, **kwargs):
        if not create:
            # Simple build, do nothing.
            return

        if extracted:
            # A list of roles were passed in, use them
            for role in extracted:
                self.roles.add(role)
