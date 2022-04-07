from diagrams.models import Ai_one, Ai_two, Else
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.shortcuts import HttpResponseRedirect, render

from .forms import Current_value


def index(request):
    a = Ai_one.objects.all()
    data = a
    return render(request, 'test_case/index.html', {'data': data})

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


def diagrams(request):
    if request.user.username == 'user_one':
         model = Ai_one
    elif request.user.username == 'user_two':
        model = Ai_two
    else:
        return HttpResponseRedirect('/')
    if request.POST:
        if request.POST.get('update'):
            id = int(request.POST.get('id'))
            obj = model.objects.get(id=id)
            obj.sts = 2
            obj.save()
        elif request.POST.get('create'):
            current = request.POST.get('current', 0)
            sts = request.POST.get('sts', 0)
            model.objects.create(current=current, sts=sts)
        elif request.POST.get('delete'):
            id = int(request.POST.get('id'))
            obj = model.objects.get(id=id)
            obj.delete()
    a = model.objects.all()
    data = a
    categories = [f"{i.id}" for i in a]
    values = [float(i.current) for i in a]
    form = Current_value()
    # categories = ["2000", "2001", "2002", "2003", "2004", "2005", "2006", "2007", "2008", "2009", "2010", "2011", "2012", "2013", "2014"]
    # values = [100, 320, 453, 234, 553, 111, 345, 123, 432, 545, 654, 345, 332, 456, 234]
    return render(request, 'diagrams/diagrams.html', {'categories': categories, 'values': values, 'data': data, 'form':form})
