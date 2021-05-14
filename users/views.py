from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render
from users.forms import SignUpForm, CustomUserCreationForm

def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            #login(request, user)
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account Created For {username}!')
            return redirect('lastshop-homepage')
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/register.html', {'form' : form})


