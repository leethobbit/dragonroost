from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from dragonroost.mixins import PageTitleViewMixin
from .models import Animal, Species, Status

# Create your views here.
class AnimalListView(LoginRequiredMixin, ListView):
    model = Animal
    template_name = "animals/animal-list.html"
    context_object_name = "animals"

class AnimalDetailView(LoginRequiredMixin, DetailView):
    model = Animal
    template_name = "animals/animal-detail.html"
    context_object_name = "animal"

class AnimalCreateView(LoginRequiredMixin, PageTitleViewMixin, CreateView):
    model = Animal
    template_name = "animals/animal-form.html"
    title = "Create Animal"
    fields = ("name", "animal_photo", "description", "donation_fee", "color", "sex", "age", "species", "location", "status")
    def get_success_url(self):
        return reverse_lazy('animals:animal-detail', kwargs={"pk": self.object.id})
    
class AnimalUpdateView(LoginRequiredMixin, PageTitleViewMixin, UpdateView):
    model = Animal
    template_name = "animals/animal-form.html"
    title = "Edit Animal"
    fields = ("name", "animal_photo", "description", "donation_fee", "color", "sex", "age", "species", "location", "status")
    def get_success_url(self):
        return reverse_lazy('animals:animal-detail', kwargs={"pk": self.object.id})

class AnimalDeleteView(LoginRequiredMixin, DeleteView):
    model = Animal
    template_name = "animals/animal-confirm-delete.html"
    success_url = reverse_lazy("animals:animal-list")

class SpeciesListView(LoginRequiredMixin, ListView):
    model = Species
    template_name = "animals/species-list.html"
    context_object_name = "species"

class SpeciesDetailView(LoginRequiredMixin, DetailView):
    model = Species
    template_name = "animals/species-detail.html"
    context_object_name = "species"

class SpeciesCreateView(LoginRequiredMixin, CreateView):
    model = Species
    template_name = "animals/species-form.html"
    fields = ("name", "class_name", "description")
    def get_success_url(self):
        return reverse_lazy('animals:species-detail', kwargs={"pk": self.object.id})

class SpeciesUpdateView(LoginRequiredMixin, UpdateView):
    model = Species
    template_name = "animals/species-form.html"
    fields = ("name", "class_name", "description")
    def get_success_url(self):
        return reverse_lazy('animals:species-detail', kwargs={"pk": self.object.id})

class SpeciesDeleteView(LoginRequiredMixin, DeleteView):
    model = Species
    template_name = "animals/species-confirm-delete.html"
    success_url = reverse_lazy("home-list")

class StatusListView(LoginRequiredMixin, ListView):
    model = Status
    template_name = "animals/status-list.html"
    context_object_name = "statuses"

class StatusDetailView(LoginRequiredMixin, DetailView):
    model = Status
    template_name = "animals/status-detail.html"
    context_object_name = "status"

class StatusCreateView(LoginRequiredMixin, CreateView):
    model = Status
    template_name = "animals/status-form.html"
    fields = ("name", "description")
    def get_success_url(self):
        return reverse_lazy("animals:status-detail", kwargs={"pk": self.object.id})

class StatusUpdateView(LoginRequiredMixin, UpdateView):
    model = Status
    template_name = "animals/status-form.html"
    fields = ("name", "description")
    def get_success_url(self):
        return reverse_lazy("animals:status-detail", kwargs={"pk": self.object.id})

class StatusDeleteView(LoginRequiredMixin, DeleteView):
    model = Status
    template_name = "animals/status-confirm-delete.html"
    success_url = reverse_lazy("animals:status-list")