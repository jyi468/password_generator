from django.shortcuts import render
from django.http import HttpResponse
# render(request, path, data) function allows you to pass in a template and show that


# Create your views here.
def home(request):
    return render(request, 'generator/home.html', {'password': 'fj39gvkfgl'})


def password(request):
    return render(request, 'generator/password.html')


def eggs(request):
    return HttpResponse('<h1>Eggs are so tasty</h1>')
