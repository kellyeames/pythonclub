from django import forms
from .models import Event, Resource, Meeting

class ResourceForm(forms.ModelForm):
    class Meta:
        model=Resource
        fields='__all__'

