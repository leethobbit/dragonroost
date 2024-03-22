from django import forms
from .models import MedicalRecord

class MedicalRecordForm(forms.ModelForm):
    class Meta:
        model = MedicalRecord
        fields = ["name", "health_report", "treatment_history", "notes", "is_vet_cleared"]