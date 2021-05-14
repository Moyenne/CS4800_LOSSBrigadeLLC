from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.core.exceptions import ValidationError


class CustomusercreationForm(forms.Form):
    username = forms.CharField(label='Enter Username', min_length=3, max_length=150)
    email = forms.EmailField(label='Enter email')
    password1 = forms.CharField(label='Enter password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)
    deliveryAddress = forms.CharField(label=' Enter Delivery Address')
    phoneNumber = forms.CharField(label=' Enter Phone Number')
    profession = forms.CharField(label=' Enter profession')


    def save(self, commit=True):
        user = User.objects.create_user(
            self.cleaned_data['username'],
            self.cleaned_data['email'],
            self.cleaned_data['password1'],
            self.cleaned_data['deliveryAddress'],
            self.cleaned_data['phoneNumber'],
            self.cleaned_data['profession']
        )
        return user


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length = 30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    deliveryAddress = forms.DeliveryAddressField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user



#   def clean_username(self):
#       username = self.cleaned_data['username'].lower()
#       r = User.objects.filter(username=username)
#       if r.count():
#           raise ValidationError("Username already exists")
#       return username

#   def clean_email(self):
#       email = self.cleaned_data['email'].lower()
#       r = User.objects.filter(email=email)
#       if r.count():
#           raise ValidationError("Email already exists")
#       return email

#   def clean_password2(self):
#       password1 = self.cleaned_data.get('password1')
#       password2 = self.cleaned_data.get('password2')

#       if password1 and password2 and password1 != password2:
#           raise ValidationError("Password don't match")

#       return password2

