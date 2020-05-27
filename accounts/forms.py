from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError


class UserLoginForm(forms.Form):
    """Form to log user in"""

    username = forms.CharField(max_length=40)
    password = forms.CharField(widget=forms.PasswordInput, max_length=40)


class UserRegistrationForm(UserCreationForm):
    """Form used to register a new user"""

    password1 = forms.CharField(label='Password',
                                widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password Confirmation',
                                widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = [
            'name', 'surname', 'username', 'birth_date', 'email',
            'password1', 'password2', 'address1', 'address2',
            'city', 'county', 'country', 'license_category'
        ]
