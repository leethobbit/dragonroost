from crispy_forms.helper import FormHelper
from django import forms

from .models import Feedback
from .models import Location
from .models import Meeting


class FeedbackForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.label_class = "text-dark"
        self.helper.form_tag = False

    class Meta:
        model = Feedback
        fields = ["name", "email_address", "feedback_type", "feedback"]


class LocationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.label_class = "text-dark"
        self.helper.form_tag = False

    class Meta:
        model = Location
        fields = [
            "name",
            "description",
        ]


class MeetingForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.label_class = "text-dark"
        self.helper.form_tag = False

    class Meta:
        model = Meeting
        fields = [
            "title",
            "meeting_url",
            "minutes",
        ]
