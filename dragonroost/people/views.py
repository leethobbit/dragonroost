# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.views.generic.edit import DeleteView
from django.views.generic.edit import UpdateView
from django_filters.views import FilterView
from django_tables2 import SingleTableMixin

from dragonroost.mixins import PageTitleViewMixin

from .filters import PersonFilter
from .forms import PersonForm
from .models import Person
from .tables import PersonHTMxTable


# Create your views here.
class PersonListView(
    SingleTableMixin,
    LoginRequiredMixin,
    PageTitleViewMixin,
    ListView,
):
    model = Person
    table_class = PersonHTMxTable
    queryset = Person.objects.all().order_by("first_name")
    template_name = "people/person-list.html"
    title = "People List"
    context_object_name = "people"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["volunteers"] = Person.objects.filter(roles__name="VOLUNTEER").order_by(
            "first_name",
        )
        context["adopters"] = Person.objects.filter(roles__name="ADOPTER").order_by(
            "first_name",
        )
        context["donors"] = Person.objects.filter(roles__name="DONOR").order_by(
            "first_name",
        )
        context["fosters"] = Person.objects.filter(roles__name="FOSTER").order_by(
            "first_name",
        )

        return context


class PersonDetailView(LoginRequiredMixin, PageTitleViewMixin, DetailView):
    model = Person
    template_name = "people/person_detail.html"
    title = "Person Details"
    context_object_name = "person"


class PersonCreateView(LoginRequiredMixin, PageTitleViewMixin, CreateView):
    model = Person
    form_class = PersonForm
    template_name = "people/person_form.html"
    title = "Add Person"

    def post(self, request, *args, **kwargs):
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse(
                status=204,
                headers={"HX-Trigger": "person_table_update"},
            )
        return render(request, "people/person_form.html", {"form": form})


class PersonUpdateView(LoginRequiredMixin, PageTitleViewMixin, UpdateView):
    model = Person
    form_class = PersonForm
    template_name = "people/person_form.html"
    title = "Edit Person"

    def post(self, request, *args, **kwargs):
        person = get_object_or_404(Person, pk=self.kwargs["pk"])
        form = PersonForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
            return HttpResponse(
                status=204,
                headers={"HX-Trigger": "person_table_update"},
            )
        return render(
            request,
            "people/person_form.html",
            {
                "form": form,
                "person": person,
            },
        )


class PersonDeleteView(LoginRequiredMixin, PageTitleViewMixin, DeleteView):
    model = Person
    template_name = "people/person_confirm_delete.html"
    title = "Delete Person"

    def post(self, request, *args, **kwargs):
        person = get_object_or_404(Person, pk=self.kwargs["pk"])
        person.delete()

        return HttpResponse(
            status=204,
            headers={"HX-Trigger": "person_table_update"},
        )


class PersonHTMxView(SingleTableMixin, PageTitleViewMixin, FilterView):
    table_class = PersonHTMxTable
    queryset = Person.objects.all()
    filterset_class = PersonFilter
    paginate_by = 10
    title = "People Search"

    def get_template_names(self) -> list[str]:
        if self.request.htmx:
            template_name = "people/person_table_htmx.html"
        else:
            template_name = "people/person_table_htmx_reload.html"

        return template_name


class PersonTableSearchView(LoginRequiredMixin, SingleTableMixin, FilterView):
    table_class = PersonHTMxTable
    queryset = Person.objects.all()
    filterset_class = PersonFilter
    paginate_by = 10
    template_name = "people/partials/person_table.html"
