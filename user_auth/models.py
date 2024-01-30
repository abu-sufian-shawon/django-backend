from django.db import models
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.
class CustomUser(AbstractBaseUser):
    # user_groups = models.ManyToManyField('user_auth.CustomUser.Groups', related_name='user_auth.CustomUser.groups')
    # user_permissions = models.ManyToManyField('user_auth.CustomUser.Permissions', related_name='custom_users_permissions')
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    USERNAME_FIELD = 'phone'

    def __str__(self) -> str:
        return self.full_name