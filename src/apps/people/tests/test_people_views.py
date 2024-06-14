import pytest
from django.urls import reverse
from pytest_django.asserts import assertContains, assertRedirects

from apps.people.models import Person
from tests.factories import PersonFactory, RoleFactory


# Person TESTS #
def test_person_list_view_success(client, admin_user):
    url = reverse("people:person-list")
    client.force_login(admin_user)
    response = client.get(url)
    content = response.content.decode(response.charset)
    assert "Roles" in content


def test_person_list_view_fail(client):
    url = reverse("people:person-list")
    response = client.get(url)
    content = response.content.decode(response.charset)
    assert "Wabbajack" not in content


@pytest.mark.django_db
def test_person_create_view(client, admin_user):
    client.force_login(admin_user)
    role = RoleFactory()
    response = client.post(
        reverse("people:person-create"),
        {
            "first_name": "Billy",
            "last_name": "Bob",
            "email": "billybob@me.com",
            "phone_number": "555-555-5555",
            "roles": [role.id],
            "address": "123 Fake Street",
            "zip_code": "12345",
            "notes": "Some notes",
        },
    )
    assert Person.objects.count() == 1
    assert Person.objects.last().first_name == "Billy"
    assertRedirects(
        response, reverse("people:person-detail", kwargs={"pk": 1}), status_code=302
    )


@pytest.mark.django_db
def test_person_detail_view(client, admin_user):
    test_person = PersonFactory()
    assert Person.objects.count() == 1
    uri = reverse("people:person-detail", kwargs={"pk": test_person.id})
    client.force_login(admin_user)
    resp = client.get(uri)
    content = resp.content.decode(resp.charset)
    assert test_person.first_name in content


@pytest.mark.django_db
def test_person_update_view(client, admin_user):
    client.force_login(admin_user)
    role = RoleFactory()
    test_person = PersonFactory()
    response = client.post(
        reverse("people:person-update", kwargs={"pk": test_person.id}),
        {
            "first_name": "Billy",
            "last_name": "Bob",
            "email": "billybob@me.com",
            "phone_number": "555-555-5555",
            "roles": [role.id],
            "address": "123 Fake Street",
            "zip_code": "12345",
            "notes": "Some notes",
        },
    )
    assert Person.objects.count() == 1
    assert Person.objects.last().first_name == "Billy"
    assertRedirects(
        response,
        reverse("people:person-detail", kwargs={"pk": test_person.id}),
        status_code=302,
    )


@pytest.mark.django_db
def test_person_delete_view(client, admin_user):
    client.force_login(admin_user)

    person = PersonFactory()

    response = client.get(reverse("people:person-delete", kwargs={"pk": person.id}))
    assertContains(response, "Are you sure you want to delete")

    post_response = client.post(
        reverse("people:person-delete", kwargs={"pk": person.id})
    )
    assertRedirects(post_response, reverse("people:person-list"), status_code=302)
