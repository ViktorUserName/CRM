import datetime

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    ROLE_CHOICES = (
        ('manager', 'Manager'),
        ('support', 'Support'),
    )

    first_name = models.CharField(max_length=30, null=False, blank=False)
    last_name = models.CharField(max_length=30, null=False, blank=False)
    email = models.EmailField(unique=True, null=False, blank=False)
    gender = models.CharField(max_length=10, blank=True, default='male')
    birthday = models.DateField(blank=True, null=True, default=datetime.date.today)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='manager')
    username = models.CharField(max_length=30, unique=True, default='employee')

    @property
    def full_age(self):
        """Вычисляет возраст на текущую дату"""
        if not self.birthday:
            return None
        today = datetime.date.today()
        return today.year - self.birthday.year - (
                (today.month, today.day) < (self.birthday.month, self.birthday.day)
        )

    def __str__(self):
        return f'{self.username} - {self.role}'
