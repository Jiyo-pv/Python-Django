# Program 31: Role-Based Authentication
# @JIYO P V ROLL NO:33 Date: 01-03-2026

from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20)

    def __str__(self):
        return self.user.username