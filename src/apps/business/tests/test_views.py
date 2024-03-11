import pytest
from django.urls import reverse
from pytest_django.asserts import assertRedirects

from apps.business.models import Location
from tests.factories import LocationFactory

# LOCATION TESTS #
    
@pytest.mark.django_db
def test_location_detail_view(client, admin_user):
    test_object = LocationFactory()
    assert Location.objects.count() == 1
    uri = reverse('business:location-detail', kwargs={"pk": test_object.id})
    client.force_login(admin_user)
    resp = client.get(uri)
    content = resp.content.decode(resp.charset)
    assert f'Detail' in content