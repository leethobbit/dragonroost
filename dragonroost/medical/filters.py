import django_filters
from crispy_forms.helper import FormHelper

from .models import MedicalUpdate


class MedicalUpdateFilter(django_filters.FilterSet):
    query = django_filters.CharFilter(method="universal_search", label="")

    class Meta:
        model = MedicalUpdate
        fields = ["query"]

    def universal_search(self, queryset, name, value):
        return MedicalUpdate.objects.filter(name__icontains=value)

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
