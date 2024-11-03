from django.urls import path

from .views import MedicalUpdateCreateView
from .views import MedicalUpdateDeleteView
from .views import MedicalUpdateDetailView
from .views import MedicalUpdateTableView
from .views import MedicalUpdateUpdateView

app_name = "medical"

urlpatterns = [
    path("", MedicalUpdateTableView.as_view(), name="medical-update-table"),
    path("new/", MedicalUpdateCreateView.as_view(), name="medical-update-create"),
    path(
        "<int:pk>/detail/",
        MedicalUpdateDetailView.as_view(),
        name="medical-update-detail",
    ),
    path(
        "<int:pk>/edit/",
        MedicalUpdateUpdateView.as_view(),
        name="medical-update-update",
    ),
    path(
        "<int:pk>/delete/",
        MedicalUpdateDeleteView.as_view(),
        name="medical-update-delete",
    ),
]
