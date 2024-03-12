from django.urls import path
from django.views.generic import TemplateView

from apps.animals.views import (
    AnimalCreateView,
    AnimalDeleteView,
    AnimalDetailView,
    AnimalListView,
    AnimalUpdateView,
    SpeciesCreateView,
    SpeciesDeleteView,
    SpeciesDetailView,
    SpeciesListView,
    SpeciesUpdateView,
)

app_name = "animals"  # This is for namespacing the URLs later

urlpatterns = [
    path("", AnimalListView.as_view(), name="animal-list"),
    path("new/", AnimalCreateView.as_view(), name="animal-create"),
    path("<int:pk>/detail/", AnimalDetailView.as_view(), name="animal-detail"),
    path("<int:pk>/edit/", AnimalUpdateView.as_view(), name="animal-update"),
    path("<int:pk>/delete/", AnimalDeleteView.as_view(), name="animal-delete"),
    path("species/new/", SpeciesCreateView.as_view(), name="species-create"),
    path(
        "species/<int:pk>/detail/", SpeciesDetailView.as_view(), name="species-detail"
    ),
    path("species/<int:pk>/edit/", SpeciesUpdateView.as_view(), name="species-update"),
    path(
        "species/<int:pk>/delete/", SpeciesDeleteView.as_view(), name="species-delete"
    ),
]
