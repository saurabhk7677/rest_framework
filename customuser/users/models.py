from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
# from django.utils.translation import ugettext_lazy as _
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager


class CustomUser(AbstractUser):
    username = models.CharField(max_length=100, blank=False, null=False, unique=True)
    email = models.EmailField(_('email address'), blank=True,null=True, unique=True)
    first_name = models.CharField(max_length=150, blank=False, null=False)
    last_name = models.CharField(max_length=150, blank=False, null=False)
    password_hint = models.CharField(max_length=150,blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(null=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email','first_name', 'last_name', 'phone']

    objects = CustomUserManager()

    # spouse_name = models.CharField(blank=True, max_length=100)
    
    

    def __str__(self):
        return self.email