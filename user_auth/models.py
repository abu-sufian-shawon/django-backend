from django.contrib.auth.models import AbstractUser, AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.db import models
from .managers import CustomUserManager

class CustomUser(AbstractBaseUser, PermissionsMixin):
    # username = None
    email = models.EmailField(_('email address'), unique = True)
    is_staff = models.BooleanField(default = False)
    is_superuser = models.BooleanField(default = True)
    date_joined = models.DateTimeField(default = timezone.now)
    is_active = models.BooleanField(default = False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email