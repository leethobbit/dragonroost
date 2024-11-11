from django.urls import path

from dragonroost.animals.views import AnimalCreateView
from dragonroost.animals.views import AnimalDeleteView
from dragonroost.animals.views import AnimalDetailView
from dragonroost.animals.views import AnimalOutcomeView
from dragonroost.animals.views import AnimalUpdateView
from dragonroost.animals.views import HTMxAnimalTableDisplayView
from dragonroost.animals.views import HTMxAnimalTableSearchView
from dragonroost.animals.views import MedicalRecordCreateView
from dragonroost.animals.views import MedicalRecordDeleteView
from dragonroost.animals.views import MedicalRecordUpdateView
from dragonroost.animals.views import SpeciesCreateView
from dragonroost.animals.views import SpeciesDeleteView
from dragonroost.animals.views import SpeciesDetailView
from dragonroost.animals.views import SpeciesListView
from dragonroost.animals.views import SpeciesTableView
from dragonroost.animals.views import SpeciesUpdateView

app_name = "animals"  # This is for namespacing the URLs later

urlpatterns = [
    path("new/", AnimalCreateView.as_view(), name="animal-create"),
    path("<int:pk>/detail/", AnimalDetailView.as_view(), name="animal-detail"),
    path("<int:pk>/edit/", AnimalUpdateView.as_view(), name="animal-update"),
    path("<int:pk>/outcome/", AnimalOutcomeView.as_view(), name="animal-outcome"),
    path("<int:pk>/delete/", AnimalDeleteView.as_view(), name="animal-delete"),
    path("table/", HTMxAnimalTableDisplayView.as_view(), name="animal-table"),
    path("table/search/", HTMxAnimalTableSearchView.as_view(), name="get-animal-list"),
    path("species/", SpeciesListView.as_view(), name="species-table"),
    path("species/new/", SpeciesCreateView.as_view(), name="species-create"),
    path(
        "species/<int:pk>/detail/",
        SpeciesDetailView.as_view(),
        name="species-detail",
    ),
    path("species/<int:pk>/edit/", SpeciesUpdateView.as_view(), name="species-update"),
    path(
        "species/<int:pk>/delete/",
        SpeciesDeleteView.as_view(),
        name="species-delete",
    ),
    path("species/table/", SpeciesTableView.as_view(), name="species-table-partial"),
    path(
        "records/<int:pk>/new/",
        MedicalRecordCreateView.as_view(),
        name="medical-record-create",
    ),
    path(
        "records/<int:pk>/edit/",
        MedicalRecordUpdateView.as_view(),
        name="medical-record-update",
    ),
    path(
        "records/<int:pk>/delete/",
        MedicalRecordDeleteView.as_view(),
        name="medical-record-delete",
    ),
]
