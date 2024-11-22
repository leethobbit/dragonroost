import django_filters
from crispy_forms.helper import FormHelper
from django.db.models import Q
from django.forms import TextInput

from .models import MedicalUpdate


class MedicalUpdateSearchInput(TextInput):
    input_type = "search"


class MedicalUpdateFilter(django_filters.FilterSet):
    query = django_filters.CharFilter(
        method="universal_search",
        label="",
        widget=MedicalUpdateSearchInput(attrs={"placeholder": "Search..."}),
    )

    class Meta:
        model = MedicalUpdate
        fields = ["query"]

    def universal_search(self, queryset, name, value):
        return MedicalUpdate.objects.filter(Q(q_staff__username__icontains=value))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.form.helper = MedicalUpdateFormHelper()
        self.form.helper.form_tag = False


class MedicalUpdateFormHelper(FormHelper):
    """
    Subclassing the FormHelper simply to force GET method
    and enable usage of form_tag = False in the AnimalFilter class.
    """

    form_method = "GET"
