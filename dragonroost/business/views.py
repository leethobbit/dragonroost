import logging

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.views.generic.edit import DeleteView
from django.views.generic.edit import UpdateView
from django_tables2 import SingleTableMixin

from dragonroost.mixins import PageTitleViewMixin

from .forms import FeedbackForm
from .models import Feedback
from .models import Location
from .models import Meeting
from .tables import LocationListTable
from .tables import MeetingListTable

logger = logging.getLogger(__name__)


# Create your views here.
class LocationListView(
    SingleTableMixin,
    LoginRequiredMixin,
    PageTitleViewMixin,
    ListView,
):
    model = Location
    table_class = LocationListTable
    queryset = Location.objects.all().order_by("name")
    title = "Location List"
    context_object_name = "locations"

    def get_template_names(self):
        if self.request.htmx:
            template_name = "business/partials/location_table_htmx.html"
        else:
            template_name = "business/location_table_htmx_reload.html"
        return template_name


class LocationDetailView(LoginRequiredMixin, PageTitleViewMixin, DetailView):
    model = Location
    title = "Location Detail"
    template_name = "business/location_detail.html"
    context_object_name = "location"


class LocationCreateView(LoginRequiredMixin, PageTitleViewMixin, CreateView):
    model = Location
    title = "Create Location"
    template_name = "business/business_form.html"
    fields = ("name", "description")

    def get_success_url(self):
        return reverse_lazy("business:location-detail", kwargs={"pk": self.object.id})


class LocationUpdateView(LoginRequiredMixin, PageTitleViewMixin, UpdateView):
    model = Location
    template_name = "business/business_form.html"
    title = "Edit Location"
    fields = ("name", "description")

    def get_success_url(self):
        return reverse_lazy("business:location-detail", kwargs={"pk": self.object.id})


class LocationDeleteView(LoginRequiredMixin, PageTitleViewMixin, DeleteView):
    model = Location
    title = "Delete Location"
    template_name = "business/location_confirm_delete.html"
    success_url = reverse_lazy("business:location-list")


class MeetingListView(
    SingleTableMixin,
    LoginRequiredMixin,
    PageTitleViewMixin,
    ListView,
):
    model = Meeting
    table_class = MeetingListTable
    queryset = Meeting.objects.all().order_by("-date")
    title = "Meeting List"
    context_object_name = "meetings"

    def get_template_names(self):
        if self.request.htmx:
            template_name = "business/partials/meeting_table_htmx.html"
        else:
            template_name = "business/meeting_table_htmx_reload.html"
        return template_name


class MeetingCreateView(LoginRequiredMixin, PageTitleViewMixin, CreateView):
    model = Meeting
    title = "Create Meeting"
    template_name = "business/business_form.html"
    fields = ("title", "meeting_url", "minutes")

    def get_success_url(self):
        return reverse_lazy("business:meeting-table")


class MeetingUpdateView(LoginRequiredMixin, PageTitleViewMixin, UpdateView):
    model = Meeting
    template_name = "business/business_form.html"
    title = "Edit Meeting"
    fields = ("title", "meeting_url", "minutes")

    def get_success_url(self):
        return reverse_lazy("business:meeting-table")


class MeetingDeleteView(LoginRequiredMixin, PageTitleViewMixin, DeleteView):
    model = Meeting
    title = "Delete Meeting"
    template_name = "business/meeting_confirm_delete.html"
    success_url = reverse_lazy("business:meeting-table")


class FeedbackCreateView(LoginRequiredMixin, PageTitleViewMixin, CreateView):
    model = Feedback
    title = "Submit Feedback"
    template_name = "business/feedback_form.html"
    fields = ("name", "email_address", "feedback_type", "feedback")

    def post(self, request, *args, **kwargs):
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse(status=204)
        return render(request, "business/feedback_form.html", {"form": form})
