from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from web.forms import SignUpForm
from django.shortcuts import render, redirect, get_object_or_404
from .models import Category, User
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required
import os
from .models import Image


# Create your views here.
@login_required()
def home(request):
    latest_categories_list = Category.objects.order_by('-pub_date')[:5]
    context = {'latest_categories_list': latest_categories_list}

    return render(request, 'web/home.html', context=context)


@login_required()
def simple_upload(request):
    dirName = f'media/{request.user.username}'
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        if not os.path.exists(dirName):
            os.mkdir(dirName)
        filename = fs.save(request.user.username + '/' + myfile.name, myfile)
        uploaded_file_url = fs.url(filename)

        image = Image(author=request.user, title=myfile.name,
                      file=filename,
                      file_path=uploaded_file_url, )
        image.save()

        return render(request, 'web/profile.html')
    return render(request, 'web/profile.html')


def view_profile(request, username):
    user = get_object_or_404(User, username=username)
    email = user.email
    user_images = Image.objects.all().filter(author=user)
    context = {'user_images': user_images}
    return render(request, 'web/view_profile.html', context=context)



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
        print(request)
        print(request.user.pk)
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
