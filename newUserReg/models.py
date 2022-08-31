from django.db import models
from datetime import datetime, date


class Register(models.Model):
    FirstName = models.CharField(max_length=100, blank=False)
    LastName = models.CharField(max_length=100, blank=False)
    email = models.EmailField(max_length=100, blank=False)
    phone = models.IntegerField(blank=False)
    password = models.CharField(max_length=200, blank=False)
    password2 = models.CharField(max_length=200, blank=False)
    Birthday_date = models.DateField(auto_now=False)
    username = models.CharField(max_length=100, blank=True, unique=True)


    def __str__(self):
        return self.username