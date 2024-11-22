import logging
from datetime import datetime

from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import DetailView
from django.views.generic import UpdateView
from django_filters.views import FilterView
from django_tables2 import SingleTableMixin

from dragonroost.mixins import PageTitleViewMixin

from .filters import AnimalFilter
from .filters import SpeciesFilter
from .forms import AnimalCreateForm
from .forms import AnimalUpdateForm
from .forms import MedicalRecordForm
from .forms import SpeciesForm
from .models import Animal
from .models import MedicalRecord
from .models import Species
from .tables import AnimalTable
from .tables import SpeciesTable

logger = logging.getLogger(__name__)


class AnimalTableView(
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


class AnimalTableSearchView(LoginRequiredMixin, SingleTableMixin, FilterView):
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
    title = "Animal Details"
    context_object_name = "animal"

    def get_template_names(self):
        if self.request.htmx:
            template_name = "animals/partials/animal_detail.html"
        else:
            template_name = "animals/animal_detail_full.html"

        return template_name

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
    form_class = AnimalCreateForm
    template_name = "animals/animal_form.html"
    title = "Create Animal"

    def post(self, request, *args, **kwargs):
        form = AnimalCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse(
                status=204,
                headers={"HX-Trigger": "animal_table_update"},
            )
        return render(request, "animals/animal_form.html", {"form": form})


class AnimalUpdateView(LoginRequiredMixin, PageTitleViewMixin, UpdateView):
    model = Animal
    form_class = AnimalUpdateForm
    template_name = "animals/animal_form.html"
    title = "Edit Animal"

    def post(self, request, *args, **kwargs):
        animal = get_object_or_404(Animal, pk=self.kwargs["pk"])
        form = AnimalUpdateForm(request.POST, request.FILES, instance=animal)
        if form.is_valid():
            form.save()
            return HttpResponse(
                status=204,
                headers={"HX-Trigger": "animal_detail_update"},
            )
        return render(
            request,
            "animals/animal_form.html",
            {
                "form": form,
                "animal": animal,
            },
        )


class AnimalOutcomeForm(forms.ModelForm):
    """
    TODO: Reimplement or create new method for adoptions
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

    def post(self, request, *args, **kwargs):
        animal = get_object_or_404(Animal, pk=self.kwargs["pk"])
        animal.delete()

        return HttpResponse(
            status=204,
            headers={"HX-Trigger": "animal_table_update"},
        )


class SpeciesListView(
    SingleTableMixin,
    LoginRequiredMixin,
    PageTitleViewMixin,
    FilterView,
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


class SpeciesTableView(LoginRequiredMixin, SingleTableMixin, FilterView):
    """
    This view handles only the small partial for reloading table data
    """

    table_class = SpeciesTable
    queryset = Species.objects.all().order_by("name")
    filterset_class = SpeciesFilter
    paginate_by = 15
    template_name = "animals/partials/animal_table.html"


class SpeciesDetailView(LoginRequiredMixin, PageTitleViewMixin, DetailView):
    model = Species
    title = "Species Detail"
    template_name = "animals/species_detail.html"
    context_object_name = "species"


class SpeciesCreateView(LoginRequiredMixin, PageTitleViewMixin, CreateView):
    model = Species
    form_class = SpeciesForm
    title = "Create Species"
    template_name = "animals/species_form.html"

    def post(self, request, *args, **kwargs):
        form = SpeciesForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse(
                status=204,
                headers={"HX-Trigger": "species_table_update"},
            )
        return render(request, "animals/species_form.html", {"form": form})


class SpeciesUpdateView(LoginRequiredMixin, PageTitleViewMixin, UpdateView):
    model = Species
    form_class = SpeciesForm
    title = "Edit Species"
    template_name = "animals/species_form.html"

    def post(self, request, *args, **kwargs):
        species = get_object_or_404(Species, pk=self.kwargs["pk"])
        form = SpeciesForm(request.POST, instance=species)
        if form.is_valid():
            form.save()
            return HttpResponse(
                status=204,
                headers={"HX-Trigger": "species_table_update"},
            )
        return render(
            request,
            "animals/species_form.html",
            {
                "form": form,
                "species": species,
            },
        )


class SpeciesDeleteView(LoginRequiredMixin, PageTitleViewMixin, DeleteView):
    model = Species
    template_name = "animals/species_confirm_delete.html"

    def post(self, request, *args, **kwargs):
        species = get_object_or_404(Species, pk=self.kwargs["pk"])
        species.delete()

        return HttpResponse(
            status=204,
            headers={"HX-Trigger": "species_table_update"},
        )


class MedicalRecordCreateView(LoginRequiredMixin, PageTitleViewMixin, CreateView):
    model = MedicalRecord
    form_class = MedicalRecordForm
    template_name = "animals/base_form.html"
    title = "Add Medical Record"

    def post(self, request, *args, **kwargs):
        form = MedicalRecordForm(request.POST)
        form.instance.animal = get_object_or_404(Animal, pk=self.kwargs["pk"])
        if form.is_valid():
            logger.debug("Form is valid so far")
            form.save()
            return HttpResponse(
                status=204,
                headers={"HX-Trigger": "animal_detail_update"},
            )
        return render(request, "animals/base_form.html", {"form": form})


class MedicalRecordUpdateView(LoginRequiredMixin, PageTitleViewMixin, UpdateView):
    model = MedicalRecord
    form_class = MedicalRecordForm
    title = "Edit Record"
    template_name = "animals/base_form.html"

    def post(self, request, *args, **kwargs):
        medical_record = get_object_or_404(MedicalRecord, pk=self.kwargs["pk"])
        form = MedicalRecordForm(request.POST, instance=medical_record)
        if form.is_valid():
            form.save()
            return HttpResponse(
                status=204,
                headers={"HX-Trigger": "animal_detail_update"},
            )
        return render(
            request,
            "animals/base_form.html",
            {
                "form": form,
                "medical_record": medical_record,
            },
        )


class MedicalRecordDeleteView(LoginRequiredMixin, DeleteView):
    model = MedicalRecord
    template_name = "animals/medical_record_confirm_delete.html"

    def post(self, request, *args, **kwargs):
        medical_record = get_object_or_404(MedicalRecord, pk=self.kwargs["pk"])
        medical_record.delete()

        return HttpResponse(
            status=204,
            headers={"HX-Trigger": "animal_detail_update"},
        )
