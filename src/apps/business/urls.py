from django.urls import path
from django.views.generic import TemplateView

from apps.business.views import (
    LocationCreateView,
    LocationDeleteView,
    LocationDetailView,
    LocationListView,
    LocationUpdateView,
    MeetingCreateView,
    MeetingDeleteView,
    MeetingListView,
    MeetingUpdateView,
)

app_name = "business"  # This is for namespacing the URLs later

urlpatterns = [
    path("locations/", LocationListView.as_view(), name="location_list"),
    path("locations/new/", LocationCreateView.as_view(), name="location_create"),
    path(
        "locations/<int:pk>/detail/",
        LocationDetailView.as_view(),
        name="location_detail",
    ),
    path(
        "locations/<int:pk>/edit/", LocationUpdateView.as_view(), name="location_update"
    ),
    path(
        "locations/<int:pk>/delete/",
        LocationDeleteView.as_view(),
        name="location_delete",
    ),
    path("meetings/", MeetingListView.as_view(), name="meeting_list"),
    path("meetings/new/", MeetingCreateView.as_view(), name="meeting_create"),
    path("meetings/<int:pk>/edit/", MeetingUpdateView.as_view(), name="meeting_update"),
    path(
        "meetings/<int:pk>/delete/",
        MeetingDeleteView.as_view(),
        name="meeting_delete",
    ),
]
