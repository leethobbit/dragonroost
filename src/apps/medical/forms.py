from django import forms

from apps.animals.models import MedicalRecord


class MedicalRecordForm(forms.ModelForm):
    class Meta:
        model = MedicalRecord
        fields = ["notes", "initials", "is_vet_cleared"]
