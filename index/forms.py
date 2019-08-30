from django import forms
from django.forms import widgets
from bootstrap_datepicker_plus import DatePickerInput
class Searchform(forms.Form):
    searchname = forms.ChoiceField(label='Location',widget = forms.Select,choices=[("dahab","Dahab"),("sharm","Sharm")])
class Datesearch(forms.Form):
    date = forms.DateField(widget=DatePickerInput(format='%m/%d/%Y'))