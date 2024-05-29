# Animals/filters.py
from decimal import Decimal

import django_filters
from django.db.models import Q

from apps.animals.models import Animal, Species


class AnimalFilter(django_filters.FilterSet):
    query = django_filters.CharFilter(method="universal_search", label="")

    class Meta:
        model = Animal
        fields = ["query"]

    def universal_search(self, queryset, name, value):
        if value.replace(".", "", 1).isdigit():
            value = Decimal(value)
            return Animal.objects.filter(
                Q(donation_fee=value) | Q(age=value) | Q(name=value)
            )

        return Animal.objects.filter(
            Q(name__icontains=value)
            | Q(description__icontains=value)
            | Q(species__name__icontains=value)
            | Q(location__name__icontains=value)
            | Q(status__icontains=value)
        )

class SpeciesFilter(django_filters.FilterSet):
    query = django_filters.CharFilter(method="universal_search", label="")

    class Meta:
        model = Species
        fields = ["query"]

    def universal_search(self, queryset, name, value):
        return Species.objects.filter(name__icontains=value)