from django import forms
from .models import ObsField

class ObsForm(forms.Form):
    """ Form for submitting observations """
    

    field = forms.ModelChoiceField(
        label = 'Observation Field',
        queryset = ObsField.objects.all(),
    )

    obsfile = forms.FileField(
        label = "Observation File",
        required = True,     
    )
