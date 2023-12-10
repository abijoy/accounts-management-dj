from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
    

class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    dob = models.DateField(blank=True, null=True)

    # calculate age
    @property
    def age(self):
        from datetime import date
        today = date.today()
        return f'{today.year - self.dob.year} years {today.month - self.dob.month} month(s) and {today.day - self.dob.day} day(s)'
    
    def __str__(self) -> str:
        return f'Profile for user: {self.user.email}'
