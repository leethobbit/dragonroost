from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from dragonroost.mixins import PageTitleViewMixin

from .models import Person


# Create your views here.
class PersonListView(LoginRequiredMixin, PageTitleViewMixin, ListView):
    model = Person
    template_name = "people/person-list.html"
    title = "People List"
    context_object_name = "people"


class PersonDetailView(LoginRequiredMixin, DetailView):
    model = Person
    template_name = "people/person-detail.html"
    context_object_name = "person"


class PersonCreateView(LoginRequiredMixin, PageTitleViewMixin, CreateView):
    model = Person
    template_name = "people/person-form.html"
    title = "Add Person"
    fields = (
        "first_name",
        "last_name",
        "email",
        "phone_number",
        "type",
        "address",
        "zip_code",
        "notes",
    )

    def get_success_url(self):
        return reverse_lazy("people:person-detail", kwargs={"pk": self.object.id})


class PersonUpdateView(LoginRequiredMixin, PageTitleViewMixin, UpdateView):
    model = Person
    template_name = "people/person-form.html"
    title = "Edit Person"
    fields = (
        "first_name",
        "last_name",
        "email",
        "phone_number",
        "type",
        "address",
        "zip_code",
        "notes",
    )

    def get_success_url(self):
        return reverse_lazy("people:person-detail", kwargs={"pk": self.object.id})


class PersonDeleteView(LoginRequiredMixin, PageTitleViewMixin, DeleteView):
    model = Person
    template_name = "people/person-confirm-delete.html"
    title = "Delete Person"
    success_url = reverse_lazy("people:person-list")
