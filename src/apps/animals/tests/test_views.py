import pytest
from django.urls import reverse
from pytest_django.asserts import assertContains, assertRedirects

from apps.animals.models import Animal, Species, Status
from tests.factories import (
    AnimalFactory,
    LocationFactory,
    SpeciesFactory,
    StatusFactory,
)

# MISC TESTS #

@pytest.mark.django_db
def test_login_page(client, django_user_model):
    username = "user1"
    password = "bar"
    user = django_user_model.objects.create_user(username=username, password=password)
    client.force_login(user)
    response = client.post("/accounts/login/")
    assert response.status_code == 200

# ANIMAL TESTS #
    
def test_animal_list_view_success(client, admin_user):
    uri = reverse('animals:animal-list')
    client.force_login(admin_user)
    resp = client.get(uri)
    content = resp.content.decode(resp.charset)
    assert 'Animal List' in content

def test_animal_list_view_fail(client):
    uri = reverse('animals:animal-list')
    resp = client.get(uri)
    content = resp.content.decode(resp.charset)
    assert 'Animal List' not in content

@pytest.mark.django_db
def test_animal_create_view(client, admin_user):
    client.force_login(admin_user)

    species = SpeciesFactory()
    status = StatusFactory()
    location = LocationFactory()

    response = client.post(reverse('animals:animal-create'), {
        'name': 'Test Animal',
        'description': 'Test animal description',
        'donation_fee': 10.22,
        'color': 'Blue',
        'sex': 'MALE',
        'age': 73,
        'diet': 'MIXED',
        'species': species.id,
        'status': status.id,
        'location': location.id,
    })
    assert Species.objects.count() == 1
    assert Animal.objects.last().name == 'Test Animal'
    assertRedirects(response, reverse('animals:animal-detail', kwargs={'pk': 1}), status_code=302)

@pytest.mark.django_db
def test_animal_detail_view(client, admin_user):
    test_animal = AnimalFactory()
    assert Animal.objects.count() == 1
    uri = reverse('animals:animal-detail', kwargs={"pk": test_animal.id})
    client.force_login(admin_user)
    resp = client.get(uri)
    content = resp.content.decode(resp.charset)
    assert f'Detail' in content

@pytest.mark.django_db
def test_animal_update_view(client, admin_user):
    client.force_login(admin_user)

    animal = AnimalFactory()

    response = client.post(reverse('animals:animal-update', kwargs={'pk': animal.id}), {
        'name': 'Test Animal',
        'description': 'Test animal description EDITED',
        'donation_fee': 10.22,
        'color': 'Blue',
        'sex': 'MALE',
        'age': 73,
        'diet': 'MIXED',
        'species': animal.species.id,
        'status': animal.status.id,
        'location': animal.location.id,
    })
    assert Animal.objects.last().sex == 'MALE'
    assertRedirects(response, reverse('animals:animal-detail', kwargs={'pk': animal.id}), status_code=302)

@pytest.mark.django_db
def test_animal_delete_view(client, admin_user):
    client.force_login(admin_user)

    animal = AnimalFactory()

    response = client.get(reverse('animals:animal-delete', kwargs={'pk': animal.id}))
    assertContains(response, 'Are you sure you want to delete')

    post_response = client.post(reverse('animals:animal-delete', kwargs={'pk': animal.id}))
    assertRedirects(post_response, reverse('animals:animal-list'), status_code=302)

# SPECIES TESTS #

@pytest.mark.django_db
def test_species_create_view(client, admin_user):
    client.force_login(admin_user)

    response = client.post(reverse('animals:species-create'), {
        'name': 'Test Species',
        'description': 'Test species description',
        'class_name': 'BIRD',
    })
    assert Species.objects.last().name == 'Test Species'
    assertRedirects(response, reverse('animals:species-detail', kwargs={'pk': Species.objects.last().id}), status_code=302)
    
@pytest.mark.django_db
def test_species_detail_view(client, admin_user):
    test_object = SpeciesFactory()
    assert Species.objects.count() == 1
    uri = reverse('animals:species-detail', kwargs={"pk": test_object.id})
    client.force_login(admin_user)
    resp = client.get(uri)
    content = resp.content.decode(resp.charset)
    assert f'Detail' in content

@pytest.mark.django_db
def test_species_update_view(client, admin_user):
    client.force_login(admin_user)

    species = SpeciesFactory()

    response = client.post(reverse('animals:species-update', kwargs={'pk': species.id}), {
        'name': 'Test Species',
        'description': 'Edited test description',
        'class_name': 'MAMMAL',
    })
    assert Species.objects.last().description == 'Edited test description'
    assertRedirects(response, reverse('animals:species-detail', kwargs={'pk': species.id}), status_code=302)


@pytest.mark.django_db
def test_species_delete_view(client, admin_user):
    client.force_login(admin_user)

    species = SpeciesFactory()

    response = client.get(reverse('animals:species-delete', kwargs={'pk': species.id}))
    assertContains(response, 'Are you sure you want to delete')

    post_response = client.post(reverse('animals:species-delete', kwargs={'pk': species.id}))
    assertRedirects(post_response, reverse('home-list'), status_code=302)

# STATUS TESTS #

@pytest.mark.django_db
def test_status_create_view(client, admin_user):
    client.force_login(admin_user)
    response = client.post('/animals/status/new/', {'name':'Test Status', 'description':'Test status description'})
    assert response.status_code == 302
    assert Status.objects.last().name == 'Test Status'

@pytest.mark.django_db
@pytest.mark.skip(reason="Not implemented yet")
def test_status_detail_view(client, admin_user):
    pass

@pytest.mark.django_db
@pytest.mark.skip(reason="Not implemented yet")
def test_status_update_view(client, admin_user):
    pass

@pytest.mark.django_db
@pytest.mark.skip(reason="Not implemented yet")
def test_status_delete_view(client, admin_user):
    pass