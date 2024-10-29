from django.urls import path

from dragonroost_ng.business.views import LocationCreateView
from dragonroost_ng.business.views import LocationDeleteView
from dragonroost_ng.business.views import LocationDetailView
from dragonroost_ng.business.views import LocationListView
from dragonroost_ng.business.views import LocationUpdateView
from dragonroost_ng.business.views import MeetingCreateView
from dragonroost_ng.business.views import MeetingDeleteView
from dragonroost_ng.business.views import MeetingListView
from dragonroost_ng.business.views import MeetingUpdateView

app_name = "business"  # This is for namespacing the URLs later

urlpatterns = [
    path("locations/", LocationListView.as_view(), name="location-table"),
    path("locations/new/", LocationCreateView.as_view(), name="location-create"),
    path(
        "locations/<int:pk>/detail/",
        LocationDetailView.as_view(),
        name="location-detail",
    ),
    path(
        "locations/<int:pk>/edit/",
        LocationUpdateView.as_view(),
        name="location-update",
    ),
    path(
        "locations/<int:pk>/delete/",
        LocationDeleteView.as_view(),
        name="location-delete",
    ),
    path("meetings/", MeetingListView.as_view(), name="meeting-table"),
    path("meetings/new/", MeetingCreateView.as_view(), name="meeting-create"),
    path("meetings/<int:pk>/edit/", MeetingUpdateView.as_view(), name="meeting-update"),
    path(
        "meetings/<int:pk>/delete/",
        MeetingDeleteView.as_view(),
        name="meeting-delete",
    ),
]