from django import forms
from django.forms import ModelForm
from django.forms import widgets
from divers.models import divers
from django.forms import ModelForm
from bookings.models import dive
from bootstrap_datepicker_plus import DateTimePickerInput
class divebook(ModelForm):
    class Meta:
        model= dive
        fields=['location','date','diver','cost']
        widgets = {
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'date': DateTimePickerInput(),
            'diver': forms.Select(attrs={'class': 'form-control'}),
            'cost': forms.NumberInput(attrs={'class': 'form-control'}),
            
        }


