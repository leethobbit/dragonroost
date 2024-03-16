from django.utils.translation import gettext_lazy as _

from viewflow import Icon
from viewflow.forms import Layout, FieldSet, Row
from viewflow.urls import (
    Application, DetailViewMixin, DeleteViewMixin,
    ModelViewset, ReadonlyModelViewset
)

from . import models

class LocationViewSet(DetailViewMixin, DeleteViewMixin, ModelViewset):
    icon = Icon('location_city')
    model = models.Location
    title = "Locations"