from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.urls import reverse


def login_view(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('home/')
        else:
            return render(request, 'authentication/login.html')
            
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.info(request, 'User has been successfully logined in')
            return redirect('home/')
        else:
            messages.info(request, 'Invalid credentials')
            return redirect('/')
    return render(request, 'authentication/login.html')

def signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        password_confirmation = request.POST['password_confirmation']

        if username == '':
            messages.error(request, 'User name cannot be empty')

        if User.objects.filter(username=username).exists():
            messages.info(request,'User already exists, Please try with a different user name')
            return render(request, 'authentication/signup.html')

        if User.objects.filter(email=email).exists():
            messages.info(request,'A user is already logged in with the provided email')
            return render(request, 'authentication/signup.html')

        if password != password_confirmation:
            messages.info(request,'Password doesn"t match please try again')
    
        else:
            user = User.objects.create_user(username = username,password=password, email=email)
            user.save()
            messages.info(request, ' you have been successfully signed in')
            return redirect('/')
    return render(request, 'authentication/signup.html')


def logout_view(request):
    logout(request)
    messages.info(request, 'User has been successfully logged out')
    return HttpResponseRedirect(reverse('authentication:login'))