from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Location

# Create your views here.
class LocationListView(LoginRequiredMixin, ListView):
    model = Location
    template_name = "business/location-list.html"
    context_object_name = "locations"

class LocationDetailView(LoginRequiredMixin, DetailView):
    model = Location
    template_name = "business/location-detail.html"
    context_object_name = "location"

class LocationCreateView(LoginRequiredMixin, CreateView):
    model = Location
    template_name = "business/location-form.html"
    fields = ("name", "description")
    def get_success_url(self):
        return reverse_lazy("business:location-detail", kwargs={"pk": self.object.id})
    
class LocationUpdateView(LoginRequiredMixin, UpdateView):
    model = Location
    template_name = "business/location-form.html"
    fields = ("name", "description")
    def get_success_url(self):
        return reverse_lazy("business:location-detail", kwargs={"pk": self.object.id})

class LocationDeleteView(LoginRequiredMixin, DeleteView):
    model = Location
    template_name = "business/location-confirm-delete.html"
    success_url = reverse_lazy("business:location-list")