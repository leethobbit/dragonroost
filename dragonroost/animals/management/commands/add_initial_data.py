import random
import secrets

from django.core.management.base import BaseCommand
from faker import Faker

from dragonroost.animals.models import Animal
from dragonroost.animals.models import MedicalRecord
from dragonroost.animals.models import Species
from dragonroost.business.models import Location
from dragonroost.people.models import Person

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
        people = list(Person.objects.all())
        names = [fake.unique.first_name() for i in range(200)]

        statuses = [
            "ADOPTED",
            "AMBASSADOR",
            "AVAILABLE",
            "DECEASED",
            "FOSTERED",
            "MEDICAL_HOLD",
            "ON_HOLD",
            "QUARANTINE",
        ]

        for i in range(count):
            animal = Animal.objects.create(
                name=names[i],
                description=fake.text(max_nb_chars=50),
                species=secrets.choice(species),
                location=secrets.choice(locations),
                color=fake.color(),
                donation_fee=random.uniform(5.00, 350.00),  # noqa: S311
                age=random.uniform(1, 50),  # noqa: S311
                starting_weight=random.uniform(1, 200),  # noqa: S311
                status=secrets.choice(statuses),
            )
            animal.save()
            record_count = secrets.randbelow(6)
            for _i in range(record_count):
                medical_record = MedicalRecord.objects.create(
                    animal=animal,
                    notes=fake.text(max_nb_chars=50),
                    treatments=fake.text(max_nb_chars=75),
                    current_weight=random.uniform(1, 200),  # noqa: S311
                    bowel_movement=fake.boolean(chance_of_getting_true=50),
                    q_volunteer=secrets.choice(people),
                )
                medical_record.save()
