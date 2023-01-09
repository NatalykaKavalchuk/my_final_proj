from django.db import models
from django.urls import reverse


class Events(models.Model):

    title_event = models.CharField(max_length=255)
    date = models.DateField()
    poster = models.ImageField(upload_to="poster/%Y")
    tech_info = models.FileField(upload_to='tech_files', blank=True, null=True)
    result = models.URLField(max_length=200, db_index=True, blank=True)
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






