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

class SearchForm(forms.Form):

    starsearch = forms.CharField(
        label = 'Search by Star Name', 
        required = True,   
        max_length = 25,
        widget=forms.TextInput(attrs={'placeholder': 'Del Ori'}),
    )
