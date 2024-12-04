import pytest

from dragonroost.animals.models import Animal
from dragonroost.animals.models import MedicalRecord
from dragonroost.animals.models import Species
from dragonroost.animals.tests.factories import AnimalFactory
from dragonroost.animals.tests.factories import MedicalRecordFactory
from dragonroost.animals.tests.factories import SpeciesFactory
from dragonroost.users.models import User
from dragonroost.users.tests.factories import UserFactory


@pytest.fixture(autouse=True)
def _media_storage(settings, tmpdir) -> None:
    settings.MEDIA_ROOT = tmpdir.strpath


@pytest.fixture
def user(db) -> User:
    return UserFactory()


@pytest.fixture
def species(db) -> Species:
    return SpeciesFactory.create()


@pytest.fixture
def animal(db) -> Animal:
    return AnimalFactory()


@pytest.fixture
def animals(db) -> Animal:
    return AnimalFactory.create_batch(5)


@pytest.fixture
def animal_is_available(db) -> Animal:
    return AnimalFactory.create(status="AVAILABLE")


@pytest.fixture
def medical_record(db) -> MedicalRecord:
    return MedicalRecordFactory()
