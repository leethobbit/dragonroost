from django.urls import path

from .views import MedicalUpdateCreateView
from .views import MedicalUpdateDeleteView
from .views import MedicalUpdateDetailView
from .views import MedicalUpdateTableView
from .views import MedicalUpdateUpdateView

app_name = "medical"

urlpatterns = [
    path("", MedicalUpdateTableView.as_view(), name="person-table"),
    path("new/", MedicalUpdateCreateView.as_view(), name="person-create"),
    path("<int:pk>/detail/", MedicalUpdateDetailView.as_view(), name="person-detail"),
    path("<int:pk>/edit/", MedicalUpdateUpdateView.as_view(), name="person-update"),
    path("<int:pk>/delete/", MedicalUpdateDeleteView.as_view(), name="person-delete"),
]
