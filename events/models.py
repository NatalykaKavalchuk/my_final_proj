from datetime import datetime

from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


# User = get_user_model()


class User(models.Model):
    username = models.CharField(max_length=100, primary_key=True, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password1 = models.CharField(max_length=50)
    password2 = models.CharField(max_length=50)

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('register', kwargs={'username': self.username})

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"


class Events(models.Model):
    title_event = models.CharField(max_length=255)
    date = models.DateField()
    poster = models.ImageField(upload_to="poster/%Y")
    tech_info = models.FileField(upload_to='tech_files/%Y', blank=True, null=True)
    result = models.URLField(max_length=200, db_index=True, blank=True)
    participants = models.ManyToManyField(User, blank=True)
    start_date = models.DateTimeField(null=True)
    end_date = models.DateTimeField(null=True)
    registration_deadline = models.DateTimeField(null=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title_event

    def get_absolute_url(self):
        return reverse('details', kwargs={'id': self.id})

    class Meta:
        verbose_name = "Event"
        verbose_name_plural = "Events"

    @property
    def event_status(self):
        status = None

        present = datetime.now().timestamp()
        deadline = self.registration_deadline.timestamp()
        past_deadline = (present > deadline)

        if past_deadline:
            status = 'Finished'
        else:
            status = 'Ongoing'

        return status


class Submission(models.Model):
    # DISTANCE_CHOICES = [
    #     ('м21А', 'М21А'),
    #     ('м21Е', 'М21Е'),
    #     ('ж21А', 'Ж21А'),
    #     ('ж21Е', 'Ж21Е'),
    # ]
    #
    # CHIP_CHOICES = [
    #     ('y', 'Да, у меня нет своего чипа'),
    #     ('n', 'Нет, я возьму свой чип'),
    #
    # ]

    participant = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    event = models.ForeignKey(Events, on_delete=models.SET_NULL, null=True)
    #
    # distance = models.CharField(max_length=4, choices=DISTANCE_CHOICES)
    # chip = models.CharField(max_length=1, choices=CHIP_CHOICES)
    # num_chip = models.CharField(max_length=10)
    # agree = models.BooleanField(null=True)

    def __str__(self):
        return str(self.event)
