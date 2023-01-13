from django.db import models
from django.urls import reverse


class User(models.Model):
    username = models.CharField(max_length=100, primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    password1 = models.CharField(max_length=50)
    password2 = models.CharField(max_length=50)

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('register', kwargs={'username': self.username})

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
