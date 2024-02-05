from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomuserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('email',)


class CustomuserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('email',)