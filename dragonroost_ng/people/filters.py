import django_filters
from crispy_forms.helper import FormHelper
from django.db.models import Q
from django.forms import TextInput

from dragonroost_ng.people.models import Person


class PeopleSearchInput(TextInput):
    input_type = "search"


class PersonFilter(django_filters.FilterSet):
    query = django_filters.CharFilter(
        method="universal_search",
        label="",
        widget=PeopleSearchInput(attrs={"placeholder": "Search..."}),
    )

    class Meta:
        model = Person
        fields = ["query"]

    def universal_search(self, queryset, name, value):
        return Person.objects.filter(
            Q(first_name__icontains=value)
            | Q(last_name__icontains=value)
            # | Q(email__icontains=value)
            # | Q(phone_number__icontains=value)
            | Q(roles__name__icontains=value),
            # | Q(address__icontains=value)
            # | Q(zip_code__icontains=value)
            # | Q(notes__icontains=value)
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.form.helper = PersonFilterFormHelper()
        self.form.helper.form_tag = False


class PersonFilterFormHelper(FormHelper):
    """
    Subclassing the FormHelper simply to force GET method
    and enable usage of form_tag = False in the AnimalFilter class.
    """

    form_method = "GET"
