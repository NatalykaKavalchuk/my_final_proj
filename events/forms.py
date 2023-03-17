from django import forms

from events.models import Events, Registration


class EventForm(forms.ModelForm):
    title_event = forms.CharField(max_length=255,
                                  widget=forms.TextInput(attrs={'placeholder': 'Title', 'class': 'form-control', }))
    date = forms.DateField(widget=forms.NumberInput(attrs={'type': 'date', 'class': 'form-control'}))
    poster = forms.ImageField(widget=forms.FileInput(attrs={'type': 'file'}))
    tech_info = forms.FileField(required=False, widget=forms.FileInput(attrs={'type': 'file'}))
    result = forms.URLField(required=False,
                            widget=forms.TextInput(attrs={'placeholder': 'Result', 'class': 'form-control', }))

    start_date = forms.DateTimeField(widget=forms.NumberInput(attrs={'type': 'date', 'class': 'form-control'}))
    registration_deadline = forms.DateTimeField(
        widget=forms.NumberInput(attrs={'type': 'date', 'class': 'form-control'}))

    class Meta:
        model = Events
        fields = ['title_event', 'date', 'poster', 'start_date', 'registration_deadline', 'tech_info', 'result']


class RegistrationForm(forms.ModelForm):
    first_name = forms.CharField(max_length=100, required=False, label='First Name:',
                                 widget=forms.TextInput(attrs={'class': 'form-control', }))
    last_name = forms.CharField(max_length=100, required=False, label='Last Name:',
                                widget=forms.TextInput(attrs={'class': 'form-control', }))

    class Meta:
        model = Registration
        fields = ['first_name', 'last_name', 'distance']
