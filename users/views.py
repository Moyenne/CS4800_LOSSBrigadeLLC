from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render
from users.forms import UserRegisterForm, SignUpForm, CustomusercreationForm


def register(request):
    if request.method == "POST":
        form = CustomusercreationForm(request.POST)
        if form.is_valid():
            form.save()
            #username = form.cleaned_data.get('username')
            messages.success(request, f'Account Created For') #{username}!')
            return redirect('lastshop-home')
    else:
        form = CustomusercreationForm()
    return render(request, 'users/register.html', {'form' : form})

#def signup(request):
#    if request.method == 'POST':
#        form = SignUpForm(request.POST)
#        if form.is_valid():
#            form.save()
#            username = form.cleaned_data.get('username')
#            raw_password = form.cleaned_data.get('password1')
#            user = authenticate(username=username, password=raw_password)
#            login(request, user)
#            return redirect('home')
#    else:
#        form = SignUpForm()
#    return render(request, 'users/register.html', {'form': form})
#
#def login(request):
#    if request.method == 'GET':
#        context = ''
#        return render(request, 'mytest/login.html', {'context': context})
#
#    elif request.method == 'POST':
#        username = request.POST.get('username', '')
#        password = request.POST.get('password', '')
#
#        user = authenticate(request, username=username, password=password)
#        if user is not None:
#            login(request, user)
#            # Redirect to a success page?
#            # return HttpResponseRedirect('/')
#        else:
#            context = {'error': 'Wrong credintials'}  # to display error?
#            return render(request, 'mytest/login.html', {'context': context})