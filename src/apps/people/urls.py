from django.urls import path
from django.views.generic import TemplateView

from apps.people.views import (
    PersonCreateView,
    PersonDeleteView,
    PersonDetailView,
    PersonHTMxView,
    PersonListView,
    PersonUpdateView,
)

app_name = "people"  # This is for namespacing the URLs later

urlpatterns = [
    path("", PersonListView.as_view(), name="person-list"),
    path("new/", PersonCreateView.as_view(), name="person-create"),
    path("<int:pk>/detail/", PersonDetailView.as_view(), name="person-detail"),
    path("<int:pk>/edit/", PersonUpdateView.as_view(), name="person-update"),
    path("<int:pk>/delete/", PersonDeleteView.as_view(), name="person-delete"),
    path("search/", PersonHTMxView.as_view(), name="person-table"),
]
