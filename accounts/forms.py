from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + (
            "first_name", 
            "last_name", 
            "email", 
            "role", 
            "course",
        )


class ProfileForm(ModelForm):
    class Meta:
        model = CustomUser
        fields = ("first_name", "last_name", "email", "course")