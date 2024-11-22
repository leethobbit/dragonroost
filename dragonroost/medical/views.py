# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.views.generic import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import DeleteView
from django.views.generic.edit import UpdateView
from django_filters.views import FilterView
from django_tables2 import SingleTableMixin

from dragonroost.mixins import PageTitleViewMixin

from .filters import MedicalUpdateFilter
from .forms import MedicalUpdateForm
from .models import MedicalUpdate
from .tables import MedicalUpdateTable


class MedicalUpdateTableView(
    SingleTableMixin,
    LoginRequiredMixin,
    PageTitleViewMixin,
    FilterView,
):
    table_class = MedicalUpdateTable
    queryset = MedicalUpdate.objects.all().order_by("-date")
    filterset_class = MedicalUpdateFilter
    paginate_by = 15
    title = "Medical Updates List"

    def get_template_names(self):
        if self.request.htmx:
            template_name = "medical/medical_update_table_htmx.html"
        else:
            template_name = "medical/medical_update_table_htmx_reload.html"

        return template_name


class MedicalUpdateTableSearchView(LoginRequiredMixin, SingleTableMixin, FilterView):
    table_class = MedicalUpdateTable
    queryset = MedicalUpdate.objects.all().order_by("-date")
    filterset_class = MedicalUpdateFilter
    paginate_by = 15
    template_name = "medical/partials/medical_update_table.html"


class MedicalUpdateDetailView(LoginRequiredMixin, PageTitleViewMixin, DetailView):
    model = MedicalUpdate
    template_name = "medical/medical_update_detail.html"
    title = "Medical Update Details"
    context_object_name = "medical_update"


class MedicalUpdateCreateView(LoginRequiredMixin, PageTitleViewMixin, CreateView):
    model = MedicalUpdate
    form_class = MedicalUpdateForm
    title = "Add Medical Update"
    template_name = "medical/medical_update_form.html"

    def post(self, request, *args, **kwargs):
        form = MedicalUpdateForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse(
                status=204,
                headers={"HX-Trigger": "medical_update_table_update"},
            )
        return render(request, "medical/medical_update_form.html", {"form": form})


class MedicalUpdateUpdateView(LoginRequiredMixin, PageTitleViewMixin, UpdateView):
    model = MedicalUpdate
    form_class = MedicalUpdateForm
    template_name = "medical/medical_update_form.html"
    title = "Edit Medical Update"

    def post(self, request, *args, **kwargs):
        medical_update = get_object_or_404(MedicalUpdate, pk=self.kwargs["pk"])
        form = MedicalUpdateForm(request.POST, instance=medical_update)
        if form.is_valid():
            form.save()
            return HttpResponse(
                status=204,
                headers={"HX-Trigger": "medical_update_table_update"},
            )
        return render(
            request,
            "medical/medical_update_form.html",
            {
                "form": form,
                "medical_update": medical_update,
            },
        )


class MedicalUpdateDeleteView(LoginRequiredMixin, PageTitleViewMixin, DeleteView):
    model = MedicalUpdate
    template_name = "medical/medical_update_confirm_delete.html"
    title = "Delete Medical Update"

    def post(self, request, *args, **kwargs):
        medical_update = get_object_or_404(MedicalUpdate, pk=self.kwargs["pk"])
        medical_update.delete()

        return HttpResponse(
            status=204,
            headers={"HX-Trigger": "medical_update_table_update"},
        )
