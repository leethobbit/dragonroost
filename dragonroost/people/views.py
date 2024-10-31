# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.views.generic.edit import DeleteView
from django.views.generic.edit import UpdateView
from django_filters.views import FilterView
from django_tables2 import SingleTableMixin

from dragonroost.mixins import PageTitleViewMixin

from .filters import PersonFilter
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
    template_name = "people/person_form.html"
    title = "Add Person"
    fields = (
        "first_name",
        "last_name",
        "email",
        "phone_number",
        "roles",
        "address",
        "zip_code",
        "notes",
    )

    def get_success_url(self):
        return reverse_lazy("people:person-detail", kwargs={"pk": self.object.id})


class PersonUpdateView(LoginRequiredMixin, PageTitleViewMixin, UpdateView):
    model = Person
    template_name = "people/person_form.html"
    title = "Edit Person"
    fields = (
        "first_name",
        "last_name",
        "email",
        "phone_number",
        "roles",
        "address",
        "zip_code",
        "notes",
    )

    def get_success_url(self):
        return reverse_lazy("people:person-detail", kwargs={"pk": self.object.id})


class PersonDeleteView(LoginRequiredMixin, PageTitleViewMixin, DeleteView):
    model = Person
    template_name = "people/person_confirm_delete.html"
    title = "Delete Person"
    success_url = reverse_lazy("people:person-list")


class PersonHTMxView(SingleTableMixin, PageTitleViewMixin, FilterView):
    table_class = PersonHTMxTable
    queryset = Person.objects.all()
    filterset_class = PersonFilter
    paginate_by = 15
    title = "People Search"

    def get_template_names(self) -> list[str]:
        if self.request.htmx:
            template_name = "people/person_table_htmx.html"
        else:
            template_name = "people/person_table_htmx_reload.html"

        return template_name
