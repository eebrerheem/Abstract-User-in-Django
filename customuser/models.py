from pyexpat import model
from django.db import models
from django.contrib.auth.models import AbstractUser

class NewUser(AbstractUser):
    other_name = models.CharField(max_length=20, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    work = models.CharField(max_length=100, blank=True, null=True)
    location = models.CharField(max_length=50, blank=True, null=True)
    
