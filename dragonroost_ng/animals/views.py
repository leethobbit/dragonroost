from datetime import datetime

from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic import UpdateView
from django_filters.views import FilterView
from django_tables2 import SingleTableMixin

from dragonroost_ng.animals.filters import AnimalFilter
from dragonroost_ng.animals.filters import SpeciesFilter
from dragonroost_ng.animals.forms import MedicalRecordForm
from dragonroost_ng.animals.models import Animal
from dragonroost_ng.animals.models import MedicalRecord
from dragonroost_ng.animals.models import Species
from dragonroost_ng.animals.tables import AnimalTable
from dragonroost_ng.animals.tables import SpeciesTable
from dragonroost_ng.mixins import PageTitleViewMixin


class HTMxAnimalTableDisplayView(
    LoginRequiredMixin,
    SingleTableMixin,
    PageTitleViewMixin,
    FilterView,
):
    """
    This view handles loading the overall Animal Table page - either via the sidebar,
    or via reload.
    """

    table_class = AnimalTable
    queryset = Animal.objects.all().order_by("name")
    filterset_class = AnimalFilter
    paginate_by = 15
    title = "Manage Animals"

    def get_template_names(self):
        if self.request.htmx:
            template_name = "animals/animal_table_htmx.html"
        else:
            template_name = "animals/animal_table_htmx_reload.html"

        return template_name


class HTMxAnimalTableSearchView(LoginRequiredMixin, SingleTableMixin, FilterView):
    """
    This view only handles the small partial for reloading the table data specifically.
    """

    table_class = AnimalTable
    queryset = Animal.objects.all().order_by("name")
    filterset_class = AnimalFilter
    paginate_by = 15
    template_name = "animals/partials/animal_table.html"


# Old views to update / remove / etc
class AnimalDetailView(LoginRequiredMixin, PageTitleViewMixin, DetailView):
    model = Animal
    template_name = "animals/animal_detail.html"
    title = "Animal Details"
    context_object_name = "animal"

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        medical_records = MedicalRecord.objects.filter(
            animal=self.get_object(),
        ).order_by("-created")
        data["medical_records"] = medical_records
        data["medical_record_form"] = MedicalRecordForm(instance=self.get_object())
        return data


class AnimalCreateView(LoginRequiredMixin, PageTitleViewMixin, CreateView):
    model = Animal
    template_name = "animals/animal_form.html"
    title = "Create Animal"
    fields = (
        "name",
        "animal_photo",
        "description",
        "intake_type",
        "intake_condition",
        "donation_fee",
        "color",
        "sex",
        "age",
        "species",
        "location",
        "status",
    )

    def get_success_url(self):
        return reverse_lazy("animals:animal-detail", kwargs={"pk": self.object.id})


class AnimalUpdateView(LoginRequiredMixin, PageTitleViewMixin, UpdateView):
    model = Animal
    template_name = "animals/animal_form.html"
    title = "Edit Animal"
    fields = (
        "name",
        "animal_photo",
        "description",
        "current_condition",
        "donation_fee",
        "color",
        "sex",
        "age",
        "species",
        "location",
        "status",
    )

    def get_success_url(self):
        return reverse_lazy("animals:animal-detail", kwargs={"pk": self.object.id})


class AnimalOutcomeForm(forms.ModelForm):
    """
    Custom form for animal outcomes - sets the status to "Adopted" and
    outcome_date to today.
    """

    def __init__(self, *args, **kwargs):
        kwargs["initial"]["status"] = "ADOPTED"
        kwargs["initial"]["outcome_date"] = datetime.now().strftime("%Y-%m-%d")  # noqa: DTZ005
        super().__init__(*args, **kwargs)

    class Meta:
        model = Animal
        fields = [
            "name",
            "outcome_type",
            "outcome_date",
            "donation_fee",
            "status",
        ]
        widgets = {
            "outcome_date": forms.widgets.DateInput(attrs={"type": "date"}),
        }


class AnimalOutcomeView(LoginRequiredMixin, PageTitleViewMixin, UpdateView):
    form_class = AnimalOutcomeForm
    model = Animal
    template_name = "animals/animal_form.html"
    title = "Animal Outcome"

    def get_success_url(self):
        return reverse_lazy("animals:animal-detail", kwargs={"pk": self.object.id})


class AnimalDeleteView(LoginRequiredMixin, PageTitleViewMixin, DeleteView):
    model = Animal
    template_name = "animals/animal_confirm_delete.html"
    title = "Animal Delete Confirmation"
    success_url = reverse_lazy("animals:animal-list")


class SpeciesListView(
    SingleTableMixin,
    LoginRequiredMixin,
    PageTitleViewMixin,
    ListView,
):
    model = Species
    table_class = SpeciesTable
    queryset = Species.objects.all().order_by("name")
    filterset_class = SpeciesFilter
    title = "Species List"
    context_object_name = "species"

    def get_template_names(self):
        if self.request.htmx:
            template_name = "animals/species_table_htmx.html"
        else:
            template_name = "animals/species_table_htmx_reload.html"

        return template_name


class SpeciesDetailView(LoginRequiredMixin, PageTitleViewMixin, DetailView):
    model = Species
    title = "Species Detail"
    template_name = "animals/species_detail.html"
    context_object_name = "species"


class SpeciesCreateView(LoginRequiredMixin, PageTitleViewMixin, CreateView):
    model = Species
    title = "Create Species"
    template_name = "animals/base_form.html"
    fields = ("name", "diet", "class_name", "description")

    def get_success_url(self):
        return reverse_lazy("animals:species-detail", kwargs={"pk": self.object.id})


class SpeciesUpdateView(LoginRequiredMixin, PageTitleViewMixin, UpdateView):
    model = Species
    title = "Edit Species"
    template_name = "animals/base_form.html"
    fields = ("name", "diet", "class_name", "description")

    def get_success_url(self):
        return reverse_lazy("animals:species-detail", kwargs={"pk": self.object.id})


class SpeciesDeleteView(LoginRequiredMixin, PageTitleViewMixin, DeleteView):
    model = Species
    template_name = "animals/species_confirm_delete.html"
    success_url = reverse_lazy("home_list")


class MedicalRecordCreateView(LoginRequiredMixin, PageTitleViewMixin, CreateView):
    model = MedicalRecord
    form_class = MedicalRecordForm
    template_name = "animals/base_form.html"

    def get_success_url(self):
        return reverse_lazy(
            "animals:animal-detail",
            kwargs={"pk": self.object.animal.id},
        )

    def post(self, request, *args, **kwargs):
        pk = self.kwargs["pk"]
        new_medical_record = MedicalRecord(
            animal_id=self.kwargs["pk"],
            notes=request.POST.get("notes"),
            created=request.POST.get("created"),
            q_volunteer_id=request.POST.get("q_volunteer"),
            bowel_movement=request.POST.get("bowel_movement") == "on",
            current_weight=request.POST.get("current_weight"),
            treatments=request.POST.get("treatments"),
        )
        new_medical_record.save()
        return redirect("animals:animal-detail", pk=pk)


class MedicalRecordDeleteView(LoginRequiredMixin, DeleteView):
    model = MedicalRecord
    template_name = "animals/medical_record_confirm_delete.html"

    def get_success_url(self):
        return reverse_lazy(
            "animals:animal-detail",
            kwargs={"pk": self.object.animal.id},
        )
