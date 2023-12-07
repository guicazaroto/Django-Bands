from django import forms
from .models import Show
from django.forms.widgets import TextInput, Select
from city.models import City
from band.models import Band


class ShowForm(forms.ModelForm):
    city = forms.ModelChoiceField(queryset=City.objects.all(), widget=Select(attrs={'class': 'form-control'}))
    band = forms.ModelChoiceField(queryset=Band.objects.all(), widget=Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Show
        fields = ['name', 'date', 'city', 'band']
        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
            'date': TextInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
        }
