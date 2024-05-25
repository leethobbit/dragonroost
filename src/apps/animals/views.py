from datetime import datetime
from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django_tables2 import SingleTableMixin, SingleTableView
from django_filters.views import FilterView

from dragonroost.mixins import PageTitleViewMixin

from .models import Animal, Species, MedicalRecord
from apps.medical.forms import MedicalRecordForm
from apps.animals.tables import AnimalHTMxTable
from apps.animals.filters import AnimalFilter


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
            animal=self.get_object()).order_by("-created")
        data["medical_records"] = medical_records
        data["medical_record_form"] = MedicalRecordForm(instance=self.get_object())
        return data
    
    def post(self, request, *args, **kwargs):
        new_medical_record = MedicalRecord(
            animal=self.get_object(),
            notes=request.POST.get("notes"),
            created=request.POST.get("created"),
            initials=request.POST.get("initials"),
            is_vet_cleared = request.POST.get("is_vet_cleared") == "on"
        )
        new_medical_record.save()
        return self.get(self, request, *args, **kwargs)


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

class MedicalRecordDeleteView(LoginRequiredMixin, DeleteView):
    model = MedicalRecord
    template_name = "animals/record-confirm-delete.html"
    
    def get_success_url(self):
        return reverse_lazy("animals:animal-detail", kwargs={"pk": self.object.animal.id})


class SpeciesListView(LoginRequiredMixin, PageTitleViewMixin, ListView):
    model = Species
    template_name = "animals/species-list.html"
    title = "Species List"
    context_object_name = "species"


class SpeciesDetailView(LoginRequiredMixin, PageTitleViewMixin, DetailView):
    model = Species
    template_name = "animals/species-detail.html"
    context_object_name = "species"


class SpeciesCreateView(LoginRequiredMixin, PageTitleViewMixin, CreateView):
    model = Species
    template_name = "animals/species-form.html"
    fields = ("name", "diet", "class_name", "description")

    def get_success_url(self):
        return reverse_lazy("animals:species-detail", kwargs={"pk": self.object.id})


class SpeciesUpdateView(LoginRequiredMixin, PageTitleViewMixin, UpdateView):
    model = Species
    template_name = "animals/species-form.html"
    fields = ("name", "diet", "class_name", "description")

    def get_success_url(self):
        return reverse_lazy("animals:species-detail", kwargs={"pk": self.object.id})


class SpeciesDeleteView(LoginRequiredMixin, PageTitleViewMixin, DeleteView):
    model = Species
    template_name = "animals/species-confirm-delete.html"
    success_url = reverse_lazy("home-list")


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