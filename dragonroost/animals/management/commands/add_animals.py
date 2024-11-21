import random
import secrets
from os import listdir
from pathlib import Path

from django.conf import settings
from django.core.management.base import BaseCommand
from faker import Faker
from measurement.measures import Weight

from dragonroost.animals.models import Animal
from dragonroost.animals.models import MedicalRecord
from dragonroost.animals.models import Species
from dragonroost.business.models import Location
from dragonroost.people.models import Person

fake = Faker()

MEDIA_ROOT = settings.MEDIA_ROOT


def random_image():
    dir_path = Path(MEDIA_ROOT) / "images/"
    files = [
        content for content in listdir(dir_path) if Path(dir_path / content).is_file()
    ]
    image = random.choice(files)  # noqa: S311
    return "images/" + str(image)


class Command(BaseCommand):
    help = "Create test data for Dragonroost."

    def add_arguments(self, parser):
        parser.add_argument(
            "-c",
            "--count",
            type=int,
            help="Number of animals to create.",
        )

    def handle(self, *args, **options):
        if options["count"]:
            self.create_animals(options["count"])
        self.stdout.write(self.style.SUCCESS("Test data created successfully!"))

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
                starting_weight=Weight(lb=random.randint(5, 35)),  # noqa: S311
                status=secrets.choice(statuses),
                animal_photo=random_image(),
            )
            animal.save()
            record_count = secrets.randbelow(6)
            for _i in range(record_count):
                medical_record = MedicalRecord.objects.create(
                    animal=animal,
                    notes=fake.text(max_nb_chars=50),
                    treatments=fake.text(max_nb_chars=75),
                    current_weight=Weight(lb=random.randint(7, 40)),  # noqa: S311
                    bowel_movement=fake.boolean(chance_of_getting_true=50),
                    q_volunteer=secrets.choice(people),
                )
                medical_record.save()
