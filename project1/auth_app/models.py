from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    ROLES = (
        ('ADMIN', 'ADMIN'),
        ('USER', 'USER')
    )

    role = models.CharField(max_length=20, choices=ROLES, default='USER')