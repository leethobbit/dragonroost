import logging
import random

from django.core.management.base import BaseCommand
from faker import Faker

from dragonroost.animals.models import Species
from dragonroost.business.models import Location
from dragonroost.people.models import Person
from dragonroost.people.models import Role

fake = Faker()
logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "Create test data for Dragonroost."

    def handle(self, *args, **options):
        self.create_species()
        self.create_locations()
        self.create_roles()
        self.create_people()
        self.stdout.write(self.style.SUCCESS("Test data created successfully!"))

    def create_species(self):
        if Species.objects.all().count() > 0:
            return

        species_names = [
            "Corn Snake",
            "Red-eared Slider",
            "Ball Python",
            "Bearded Dragon",
            "Reticulated Python",
            "Russian Tortoise",
        ]

        for name in species_names:
            Species.objects.get_or_create(
                name=name,
                description=fake.text(max_nb_chars=20),
                is_ohio_native=fake.boolean(chance_of_getting_true=25),
            )

    def create_locations(self):
        if Location.objects.all().count() > 0:
            return

        location_names = ["Sales Floor", "Q Room", "Upstairs"]

        for name in location_names:
            Location.objects.get_or_create(
                name=name,
                description=fake.text(max_nb_chars=20),
            )

    def create_roles(self):
        if Role.objects.all().count() > 0:
            return

        roles = ["Volunteer", "Donor", "Foster", "Adopter"]

        for role in roles:
            Role.objects.get_or_create(
                name=role,
                description=fake.text(max_nb_chars=50),
            )

    def create_people(self):
        person_count = 15
        roles = list(Role.objects.all())

        for _ in range(person_count):
            person = Person.objects.create(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                notes=fake.text(max_nb_chars=50),
            )
            person.roles.set(
                random.sample(roles, k=random.randrange(1, len(roles))),  # noqa: S311
            )
            person.save()
