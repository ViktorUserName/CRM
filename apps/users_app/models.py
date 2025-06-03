from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    ROLE_CHOICES = (
        ('manager', 'Manager'),
        ('support', 'Support'),
    )

    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='manager')

    def __str__(self):
        return f'{self.username} - {self.role}'
