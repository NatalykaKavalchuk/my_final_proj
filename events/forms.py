from django import forms
from django.forms import NumberInput

from events.models import Events


class EventForm(forms.ModelForm):
    date = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))

    class Meta:
        model = Events
        fields = ['title_event', 'date', 'poster', 'tech_info', 'result']

