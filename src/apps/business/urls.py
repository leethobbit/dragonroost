from django.urls import path
from django.views.generic import TemplateView

from apps.business.views import (
    LocationCreateView,
    LocationDeleteView,
    LocationDetailView,
    LocationListView,
    LocationUpdateView,
)

app_name = 'business' # This is for namespacing the URLs later

urlpatterns = [
    path('locations/',LocationListView.as_view(), name="location-list"),
    path('locations/new/', LocationCreateView.as_view(), name="location-create"),
    path('locations/<int:pk>/detail/', LocationDetailView.as_view(), name="location-detail"),
    path('locations/<int:pk>/edit/', LocationUpdateView.as_view(), name="location-update"),
    path('locations/<int:pk>/delete/', LocationDeleteView.as_view(), name="location-delete"),
]