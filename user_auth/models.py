from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class GeneralUserManager(BaseUserManager):
    def create_user(self, phone, email, full_name, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)

        user = self.model(
            phone=phone,
            email=email,
            full_name=full_name,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone, email, full_name, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(phone, email, full_name, password, **extra_fields)

class GeneralUser(AbstractBaseUser, PermissionsMixin):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)  # Make sure email is unique
    phone = models.CharField(max_length=100, unique=True)  # Make sure phone is unique
    password = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = GeneralUserManager()

    USERNAME_FIELD = 'email'  # Use 'email' as the unique identifier
    REQUIRED_FIELDS = ['phone', 'full_name']

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_groups',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_permissions',
        blank=True,
        help_text='Specific permissions for this user.',
    )

    def __str__(self):
        return self.email
