from django import forms
from django.forms import NumberInput

from account.models import User
from events.models import Events, Submission


class EventForm(forms.ModelForm):
    title_event = forms.CharField(max_length=255,
                                  widget=forms.TextInput(attrs={'placeholder': 'Title', 'class': 'form-control', }))
    date = forms.DateField(widget=forms.NumberInput(attrs={'type': 'date', 'class': 'form-control'}))
    poster = forms.ImageField(widget=forms.FileInput(attrs={'type': 'file'}))
    tech_info = forms.FileField(required=False, widget=forms.FileInput(attrs={'type': 'file'}))
    result = forms.URLField(required=False,
                            widget=forms.TextInput(attrs={'placeholder': 'Result', 'class': 'form-control', }))

    class Meta:
        model = Events
        fields = ['title_event', 'date', 'poster', 'tech_info', 'result']


class SubmissionForm(forms.ModelForm):
    DISTANCE_CHOICES = [
        ('м21А', 'М21А'),
        ('м21Е', 'М21Е'),
        ('ж21А', 'Ж21А'),
        ('ж21Е', 'Ж21Е'),
    ]

    CHIP_CHOICES = [
        ('y', 'Да, у меня нет своего чипа'),
        ('n', 'Нет, я возьму свой чип'),

    ]

    event = forms.ModelChoiceField(queryset=Events.objects.all(), widget=forms.HiddenInput)
    participant = forms.ModelChoiceField(queryset=User.objects.all(), widget=forms.HiddenInput)
    distance = forms.ChoiceField(choices=DISTANCE_CHOICES)
    chip = forms.ChoiceField(widget=forms.RadioSelect, choices=CHIP_CHOICES)
    num_chip = forms.IntegerField()
    agree = forms.BooleanField(label='Даю согласие на обработку данных')

    class Meta:
        model = Submission
        fields = ['distance', 'chip', 'num_chip', 'agree']

