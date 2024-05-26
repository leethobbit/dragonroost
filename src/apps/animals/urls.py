from django.urls import path
from django.views.generic import TemplateView

from apps.animals.views import (
    AnimalCreateView,
    AnimalDeleteView,
    AnimalDetailView,
    AnimalHTMxTableView,
    AnimalListView,
    AnimalOutcomeView,
    AnimalUpdateView,
    MedicalRecordDeleteView,
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
    path("<int:pk>/outcome/", AnimalOutcomeView.as_view(), name="animal-outcome"),
    path("<int:pk>/delete/", AnimalDeleteView.as_view(), name="animal-delete"),
    path("search/", AnimalHTMxTableView.as_view(), name="animal-table"),
    path("species/", SpeciesListView.as_view(), name="species-list"),
    path("species/new/", SpeciesCreateView.as_view(), name="species-create"),
    path(
        "species/<int:pk>/detail/", SpeciesDetailView.as_view(), name="species-detail"
    ),
    path("species/<int:pk>/edit/", SpeciesUpdateView.as_view(), name="species-update"),
    path(
        "species/<int:pk>/delete/", SpeciesDeleteView.as_view(), name="species-delete"
    ),
    path(
        "medical-records/<int:pk>/delete/",
        MedicalRecordDeleteView.as_view(),
        name="medical-record-delete",
    ),
]
