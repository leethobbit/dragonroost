from datetime import datetime

from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django_filters.views import FilterView
from django_tables2 import SingleTableMixin, SingleTableView

from apps.animals.filters import AnimalFilter, SpeciesFilter
from apps.animals.tables import AnimalHTMxTable, SpeciesListTable
from apps.medical.forms import MedicalRecordForm
from dragonroost.mixins import PageTitleViewMixin

from .models import Animal, MedicalRecord, Species


# Create your views here.
class AnimalListView(LoginRequiredMixin, PageTitleViewMixin, ListView):
    model = Animal
    template_name = "animals/animal-list.html"
    title = "Recent Intakes"
    context_object_name = "animals"


class AnimalDetailView(LoginRequiredMixin, PageTitleViewMixin, DetailView):
    model = Animal
    template_name = "animals/animal-detail.html"
    title = "Animal Details"
    context_object_name = "animal"

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        medical_records = MedicalRecord.objects.filter(
            animal=self.get_object()
        ).order_by("-created")
        data["medical_records"] = medical_records
        data["medical_record_form"] = MedicalRecordForm(instance=self.get_object())
        return data


class AnimalCreateView(LoginRequiredMixin, PageTitleViewMixin, CreateView):
    model = Animal
    template_name = "animals/animal-form.html"
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
    template_name = "animals/animal-form.html"
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
    Custom form for animal outcomes - sets the status to "Adopted" and outcome_date to today.
    """

    def __init__(self, *args, **kwargs):
        kwargs["initial"]["status"] = "ADOPTED"
        kwargs["initial"]["outcome_date"] = datetime.now().strftime("%Y-%m-%d")
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
    template_name = "animals/animal-form.html"
    title = "Animal Outcome"

    def get_success_url(self):
        return reverse_lazy("animals:animal-detail", kwargs={"pk": self.object.id})


class AnimalDeleteView(LoginRequiredMixin, PageTitleViewMixin, DeleteView):
    model = Animal
    template_name = "animals/animal-confirm-delete.html"
    title = "Animal Delete Confirmation"
    success_url = reverse_lazy("animals:animal-list")


class SpeciesListView(
    SingleTableMixin, LoginRequiredMixin, PageTitleViewMixin, ListView
):
    model = Species
    table_class = SpeciesListTable
    queryset = Species.objects.all().order_by("name")
    filterset_class = SpeciesFilter
    template_name = "animals/species-list.html"
    title = "Species List"
    context_object_name = "species"


class SpeciesDetailView(LoginRequiredMixin, PageTitleViewMixin, DetailView):
    model = Species
    title = "Species Detail"
    template_name = "animals/species-detail.html"
    context_object_name = "species"


class SpeciesCreateView(LoginRequiredMixin, PageTitleViewMixin, CreateView):
    model = Species
    title = "Create Species"
    template_name = "animals/base-form.html"
    fields = ("name", "diet", "class_name", "description")

    def get_success_url(self):
        return reverse_lazy("animals:species-detail", kwargs={"pk": self.object.id})


class SpeciesUpdateView(LoginRequiredMixin, PageTitleViewMixin, UpdateView):
    model = Species
    title = "Edit Species"
    template_name = "animals/base-form.html"
    fields = ("name", "diet", "class_name", "description")

    def get_success_url(self):
        return reverse_lazy("animals:species-detail", kwargs={"pk": self.object.id})


class SpeciesDeleteView(LoginRequiredMixin, PageTitleViewMixin, DeleteView):
    model = Species
    template_name = "animals/species-confirm-delete.html"
    success_url = reverse_lazy("home_list")


class AnimalHTMxTableView(SingleTableMixin, PageTitleViewMixin, FilterView):
    table_class = AnimalHTMxTable
    queryset = Animal.objects.all()
    filterset_class = AnimalFilter
    paginate_by = 15
    title = "Animal Search"

    def get_template_names(self):
        if self.request.htmx:
            template_name = "animals/animal-table-partial.html"
        else:
            template_name = "animals/animal-table-htmx.html"

        return template_name


class MedicalRecordCreateView(LoginRequiredMixin, PageTitleViewMixin, CreateView):
    model = MedicalRecord
    form_class = MedicalRecordForm
    template_name = "animals/base-form.html"

    def get_success_url(self):
        print("Reached success redirect url function, yay!")
        print(self.object.animal.id)
        return reverse_lazy(
            "animals:animal-detail", kwargs={"pk": self.object.animal.id}
        )

    # def get_context_data(self, **kwargs):
    #     context = super(MedicalRecordCreateView, self).get_context_data(**kwargs)
    #     context["animal_id"] = self.kwargs["pk"]
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

    # def __init__(self, *args, **kwargs):
    #     animal_id = kwargs.pop("animal.id")


class MedicalRecordDeleteView(LoginRequiredMixin, DeleteView):
    model = MedicalRecord
    template_name = "animals/record-confirm-delete.html"

    def get_success_url(self):
        return reverse_lazy(
            "animals:animal-detail", kwargs={"pk": self.object.animal.id}
        )
