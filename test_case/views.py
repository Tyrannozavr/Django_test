from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.shortcuts import HttpResponseRedirect


def index(request):
    return render(request, 'test_case/index.html')

def register(request):
    if request.POST:
        if request.POST['type'] == 'login':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                return render(request, 'test_case/register.html', {'message': 'user is not exist'})
        elif request.POST['type'] == 'register':
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            try:
                user = User.objects.create_user(username, email, password)
                login(request, user)
                return HttpResponseRedirect('/')
            except IntegrityError:
                return render(request, 'test_case/register.html', {'message': 'user is taken'})
    return render(request, 'test_case/register.html')


def Logout(request):
    logout(request)
    return render(request, 'test_case/index.html')