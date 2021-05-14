from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from users.models import webuser, Profile

class CustomUserCreationForm(forms.ModelForm):
    userName = forms.CharField(label='Enter Username')
    password1 = forms.CharField(label='Enter password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password',widget=forms.PasswordInput)
    deliveryAddress = forms.CharField(label=' Enter Delivery Address')
    emailAddress = forms.CharField(label='Enter email')
    phoneNumber = forms.CharField(label=' Enter Phone Number')
    profession = forms.CharField(label=' Enter profession')

    class Meta:
        model = Profile
        fields = ('userName', 'password1', 'password2', 'deliveryAddress', 'emailAddress', 'phoneNumber', 'profession', )


class AuthForm(AuthenticationForm):
    userName = forms.CharField(label='Enter Username')
    password = forms.CharField(label='Enter password')

    class Meta:
        model = Profile
        fields = ('userName', 'password', )

class SimpForm():
    userName = forms.CharField(label='Enter username')
    password = forms.CharField(label='Enter password')

    class Meta:
        model = Profile
        fields = ('userName', 'password', )