from django.contrib.auth.forms import UserCreationForm, BaseUserManager
from .models import CustomUser
# class CustomUserCreationForm(UserCreationForm):
#       class Meta(UserCreationForm.Meta):
#             model = CustomUser
#             fields = UserCreationForm.Meta.fields + ('full_name', 'phone', 'email', 'password',)