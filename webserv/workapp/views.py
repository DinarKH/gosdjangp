from django.shortcuts import render, HttpResponse, redirect
import os
from django.conf import settings
from .forms import RegistrationForm
from .models import RegistrationForm as RegMod


def some(request):
    sour = os.path.join(settings.BASE_DIR,'1.txt')
    f = open(sour,'r+')
    print(f.readline())
    return render(request,'base.html',
                  {
                    'asd':'/static/1.jpg',
                  })

def validation(request):
    if request.method == 'GET':
        form = RegistrationForm()
    else:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            model = RegMod()
            model.name = form.cleaned_data['name']
            model.email = form.cleaned_data['email']
            model.password = form.cleaned_data['password']
            model.home = form.cleaned_data['home']
            model.save()
            return redirect('/user/')
    return render(request, "registration.html", {'form': form})

def user(request):
    user = RegMod.objects.last()
    return render(request, "user.html", {
        'user': user})


def navigate(request):
    if request.method == 'POST':
        print(request.POST.get('user_id'))
    return render(request,'navigate.html',)