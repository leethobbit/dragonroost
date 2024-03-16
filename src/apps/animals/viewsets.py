from django.utils.translation import gettext_lazy as _

from viewflow import Icon
from viewflow.forms import Layout, FieldSet, Row, FormDependentSelectMixin
from viewflow.urls import (
    Application, DetailViewMixin, DeleteViewMixin,
    ModelViewset, ReadonlyModelViewset, UpdateViewMixin
)

from . import models

class AnimalViewSet(DeleteViewMixin, ModelViewset):
    icon = Icon('pets')
    model = models.Animal
    title = "Animals"

    list_columns = ('name', 'species','description', 'status', 'location', 'medical_record')
    list_filter_fields = ('status', 'species',)


class SpeciesViewSet(DeleteViewMixin, ModelViewset):
    icon = Icon('biotech')
    model = models.Species
    title = "Species"

# class CityViewset(DetailViewMixin, DeleteViewMixin, ModelViewset):
#     icon = Icon('location_city')
#     model = models.City
#     list_columns = ('name', 'country', 'population')
#     list_filter_fields = ('is_capital', 'country', )
#     list_search_fields = ['name']
#     queryset = model._default_manager.select_related('country')
#     try:
#         from viewflow.forms import AjaxModelSelect
#         form_widgets = {
#             'country': AjaxModelSelect(lookups=['name__istartswith'])
#         }
#     except ImportError:
#         # pro-only
#         pass