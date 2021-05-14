from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from users.models import webuser, Profile

class CustomUserCreationForm(forms.ModelForm):
    userName = forms.CharField(label='Enter Username')
    password1 = forms.CharField(label='Enter password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)
    deliveryAddress = forms.CharField(label=' Enter Delivery Address')
    emailAddress = forms.EmailField(label='Enter email')
    phoneNumber = forms.CharField(label=' Enter Phone Number')
    profession = forms.CharField(label=' Enter profession')

    class Meta:
        model = Profile
        fields = ('userName', 'password1', 'password2', 'deliveryAddress', 'emailAddress', 'phoneNumber', 'profession', )



