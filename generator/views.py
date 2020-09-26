from django.shortcuts import render
from django.http import HttpResponse
import random
# render(request, path, data) function allows you to pass in a template and show that


# Create your views here.
def home(request):
    return render(request, 'generator/home.html', {'password': 'fj39gvkfgl'})


def about(request):
    return render(request, 'generator/about.html')


def password(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()'))  # extend is the same as using + to concatenate lists

    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))

    length = int(request.GET.get('length', 12))  # GET - http verb. You can get the query parameters

    thepassword = ''
    for x in range(length):
        thepassword += random.choice(characters)

    return render(request, 'generator/password.html', {'password': thepassword})


def eggs(request):
    return HttpResponse('<h1>Eggs are so tasty</h1>')
