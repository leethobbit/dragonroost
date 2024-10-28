from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.views.generic.edit import DeleteView
from django.views.generic.edit import UpdateView
from django_tables2 import SingleTableMixin

from dragonroost_ng.mixins import PageTitleViewMixin

from .models import Location
from .models import Meeting
from .tables import LocationListTable
from .tables import MeetingListTable


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
    template_name = "business/location_list.html"
    title = "Location List"
    context_object_name = "locations"


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
        return reverse_lazy("business:location_detail", kwargs={"pk": self.object.id})


class LocationUpdateView(LoginRequiredMixin, PageTitleViewMixin, UpdateView):
    model = Location
    template_name = "business/business_form.html"
    title = "Edit Location"
    fields = ("name", "description")

    def get_success_url(self):
        return reverse_lazy("business:location_detail", kwargs={"pk": self.object.id})


class LocationDeleteView(LoginRequiredMixin, PageTitleViewMixin, DeleteView):
    model = Location
    title = "Delete Location"
    template_name = "business/location_confirm_delete.html"
    success_url = reverse_lazy("business:location_list")


class MeetingListView(
    SingleTableMixin,
    LoginRequiredMixin,
    PageTitleViewMixin,
    ListView,
):
    model = Meeting
    table_class = MeetingListTable
    queryset = Meeting.objects.all().order_by("-date")
    template_name = "business/meeting_list.html"
    title = "Meeting List"
    context_object_name = "meetings"


class MeetingCreateView(LoginRequiredMixin, PageTitleViewMixin, CreateView):
    model = Meeting
    title = "Create Meeting"
    template_name = "business/business_form.html"
    fields = ("title", "minutes")

    def get_success_url(self):
        return reverse_lazy("business:meeting_list")


class MeetingUpdateView(LoginRequiredMixin, PageTitleViewMixin, UpdateView):
    model = Meeting
    template_name = "business/business_form.html"
    title = "Edit Meeting"
    fields = ("title", "minutes")

    def get_success_url(self):
        return reverse_lazy("business:meeting_list")


class MeetingDeleteView(LoginRequiredMixin, PageTitleViewMixin, DeleteView):
    model = Meeting
    title = "Delete Meeting"
    template_name = "business/meeting_confirm_delete.html"
    success_url = reverse_lazy("business:meeting_list")
