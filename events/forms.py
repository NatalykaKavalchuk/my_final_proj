from django import forms
from django.forms import NumberInput

from events.models import Events


class EventForm(forms.ModelForm):

    title_event = forms.CharField(max_length=255,
                                  widget=forms.TextInput(attrs={'placeholder': 'Title', 'class': 'form-control', }))
    date = forms.DateField(widget=forms.NumberInput(attrs={'type': 'date', 'class': 'form-control',}))
    poster = forms.ImageField(widget=forms.FileInput(attrs={'type': 'file'}))
    tech_info = forms.FileField(widget=forms.FileInput(attrs={'type': 'file'}))
    result = forms.URLField(widget=forms.TextInput(attrs={'placeholder': 'Result', 'class': 'form-control', }))

    class Meta:
        model = Events
        fields = ['title_event', 'date', 'poster', 'tech_info', 'result']



