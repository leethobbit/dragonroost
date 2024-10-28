from django import forms

from dragonroost_ng.animals.models import MedicalRecord


class MedicalRecordForm(forms.ModelForm):
    class Meta:
        model = MedicalRecord
        fields = [
            "bowel_movement",
            "treatments",
            "current_weight",
            "notes",
            "q_volunteer",
        ]
