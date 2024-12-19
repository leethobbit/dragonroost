from crispy_bootstrap5.bootstrap5 import FloatingField
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Div
from crispy_forms.layout import Layout
from crispy_forms.layout import Row
from django import forms
from django_measurement.forms import MeasurementField
from measurement.measures import Weight

from dragonroost.animals.models import Animal
from dragonroost.animals.models import MedicalRecord
from dragonroost.animals.models import Species


class AnimalCreateForm(forms.ModelForm):
    starting_weight = MeasurementField(
        measurement=Weight,
        unit_choices=(("lb", "lb"), ("kg", "kg"), ("g", "g")),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.label_class = "text-dark"
        self.helper.form_tag = False

        # Layout
        self.helper.layout = Layout(
            Row(
                Div(
                    FloatingField("name"),
                    css_class="col-md-6",
                ),
                Div(
                    FloatingField("donation_fee"),
                    css_class="col-md-6",
                ),
            ),
            "animal_photo",
            FloatingField("description"),
            Row(
                Div(
                    FloatingField("intake_type"),
                    css_class="col-md-4",
                ),
                Div(
                    FloatingField("intake_condition"),
                    css_class="col-md-4",
                ),
                Div(
                    FloatingField("starting_weight"),
                    css_class="col-md-4",
                ),
            ),
            Row(
                Div(
                    FloatingField("sex"),
                    css_class="col-md-4",
                ),
                Div(
                    FloatingField("age"),
                    css_class="col-md-4",
                ),
                Div(
                    FloatingField("color"),
                    css_class="col-md-4",
                ),
            ),
            FloatingField("species"),
            FloatingField("location"),
            FloatingField("status"),
        )

    class Meta:
        model = Animal
        fields = [
            "name",
            "animal_photo",
            "description",
            "intake_type",
            "intake_condition",
            "starting_weight",
            "donation_fee",
            "color",
            "sex",
            "age",
            "species",
            "location",
            "status",
        ]


class AnimalUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.label_class = "text-dark"
        self.helper.form_tag = False

        # Layout
        self.helper.layout = Layout(
            Row(
                FloatingField("name", wrapper_class="form-group col-md-6 mb-0"),
                FloatingField("donation_fee", wrapper_class="form-group col-md-6 mb-0"),
            ),
            "animal_photo",
            FloatingField("description"),
            Row(
                FloatingField("sex", wrapper_class="form-group col-md-4 mb-0"),
                FloatingField("age", wrapper_class="form-group col-md-4 mb-0"),
                FloatingField("color", wrapper_class="form-group col-md-4 mb-0"),
            ),
            FloatingField("species"),
            FloatingField("location"),
            FloatingField("status"),
        )

    class Meta:
        model = Animal
        fields = [
            "name",
            "animal_photo",
            "description",
            "donation_fee",
            "color",
            "sex",
            "age",
            "species",
            "location",
            "status",
        ]


class SpeciesForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.label_class = "text-dark"
        self.helper.form_tag = False

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
    current_weight = MeasurementField(
        measurement=Weight,
        unit_choices=(("lb", "lb"), ("kg", "kg"), ("g", "g")),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.label_class = "text-dark"
        self.helper.form_tag = False

    class Meta:
        model = MedicalRecord
        fields = [
            "bowel_movement",
            "treatments",
            "current_weight",
            "notes",
            "q_volunteer",
        ]
