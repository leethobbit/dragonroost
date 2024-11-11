from django import forms

from dragonroost.animals.models import Animal
from dragonroost.animals.models import MedicalRecord
from dragonroost.animals.models import Species


class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = [
            "name",
            "description",
        ]


class SpeciesForm(forms.ModelForm):
    class Meta:
        model = Species
        fields = [
            "name",
            "class_name",
            "diet",
            "description",
            "is_ohio_native",
        ]


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
