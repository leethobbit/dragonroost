from crispy_forms.helper import FormHelper
from django import forms

from .models import Person


class PersonForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.label_class = "text-dark"
        self.helper.form_tag = False

    class Meta:
        model = Person
        fields = [
            "first_name",
            "last_name",
            "email",
            "phone_number",
            "roles",
            "address",
            "zip_code",
            "notes",
        ]
