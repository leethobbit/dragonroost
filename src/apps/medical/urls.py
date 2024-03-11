from django.urls import path
from django.views.generic import TemplateView

from apps.animals.views import (
    AnimalCreateView,
    AnimalDeleteView,
    AnimalDetailView,
    AnimalListView,
    AnimalUpdateView,
)

app_name = "medical"  # This is for namespacing the URLs later

urlpatterns = []
