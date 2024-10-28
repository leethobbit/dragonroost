from decimal import Decimal

import django_filters
from crispy_forms.helper import FormHelper
from django.db.models import Q
from django.forms import TextInput

from dragonroost_ng.animals.models import Animal
from dragonroost_ng.animals.models import Species


class AnimalSearchInput(TextInput):
    input_type = "search"


class AnimalFilter(django_filters.FilterSet):
    query = django_filters.CharFilter(
        method="universal_search",
        label="",
        widget=AnimalSearchInput(attrs={"placeholder": "Search..."}),
    )

    class Meta:
        model = Animal
        fields = ["query"]

    def universal_search(self, queryset, name, value):
        if value.replace(".", "", 1).isdigit():
            value = Decimal(value)
            return Animal.objects.filter(
                Q(donation_fee=value) | Q(age=value) | Q(name=value),
            )

        return Animal.objects.filter(
            Q(name__icontains=value)
            | Q(description__icontains=value)
            | Q(species__name__icontains=value)
            | Q(location__name__icontains=value)
            | Q(status__icontains=value),
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.form.helper = AnimalFilterFormHelper()
        self.form.helper.form_tag = False


class AnimalFilterFormHelper(FormHelper):
    """
    Subclassing the FormHelper simply to force GET method
    and enable usage of form_tag = False in the AnimalFilter class.
    """

    form_method = "GET"


class SpeciesFilter(django_filters.FilterSet):
    query = django_filters.CharFilter(method="universal_search", label="")

    class Meta:
        model = Species
        fields = ["query"]

    def universal_search(self, queryset, name, value):
        return Species.objects.filter(name__icontains=value)
