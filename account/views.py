from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.cache import never_cache, cache_control
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import *

# Create your views here

def Registration(request):
    if request.method == 'POST':
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']

        user = Member.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password
        )
        login(request, user)
        return redirect('home')
    else:
        pass

    return render(request, 'registration.html')

def Login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Email or Password is wrong.')
    else:
        pass
    return render(request, 'login.html')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def Logout(request):
    logout(request)
    return redirect('home')

@login_required
def Profile(request):
    return render(request, 'profile.html')