from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# todo for future work

# class Profile(models.Model):
#     username = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     email = models.EmailField(unique=True)
#     date_of_birth = models.DateField()
#     data_reg = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)
#
#     def __str__(self):
#         return 'Profile' + str(self.username)
#
#     def delete(self, *args, **kwargs):
#         self.first_name.delete()
#         self.last_name.delete()
#         self.email.delete()
#         self.date_of_birth.delete()
#         self.data_reg.delete()
#         super().delete(*args, **kwargs)
#
#     def get_absolute_url(self):
#         return reverse('register', kwargs={'username': self.username})
#
#     class Meta:
#         verbose_name = "Profile"
#         verbose_name_plural = "Profiles"
