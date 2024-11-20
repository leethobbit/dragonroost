from decimal import Decimal

import django_filters
from crispy_forms.helper import FormHelper
from django import forms
from django.db.models import Q
from django.forms import TextInput

from dragonroost.animals.models import Animal
from dragonroost.animals.models import Species
from dragonroost.business.models import Location

# These choices are duplicated in the Animal model definition for the time being.
STATUS_CHOICES = [
    ("ADOPTED", "Adopted"),
    ("AMBASSADOR", "Ambassador"),
    ("AVAILABLE", "Available"),
    ("DECEASED", "Deceased"),
    ("FOSTERED", "Fostered"),
    ("MEDICAL_HOLD", "Medical Hold"),
    ("ON_HOLD", "On Hold"),
    ("QUARANTINE", "Quarantine"),
]


class AnimalSearchInput(TextInput):
    input_type = "search"


class AnimalFilter(django_filters.FilterSet):
    query = django_filters.CharFilter(
        method="universal_search",
        label="",
        widget=AnimalSearchInput(attrs={"placeholder": "Search..."}),
    )

    start_intake_date = django_filters.DateFilter(
        field_name="intake_date",
        lookup_expr="gte",
        label="Date From",
        widget=forms.DateInput(attrs={"type": "date"}),
    )

    end_intake_date = django_filters.DateFilter(
        field_name="intake_date",
        lookup_expr="lte",
        label="Date To",
        widget=forms.DateInput(attrs={"type": "date"}),
    )

    status = django_filters.MultipleChoiceFilter(
        choices=STATUS_CHOICES,
        widget=forms.CheckboxSelectMultiple(),
    )

    location = django_filters.ModelMultipleChoiceFilter(
        queryset=Location.objects.all(),
        label="Locations",
        widget=forms.CheckboxSelectMultiple(),
    )

    class Meta:
        model = Animal
        fields = [
            "query",
            "start_intake_date",
            "end_intake_date",
            "status",
            "location",
        ]

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
