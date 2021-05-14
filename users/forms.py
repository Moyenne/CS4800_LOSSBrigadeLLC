from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from users.models import webuser, Profile

class CustomUserCreationForm(forms.ModelForm):
    username = forms.CharField(label='Enter Username')
    email = forms.EmailField(label='Enter email')
    password1 = forms.CharField(label='Enter password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)
    deliveryAddress = forms.CharField(label=' Enter Delivery Address')
    phoneNumber = forms.CharField(label=' Enter Phone Number')
    profession = forms.CharField(label=' Enter profession')

    class Meta:
        model = Profile
        fields = ('username', 'email', 'password1', 'password2', 'deliveryAddress', 'phoneNumber', 'profession', )


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length = 30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )
