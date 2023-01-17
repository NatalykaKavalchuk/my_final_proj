from datetime import datetime

from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Events(models.Model):
    title_event = models.CharField(max_length=255)
    date = models.DateField()
    poster = models.ImageField(upload_to="poster/%Y")
    tech_info = models.FileField(upload_to='tech_files/%Y', blank=True, null=True)
    result = models.URLField(max_length=200, db_index=True, blank=True)
    start_date = models.DateTimeField(null=True)
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


class Registration(models.Model):
    DISTANCE_CHOICES = [
        ('м21А', 'М21А'),
        ('м21Е', 'М21Е'),
        ('ж21А', 'Ж21А'),
        ('ж21Е', 'Ж21Е'),
    ]

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='attendee')
    event = models.ForeignKey(Events, on_delete=models.SET_NULL, null=True)
    distance = models.CharField(max_length=4, choices=DISTANCE_CHOICES)
    data_reg = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)

    def __str__(self):
        return str(self.event)
