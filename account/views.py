from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.cache import cache_control
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import *
from account.models import Member
from django.db import IntegrityError

# Create your views here

@login_required
def Registration(request):
    theme = request.session.get('inlineRadioOptions')
    if request.user.is_staff == 0:
        return redirect('home')

    if request.method == 'POST':
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']

        try:
            user = Member.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                email=email,
                password=password
            )
            login(request, user)
            return redirect('home')
        except IntegrityError:
            messages.error(request, 'User already have with this email', extra_tags='danger')
            return redirect('registration')
    else:
        pass
    return render(request, 'registration.html', {'theme': theme})
    

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
    theme = request.session.get('inlineRadioOptions')
    user = get_object_or_404(Member, id=request.user.id)
    if request.method == "POST":
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.save()
        return redirect('profile')
    return render(request, 'profile.html')