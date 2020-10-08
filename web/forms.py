from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    phone = forms.CharField(max_length=16, help_text='Required. Inform a valid phone number.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'phone', 'password1', 'password2', )
