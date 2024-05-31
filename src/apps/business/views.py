from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django_tables2 import SingleTableMixin

from dragonroost.mixins import PageTitleViewMixin

from .models import Location, Meeting
from .tables import LocationListTable, MeetingListTable


# Create your views here.
class LocationListView(SingleTableMixin, LoginRequiredMixin, PageTitleViewMixin, ListView):
    model = Location
    table_class = LocationListTable
    queryset = Location.objects.all().order_by("name")
    template_name = "business/location-list.html"
    title = "Location List"
    context_object_name = "locations"

class LocationDetailView(LoginRequiredMixin, PageTitleViewMixin, DetailView):
    model = Location
    title = "Location Detail"
    template_name = "business/location-detail.html"
    context_object_name = "location"


class LocationCreateView(LoginRequiredMixin, PageTitleViewMixin, CreateView):
    model = Location
    title = "Create Location"
    template_name = "business/business-form.html"
    fields = ("name", "description")

    def get_success_url(self):
        return reverse_lazy("business:location-detail", kwargs={"pk": self.object.id})


class LocationUpdateView(LoginRequiredMixin, PageTitleViewMixin, UpdateView):
    model = Location
    template_name = "business/business-form.html"
    title = "Edit Location"
    fields = ("name", "description")

    def get_success_url(self):
        return reverse_lazy("business:location-detail", kwargs={"pk": self.object.id})


class LocationDeleteView(LoginRequiredMixin, PageTitleViewMixin, DeleteView):
    model = Location
    title = "Delete Location"
    template_name = "business/location-confirm-delete.html"
    success_url = reverse_lazy("business:location-list")

class MeetingListView(SingleTableMixin, LoginRequiredMixin, PageTitleViewMixin, ListView):
    model = Meeting
    table_class = MeetingListTable
    queryset = Meeting.objects.all().order_by("-date")
    template_name = "business/meeting-list.html"
    title = "Meeting List"
    context_object_name = "meetings"

class MeetingCreateView(LoginRequiredMixin, PageTitleViewMixin, CreateView):
    model = Meeting
    title = "Create Meeting"
    template_name = "business/business-form.html"
    fields = ("title", "minutes")

    def get_success_url(self):
        return reverse_lazy("business:meeting-list")

class MeetingUpdateView(LoginRequiredMixin, PageTitleViewMixin, UpdateView):
    model = Meeting
    template_name = "business/business-form.html"
    title = "Edit Meeting"
    fields = ("title", "minutes")

    def get_success_url(self):
        return reverse_lazy("business:meeting-list")

class MeetingDeleteView(LoginRequiredMixin, PageTitleViewMixin, DeleteView):
    model = Meeting
    title = "Delete Meeting"
    template_name = "business/meeting-confirm-delete.html"
    success_url = reverse_lazy("business:meeting-list")