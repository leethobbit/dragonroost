from django import forms
from django.forms import formset_factory
from viewflow.forms import Form, ModelForm, Layout, Row, Caption, FormSet

from . import models

COUNTRY_CHOICES = (
    ("", "Country"),
    (1, "Afghanistan"),
    (2, "Albania"),
    (3, "Algeria"),
    (5, "Andorra"),
    (10, "Argentina"),
    (11, "Armenia"),
    (13, "Australia"),
    (14, "Austria"),
    (15, "Azerbaijan"),
    (16, "Bahamas"),
)

class AnimalCommentForm(forms.ModelForm):

    class Meta:
        model = models.AnimalComment
        fields = '__all__'

AnimalCommentFormSet = formset_factory(AnimalCommentForm, extra=1, can_delete=True)

class AnimalForm(forms.ModelForm):

    name = forms.CharField(max_length=80)
    age = forms.IntegerField()
    comments = FormSet(AnimalCommentForm)
    class Meta:
        model = models.Animal
        fields = '__all__'