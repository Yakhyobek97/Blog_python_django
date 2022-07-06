from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True) #foydalanuvchi yoshuni kiritmasdan otib ketsa boladi true qlingani bilan

