from django.urls import path

from dragonroost_ng.animals.views import AnimalCreateView
from dragonroost_ng.animals.views import AnimalDeleteView
from dragonroost_ng.animals.views import AnimalDetailView
from dragonroost_ng.animals.views import AnimalListView
from dragonroost_ng.animals.views import AnimalOutcomeView
from dragonroost_ng.animals.views import AnimalUpdateView
from dragonroost_ng.animals.views import HTMxAnimalTableDisplayView
from dragonroost_ng.animals.views import HTMxAnimalTableSearchView
from dragonroost_ng.animals.views import MedicalRecordCreateView
from dragonroost_ng.animals.views import MedicalRecordDeleteView
from dragonroost_ng.animals.views import SpeciesCreateView
from dragonroost_ng.animals.views import SpeciesDeleteView
from dragonroost_ng.animals.views import SpeciesDetailView
from dragonroost_ng.animals.views import SpeciesListView
from dragonroost_ng.animals.views import SpeciesUpdateView

app_name = "animals"  # This is for namespacing the URLs later

urlpatterns = [
    path("", AnimalListView.as_view(), name="animal-list"),
    path("new/", AnimalCreateView.as_view(), name="animal-create"),
    path("<int:pk>/detail/", AnimalDetailView.as_view(), name="animal-detail"),
    path("<int:pk>/edit/", AnimalUpdateView.as_view(), name="animal-update"),
    path("<int:pk>/outcome/", AnimalOutcomeView.as_view(), name="animal-outcome"),
    path("<int:pk>/delete/", AnimalDeleteView.as_view(), name="animal-delete"),
    path("table/", HTMxAnimalTableDisplayView.as_view(), name="animal-table"),
    path("table/search/", HTMxAnimalTableSearchView.as_view(), name="get_animal_list"),
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
    path(
        "<int:pk>/records/new/",
        MedicalRecordCreateView.as_view(),
        name="medical-record-create",
    ),
    path(
        "medical-records/<int:pk>/delete/",
        MedicalRecordDeleteView.as_view(),
        name="medical-record-delete",
    ),
]
