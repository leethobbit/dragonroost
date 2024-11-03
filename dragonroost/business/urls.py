from django.urls import path

from dragonroost.business.views import FeedbackCreateView
from dragonroost.business.views import LocationCreateView
from dragonroost.business.views import LocationDeleteView
from dragonroost.business.views import LocationDetailView
from dragonroost.business.views import LocationListView
from dragonroost.business.views import LocationUpdateView
from dragonroost.business.views import MeetingCreateView
from dragonroost.business.views import MeetingDeleteView
from dragonroost.business.views import MeetingListView
from dragonroost.business.views import MeetingUpdateView

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
    path("feedback/new/", FeedbackCreateView.as_view(), name="feedback-create"),
]
