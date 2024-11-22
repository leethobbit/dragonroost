import logging

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.views.generic.edit import DeleteView
from django.views.generic.edit import UpdateView
from django_tables2 import SingleTableMixin

from dragonroost.mixins import PageTitleViewMixin

from .forms import FeedbackForm
from .forms import LocationForm
from .forms import MeetingForm
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
            template_name = "business/location_table_htmx.html"
        else:
            template_name = "business/location_table_htmx_reload.html"
        return template_name


class LocationTableView(LoginRequiredMixin, SingleTableMixin, ListView):
    table_class = LocationListTable
    queryset = Location.objects.all().order_by("name")
    paginate_by = 15
    template_name = "business/partials/table_partial.html"


class LocationDetailView(LoginRequiredMixin, PageTitleViewMixin, DetailView):
    model = Location
    title = "Location Detail"
    template_name = "business/location_detail.html"
    context_object_name = "location"


class LocationCreateView(LoginRequiredMixin, PageTitleViewMixin, CreateView):
    model = Location
    form_class = LocationForm
    title = "Create Location"
    template_name = "business/business_form.html"

    def post(self, request, *args, **kwargs):
        form = LocationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse(
                status=204,
                headers={"HX-Trigger": "location_table_update"},
            )
        return render(request, "business/business_form.html", {"form": form})


class LocationUpdateView(LoginRequiredMixin, PageTitleViewMixin, UpdateView):
    model = Location
    form_class = LocationForm
    template_name = "business/business_form.html"
    title = "Edit Location"

    def post(self, request, *args, **kwargs):
        location = get_object_or_404(Location, pk=self.kwargs["pk"])
        form = LocationForm(request.POST, instance=location)
        if form.is_valid():
            form.save()
            return HttpResponse(
                status=204,
                headers={"HX-Trigger": "location_table_update"},
            )
        return render(
            request,
            "business/business_form.html",
            {
                "form": form,
                "location": location,
            },
        )


class LocationDeleteView(LoginRequiredMixin, PageTitleViewMixin, DeleteView):
    model = Location
    title = "Delete Location"
    template_name = "business/location_confirm_delete.html"

    def post(self, request, *args, **kwargs):
        location = get_object_or_404(Location, pk=self.kwargs["pk"])
        location.delete()

        return HttpResponse(
            status=204,
            headers={"HX-Trigger": "location_table_update"},
        )


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
            template_name = "business/meeting_table_htmx.html"
        else:
            template_name = "business/meeting_table_htmx_reload.html"
        return template_name


class MeetingTableView(LoginRequiredMixin, SingleTableMixin, ListView):
    table_class = MeetingListTable
    queryset = Meeting.objects.all().order_by("-date")
    paginate_by = 15
    template_name = "business/partials/table_partial.html"


class MeetingCreateView(LoginRequiredMixin, PageTitleViewMixin, CreateView):
    model = Meeting
    form_class = MeetingForm
    title = "Create Meeting"
    template_name = "business/business_form.html"

    def post(self, request, *args, **kwargs):
        form = MeetingForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse(
                status=204,
                headers={"HX-Trigger": "meeting_table_update"},
            )
        return render(request, "business/business_form.html", {"form": form})


class MeetingUpdateView(LoginRequiredMixin, PageTitleViewMixin, UpdateView):
    model = Meeting
    form_class = MeetingForm
    template_name = "business/business_form.html"
    title = "Edit Meeting"

    def post(self, request, *args, **kwargs):
        meeting = get_object_or_404(Meeting, pk=self.kwargs["pk"])
        form = MeetingForm(request.POST, instance=meeting)
        if form.is_valid():
            form.save()
            return HttpResponse(
                status=204,
                headers={"HX-Trigger": "meeting_table_update"},
            )
        return render(
            request,
            "business/business_form.html",
            {
                "form": form,
                "meeting": meeting,
            },
        )


class MeetingDeleteView(LoginRequiredMixin, PageTitleViewMixin, DeleteView):
    model = Meeting
    title = "Delete Meeting"
    template_name = "business/meeting_confirm_delete.html"

    def post(self, request, *args, **kwargs):
        meeting = get_object_or_404(Meeting, pk=self.kwargs["pk"])
        meeting.delete()

        return HttpResponse(
            status=204,
            headers={"HX-Trigger": "meeting_table_update"},
        )


class FeedbackCreateView(LoginRequiredMixin, PageTitleViewMixin, CreateView):
    """
    Form for sending feedback to the database for the admin to view.
    TODO: Fix the form showing blank if the browser's back button is used.
    """

    model = Feedback
    form_class = FeedbackForm
    title = "Submit Feedback"
    template_name = "business/feedback_form.html"

    def post(self, request, *args, **kwargs):
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse(status=204)
        return render(request, "business/feedback_form.html", {"form": form})
