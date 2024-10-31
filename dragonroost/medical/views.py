# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import DeleteView
from django.views.generic.edit import UpdateView
from django_filters.views import FilterView
from django_tables2 import SingleTableMixin

from dragonroost.mixins import PageTitleViewMixin

from .filters import MedicalUpdateFilter
from .models import MedicalUpdate
from .tables import MedicalUpdateTable


class MedicalUpdateTableView(
    SingleTableMixin,
    LoginRequiredMixin,
    PageTitleViewMixin,
    FilterView,
):
    table_class = MedicalUpdateTable
    queryset = MedicalUpdate.objects.all()
    filterset_class = MedicalUpdateFilter
    paginate_by = 15
    title = "Medical Updates List"


class MedicalUpdateDetailView(LoginRequiredMixin, PageTitleViewMixin, DetailView):
    model = MedicalUpdate
    template_name = "medical/medical_update_detail.html"
    title = "Medical Update Details"
    context_object_name = "medical_update"


class MedicalUpdateCreateView(LoginRequiredMixin, PageTitleViewMixin, CreateView):
    model = MedicalUpdate
    template_name = "medical/medical_update_form.html"
    title = "Add Medical Update"
    fields = ("title", "notes", "q_staff")

    def get_success_url(self):
        return reverse_lazy(
            "medical:medical-update-detail",
            kwargs={"pk": self.object.id},
        )


class MedicalUpdateUpdateView(LoginRequiredMixin, PageTitleViewMixin, UpdateView):
    model = MedicalUpdate
    template_name = "medical/medical_update_form.html"
    title = "Edit Medical Update"
    fields = ("title", "notes", "q_staff")

    def get_success_url(self):
        return reverse_lazy(
            "medical:medical-update-detail",
            kwargs={"pk": self.object.id},
        )


class MedicalUpdateDeleteView(LoginRequiredMixin, PageTitleViewMixin, DeleteView):
    model = MedicalUpdate
    template_name = "medical/medical_update_confirm_delete.html"
    title = "Delete Medical Update"
    success_url = reverse_lazy("medical:medical-update-list")
