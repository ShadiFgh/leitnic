from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from web.forms import SignUpForm
from django.shortcuts import render, redirect
from .models import Category


# Create your views here.

def home(request):
    latest_categories_list = Category.objects.order_by('-pub_date')[:5]
    context = {'latest_categories_list': latest_categories_list}

    return render(request, 'web/home.html', context=context)


@csrf_exempt
def log_in(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['pass']
        username = User.objects.all().filter(email=email)[0].username
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


@csrf_exempt
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'web/signup.html', {'form': form})


def send_sms(request):
    pass
