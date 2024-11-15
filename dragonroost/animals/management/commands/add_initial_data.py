import random

from django.core.management.base import BaseCommand
from faker import Faker

from dragonroost.animals.models import Animal
from dragonroost.animals.models import Species
from dragonroost.business.models import Location

fake = Faker()


class Command(BaseCommand):
    help = "Create test data for Dragonroost."

    def add_arguments(self, parser):
        parser.add_argument(
            "--initial",
            help="Create initial data before animals can be added.",
        )
        parser.add_argument("--animals", type=int, help="Number of animals to create.")

    def handle(self, *args, **options):
        if options["initial"]:
            """
            Create all initial data EXCEPT animals.
            """
            self.create_species()
            self.create_locations()
        if options["animals"]:
            self.create_animals(options["animals"])
        self.stdout.write(self.style.SUCCESS("Test data created successfully!"))

    def create_species():
        species_names = [
            "Corn Snake",
            "Red-eared Slider",
            "Ball Python",
            "Bearded Dragon",
        ]

        for name in species_names:
            Species.objects.get_or_create(
                name=name,
                description=fake.text(max_nb_chars=20),
                is_ohio_native=fake.boolean(chance_of_getting_true=25),
            )

    def create_locations():
        location_names = ["Sales Floor", "Q Room", "Upstairs"]

        for name in location_names:
            Location.objects.get_or_create(
                name=name,
                description=fake.text(max_nb_chars=20),
            )

    def create_animals(self, count):
        species = list(Species.objects.all())
        locations = list(Location.objects.all())

        for _ in range(count):
            animal = Animal.objects.create(
                name=fake.unique.first_name(),
                description=fake.text(max_nb_chars=50),
                species=random.choice(species),  # noqa: S311
                location=random.choice(locations),  # noqa: S311
                color=fake.color(),
                donation_fee=random.uniform(5.00, 350.00),  # noqa: S311
                age=random.uniform(1, 50),  # noqa: S311
                starting_weight=random.uniform(1, 200),  # noqa: S311
                intake_date=fake.date_time_this_year(),
            )
            animal.save()
