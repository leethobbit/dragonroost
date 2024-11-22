from crispy_forms.helper import FormHelper
from django import forms

from .models import MedicalUpdate


class MedicalUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.label_class = "text-dark"
        self.helper.form_tag = False

    class Meta:
        model = MedicalUpdate
        fields = ["title", "notes", "q_staff"]
