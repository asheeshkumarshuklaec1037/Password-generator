from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def home(request):
    return render(request,'generator/home.html',{'password':'ashashash'})

def password(request):
    character = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        character.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    
    if request.GET.get('special'):
        character.extend(list('!@#$%^&*'))

    if request.GET.get('numbers'):
        character.extend(list('0123456789'))

    length = int(request.GET.get('length'))
    thepassword = ''
    for _ in range(length):
        thepassword+= random.choice(character)
    return render(request,'generator/password.html',{'password':thepassword})

def aboutpage(request):
    return render(request,'generator/about.html')