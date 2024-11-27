import factory

from dragonroost.business.models import Location
from dragonroost.business.models import Meeting


class LocationFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Location
        django_get_or_create = ("name",)

    name = factory.Sequence(lambda n: f"Location {n}")
    description = factory.Sequence(lambda n: f"Description {n}")


class MeetingFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Meeting
        django_get_or_create = ("title",)

    title = factory.Sequence(lambda n: f"Meeting {n}")
    description = factory.Sequence(lambda n: f"Description {n}")
