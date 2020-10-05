from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from json import JSONEncoder
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from datetime import datetime
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def home(request):
    return render(request, 'web/home.html')


@csrf_exempt
def register(request):
    if request.method == 'POST':
        print(request.POST)
        print("Username: ", request.POST['username'])
        print("Email: ", request.POST['email'])
        print("Password: ", request.POST['pass'])
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['pass']
        #  Register
        user = User.objects.create_user(username=username, email=email, password=password)

    elif request.method == 'GET':
        return render(request, 'web/register.html')


@csrf_exempt
def log_in(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['pass']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/home/')
        else:
            return HttpResponse("User not found.")
    elif request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('/home/')
        else:
            return render(request, 'web/login.html')


@csrf_exempt
def log_out(request):
    if request.method == 'GET':
        logout(request)
        return render(request, 'web/logout.html')
