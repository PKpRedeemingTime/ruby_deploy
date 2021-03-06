from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Q, Count
from django.core.urlresolvers import reverse
import bcrypt, datetime
from .models import User

def index(request):
    return render(request, 'mainApp/index.html')

def login(request):
    result = User.objects.login(request.POST, request)
    if result == True:
        return redirect(reverse('success'))
    else:
        return redirect(reverse('index'))

def registration(request):
    result = User.objects.register(request.POST, request)
    if result == True:
        return redirect(reverse('success'))
    else:
        return redirect(reverse('index'))
    
def success(request):
    context = {
        "users" : User.objects.all(),
    }
    return render(request, 'mainApp/success.html', context)