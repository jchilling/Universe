from django import forms
from .models import Universe

class UniverseForm(forms.ModelForm):
    class Meta:
        model = Universe
        fields = ['name',]
