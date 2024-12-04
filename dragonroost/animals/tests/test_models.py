import pytest

from dragonroost.animals.models import Animal
from dragonroost.animals.models import MedicalRecord


# Animal model tests
@pytest.mark.django_db
def test_animal_queryset_get_available_animals(animals):
    qs = Animal.objects.get_available_animals()
    assert qs.count() > 0
    assert all(animal.status == "AVAILABLE" for animal in qs)


@pytest.mark.django_db
def test_animal_queryset_get_animals_needing_medical_attention(animals):
    qs = Animal.objects.get_animals_needing_medical_attention()
    assert qs.count() > 0
    assert all(animal.status == "QUARANTINE" for animal in qs)


@pytest.mark.django_db
def test_animal_str_method(animal):
    assert str(animal) == animal.name


@pytest.mark.django_db
def test_animal_get_absolute_url(animal):
    assert animal.get_absolute_url() == f"/animals/{animal.pk}/"


@pytest.mark.django_db
def test_animal_get_animal_tag(animal):
    assert animal.animal_tag == f"A-{animal.pk:05d}"


@pytest.mark.django_db
def test_animal_is_available(animal_is_available):
    assert animal_is_available.is_available is True


@pytest.mark.django_db
def test_animal_number_of_medical_records(medical_record):
    animal = medical_record.animal
    number_of_records = 1
    assert animal.number_of_medical_records == number_of_records


@pytest.mark.django_db
def test_animal_latest_medical_record(medical_record):
    animal = medical_record.animal
    latest_medical_record = MedicalRecord.objects.filter(animal=animal).latest(
        "created",
    )
    assert animal.latest_medical_record == latest_medical_record


# Species model tests
@pytest.mark.django_db
def test_species_str_method(species):
    assert str(species) == species.name


@pytest.mark.django_db
def test_species_get_absolute_url(species):
    assert species.get_absolute_url() == f"/animals/species/{species.pk}/detail/"


# MedicalRecord model tests
@pytest.mark.django_db
def test_medical_record_str_method(medical_record):
    assert str(medical_record) == medical_record.notes
