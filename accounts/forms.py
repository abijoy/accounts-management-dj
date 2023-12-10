from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('email', )


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('email',)

class LoginForm(AuthenticationForm):
    # email = forms.EmailField(widget=forms.EmailInput)
    password = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={'placeholder':'password'}))