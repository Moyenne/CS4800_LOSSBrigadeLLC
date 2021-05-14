from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import redirect, render

from users import models
from users.forms import CustomUserCreationForm, AuthForm, SimpForm
from users.models import Profile


def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            userName = form.cleaned_data.get('userName')
            messages.success(request, f'Account Created For {userName}!')
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/register.html', {'form': form})


def loginls(request):
    if request.method == "POST":
        form = AuthenticationForm(Profile)
        return redirect('lastshop-homepage')
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect('lastshop-homepage')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm(Profile)
    return render(request, 'users/login.html', {'login_form': form})


