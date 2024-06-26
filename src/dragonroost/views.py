import datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q, Sum
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from apps.animals.models import Animal, Species
from apps.business.models import Location
from apps.people.models import Person
from dragonroost.mixins import PageTitleViewMixin


# Create your views here.
class HomeListView(LoginRequiredMixin, PageTitleViewMixin, ListView):
    """
    This custom ListView gathers context from many models to display on the index page.
    """

    context_object_name = "animals"
    template_name = "index.html"
    title = "Dashboard"
    queryset = Animal.objects.all()

    def get_context_data(self, **kwargs):
        context = super(HomeListView, self).get_context_data(**kwargs)
        context["species"] = Species.objects.all()
        context["people"] = Person.objects.all()
        context["locations"] = Location.objects.all()
        context["animal_count"] = Animal.objects.filter(~Q(status="ADOPTED")).count()
        context["adopted_past_30_days"] = (
            Animal.objects.filter(status="ADOPTED")
            .filter(
                outcome_date__gte=(
                    datetime.datetime.now() - datetime.timedelta(days=(30))
                )
            )
            .count()
        )
        context["donation_total_365_days"] = Animal.objects.filter(
            outcome_date__gte=(datetime.datetime.now() - datetime.timedelta(days=(365)))
        ).aggregate(Sum("donation_fee"))["donation_fee__sum"]

        return context
