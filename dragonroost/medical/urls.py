from django.urls import path

from .views import MedicalUpdateCreateView
from .views import MedicalUpdateDeleteView
from .views import MedicalUpdateDetailView
from .views import MedicalUpdateTableSearchView
from .views import MedicalUpdateTableView
from .views import MedicalUpdateUpdateView

app_name = "medical"

urlpatterns = [
    path(
        "updates/table/",
        MedicalUpdateTableView.as_view(),
        name="medical-update-table",
    ),
    path(
        "updates/table/search/",
        MedicalUpdateTableSearchView.as_view(),
        name="get-medical-update-results",
    ),
    path(
        "updates/new/",
        MedicalUpdateCreateView.as_view(),
        name="medical-update-create",
    ),
    path(
        "updates/<int:pk>/detail/",
        MedicalUpdateDetailView.as_view(),
        name="medical-update-detail",
    ),
    path(
        "updates/<int:pk>/edit/",
        MedicalUpdateUpdateView.as_view(),
        name="medical-update-update",
    ),
    path(
        "updates/<int:pk>/delete/",
        MedicalUpdateDeleteView.as_view(),
        name="medical-update-delete",
    ),
]
